# Crawlr — Universal Web Scraper
© Saksham Srivastava — sakshamsrivastava7000@gmail.com

Paste **any URL** → extracts headings, paragraphs, links, images, prices, meta tags.
Displays everything in a dark minimal dashboard with search + filtering per category.

---

## Usage

### Option A — Live in browser (paste URL directly)
Just open `frontend/index.html` in your browser and paste any URL.
Uses a CORS proxy (allorigins.win) to fetch pages client-side.

### Option B — Python scraper (no CORS limits, more reliable)
```bash
pip install requests beautifulsoup4   # optional, stdlib version works too

python scraper.py https://example.com
# → saves to output/result.json

# Then open frontend/index.html — it auto-loads result.json
```

---

## What it extracts

| Category   | Details |
|------------|---------|
| Headings   | h1–h6 with level badge |
| Paragraphs | All `<p>` text blocks > 40 chars |
| Links      | href, link text, internal/external flag |
| Images     | src, alt text, thumbnail preview |
| Prices     | Regex-detected £$€₹¥ amounts |
| Meta       | All `<meta>` name/property + content |

---

## Structure

```
universal-scraper/
├── scraper.py          ← Python CLI scraper (zero deps)
├── frontend/
│   └── index.html      ← Dashboard UI
├── output/
│   └── result.json     ← Generated after running scraper.py
└── README.md
```
