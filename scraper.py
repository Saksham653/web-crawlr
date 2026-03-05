#!/usr/bin/env python3
"""
scraper.py — Universal web scraper
Extracts everything from any URL: headings, text, links, images, prices, meta.
© Saksham Srivastava — sakshamsrivastava7000@gmail.com
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse


# ── Minimal HTML parser (no deps beyond stdlib) ──────────────────────────────

class UniversalParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.headings   = []
        self.links      = []
        self.images     = []
        self.prices     = []
        self.paragraphs = []
        self.meta       = {}

        self._current_tag  = None
        self._current_text = []
        self._in_skip      = False
        self._skip_tags    = {"script", "style", "noscript", "head"}
        self._heading_tags = {"h1", "h2", "h3", "h4", "h5", "h6"}
        self._price_re     = re.compile(
            r'[\$\£\€\₹\¥]?\s*\d{1,6}(?:[.,]\d{2,3})*(?:\.\d{2})?'
        )

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._current_tag = tag

        if tag in self._skip_tags:
            self._in_skip = True
            return

        # Links
        if tag == "a" and attrs.get("href"):
            href = attrs["href"].strip()
            if href and not href.startswith(("#", "javascript")):
                full = urljoin(self.base_url, href)
                text_hint = attrs.get("title") or attrs.get("aria-label") or ""
                self.links.append({"url": full, "hint": text_hint})

        # Images
        if tag == "img":
            src = attrs.get("src") or attrs.get("data-src") or attrs.get("data-lazy-src") or ""
            if src:
                full = urljoin(self.base_url, src.strip())
                alt  = attrs.get("alt", "").strip()
                self.images.append({"src": full, "alt": alt})

        # Meta
        if tag == "meta":
            name    = attrs.get("name") or attrs.get("property") or ""
            content = attrs.get("content", "").strip()
            if name and content:
                self.meta[name] = content

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._in_skip = False

        text = " ".join(self._current_text).strip()
        self._current_text = []

        if not text or self._in_skip:
            return

        if tag in self._heading_tags:
            self.headings.append({"level": tag, "text": text})

        elif tag == "p" and len(text) > 30:
            self.paragraphs.append(text)

        # Price detection on any element
        prices_found = self._price_re.findall(text)
        for p in prices_found:
            p = p.strip()
            if p and p not in self.prices:
                self.prices.append(p)

    def handle_data(self, data):
        if not self._in_skip:
            clean = data.strip()
            if clean:
                self._current_text.append(clean)


# ── Fetch + parse ─────────────────────────────────────────────────────────────

def fetch(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (compatible; UniversalScraper/1.0; "
                "+https://github.com/saksham; sakshamsrivastava7000@gmail.com)"
            ),
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.9",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = "utf-8"
        ct = resp.headers.get_content_charset()
        if ct:
            charset = ct
        return resp.read().decode(charset, errors="replace")


def scrape(url: str) -> dict:
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url

    html  = fetch(url)
    parser = UniversalParser(url)
    parser.feed(html)

    # Page title from meta or first h1
    title = (
        parser.meta.get("og:title")
        or parser.meta.get("title")
        or (parser.headings[0]["text"] if parser.headings else "")
        or urlparse(url).netloc
    )

    description = (
        parser.meta.get("og:description")
        or parser.meta.get("description")
        or (parser.paragraphs[0] if parser.paragraphs else "")
    )

    return {
        "url":         url,
        "title":       title,
        "description": description,
        "meta":        parser.meta,
        "headings":    parser.headings[:40],
        "paragraphs":  parser.paragraphs[:30],
        "links":       parser.links[:80],
        "images":      parser.images[:40],
        "prices":      list(dict.fromkeys(parser.prices))[:30],
        "stats": {
            "headings":   len(parser.headings),
            "paragraphs": len(parser.paragraphs),
            "links":      len(parser.links),
            "images":     len(parser.images),
            "prices":     len(parser.prices),
        },
    }


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Universal web scraper")
    ap.add_argument("url", help="URL to scrape")
    ap.add_argument("-o", "--output", default="output/result.json", help="Output JSON path")
    args = ap.parse_args()

    import os
    os.makedirs("output", exist_ok=True)

    print(f"\n  Scraping → {args.url}")
    try:
        data = scrape(args.url)
    except Exception as e:
        print(f"  ✗ Error: {e}", file=sys.stderr)
        sys.exit(1)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    s = data["stats"]
    print(f"  ✓ Done!")
    print(f"     Headings : {s['headings']}")
    print(f"     Paragraphs: {s['paragraphs']}")
    print(f"     Links    : {s['links']}")
    print(f"     Images   : {s['images']}")
    print(f"     Prices   : {s['prices']}")
    print(f"     Saved to : {args.output}\n")


if __name__ == "__main__":
    main()
