<div align="center">

<!-- ANIMATED LOGO -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 160" width="480" height="160">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&amp;family=Lora:ital,wght@1,600&amp;display=swap');

      .bg { fill: #070707; }
      .logo-main {
        font-family: 'Syne', sans-serif;
        font-size: 72px;
        font-weight: 800;
        fill: #edebe4;
        letter-spacing: -4px;
      }
      .logo-em {
        font-family: 'Lora', serif;
        font-style: italic;
        font-weight: 600;
        fill: #72bba0;
      }
      .badge-text {
        font-family: 'Courier New', monospace;
        font-size: 9px;
        letter-spacing: 3px;
        text-transform: uppercase;
        fill: #3f8066;
      }
      .orb { opacity: 0; animation: orbIn 1.4s ease forwards; }
      .logo-text { opacity: 0; animation: fadeUp 0.9s 0.2s ease forwards; }
      .badge { opacity: 0; animation: fadeUp 0.9s 0.1s ease forwards; }
      .scan { animation: scanLoop 4s ease-in-out infinite; }
      .dot1 { animation: pulse 1.2s 0s ease-in-out infinite; }
      .dot2 { animation: pulse 1.2s 0.4s ease-in-out infinite; }
      .dot3 { animation: pulse 1.2s 0.8s ease-in-out infinite; }
      .spider-line { stroke-dasharray: 100; stroke-dashoffset: 100; animation: drawLine 1.5s 0.6s ease forwards; }
      .cursor-blink { animation: blink 0.85s step-end infinite; }

      @keyframes orbIn { from { opacity: 0; } to { opacity: 1; } }
      @keyframes fadeUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
      @keyframes scanLoop { 0% { transform: translateY(-20px); opacity: 0; } 15% { opacity: 1; } 85% { opacity: 0.3; } 100% { transform: translateY(160px); opacity: 0; } }
      @keyframes pulse { 0%, 100% { opacity: 1; r: 3; } 50% { opacity: 0.3; r: 1.5; } }
      @keyframes drawLine { to { stroke-dashoffset: 0; } }
      @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    </style>

    <!-- Glow gradient -->
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3f8066" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#3f8066" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#9077c5" stop-opacity="0.07"/>
      <stop offset="100%" stop-color="#9077c5" stop-opacity="0"/>
    </radialGradient>

    <!-- Dot grid pattern -->
    <pattern id="dots" x="0" y="0" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="12" cy="12" r="0.8" fill="#222222"/>
    </pattern>
    <mask id="fade-mask">
      <radialGradient id="mask-grad" cx="50%" cy="50%" r="50%">
        <stop offset="20%" stop-color="white"/>
        <stop offset="100%" stop-color="black"/>
      </radialGradient>
      <rect width="480" height="160" fill="url(#mask-grad)"/>
    </mask>
  </defs>

  <!-- Background -->
  <rect width="480" height="160" class="bg" rx="12"/>

  <!-- Dot grid -->
  <rect width="480" height="160" fill="url(#dots)" mask="url(#fade-mask)" opacity="0.6"/>

  <!-- Glow orbs -->
  <ellipse class="orb" cx="240" cy="60" rx="280" ry="120" fill="url(#glow)"/>
  <ellipse class="orb" cx="400" cy="130" rx="160" ry="80" fill="url(#glow2)"/>

  <!-- Scan line -->
  <rect class="scan" x="0" y="0" width="480" height="50" fill="url(#glow)" opacity="0.4"/>

  <!-- Badge -->
  <g class="badge">
    <rect x="162" y="14" width="156" height="20" rx="10" fill="rgba(63,128,102,0.08)" stroke="rgba(63,128,102,0.2)" stroke-width="1"/>
    <circle class="dot1" cx="173" cy="24" r="3" fill="#3f8066"/>
    <text x="182" y="28" class="badge-text">Universal Scraper</text>
  </g>

  <!-- Spider web accent lines -->
  <line class="spider-line" x1="30" y1="20" x2="80" y2="80" stroke="#3f8066" stroke-width="0.6" opacity="0.4"/>
  <line class="spider-line" x1="80" y1="80" x2="30" y2="140" stroke="#3f8066" stroke-width="0.6" opacity="0.4"/>
  <line class="spider-line" x1="80" y1="80" x2="140" y2="80" stroke="#3f8066" stroke-width="0.6" opacity="0.3"/>
  <line class="spider-line" x1="450" y1="20" x2="400" y2="80" stroke="#9077c5" stroke-width="0.6" opacity="0.3"/>
  <line class="spider-line" x1="400" y1="80" x2="450" y2="140" stroke="#9077c5" stroke-width="0.6" opacity="0.3"/>

  <!-- Main logo text -->
  <text class="logo-text" x="240" y="115" text-anchor="middle" class="logo-main">
    <tspan class="logo-main">Crawl</tspan><tspan class="logo-main logo-em">r</tspan>
  </text>

  <!-- Pulsing dots decoration -->
  <circle class="dot2" cx="115" cy="95" r="3" fill="#72bba0" opacity="0.6"/>
  <circle class="dot3" cx="365" cy="95" r="3" fill="#72bba0" opacity="0.6"/>

  <!-- Cursor blink after logo -->
  <rect class="cursor-blink" x="308" y="88" width="5" height="14" fill="#72bba0" rx="1"/>

  <!-- Bottom tagline -->
  <text x="240" y="148" text-anchor="middle" font-family="'Courier New', monospace" font-size="8.5" letter-spacing="2.5" fill="#595959" text-transform="uppercase">BROWSER · PYTHON · ZERO DEPS · 4 EXPORT FORMATS</text>
</svg>

<br/>

[![Live Demo](https://img.shields.io/badge/🔍_Live_App-saksham653.github.io-3f8066?style=for-the-badge&labelColor=0d0d0d)](https://saksham653.github.io/web-crawlr/)
[![GitHub](https://img.shields.io/badge/GitHub-Saksham653-72bba0?style=for-the-badge&logo=github&logoColor=white&labelColor=0d0d0d)](https://github.com/Saksham653/web-crawlr)
[![Email](https://img.shields.io/badge/Email-sakshamsrivastava7000-c8a050?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d0d0d)](mailto:sakshamsrivastava7000@gmail.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3f8066?style=for-the-badge&logo=python&logoColor=white&labelColor=0d0d0d)](https://www.python.org/)
[![Zero Deps](https://img.shields.io/badge/Dependencies-0-9077c5?style=for-the-badge&labelColor=0d0d0d)]()

</div>

---

```
  Scraping → https://books.toscrape.com

  [1/3] Fetching page…
  [2/3] Parsing HTML structure…
  [3/3] Writing output…

  ✓ Complete
      Headings    42
      Paragraphs  18
      Links       94
      Images      61
      Prices      50  ← ₹ $ £ € ¥ detected
      Saved →     output/result.json
```

---

## What is Crawlr?

**Crawlr** is a universal web scraper that works in two ways — paste a URL in your browser and get instant results, or run the Python CLI locally for more power. No configuration, no selectors to write, no dependencies to install. Just point it at any URL and get back clean, structured data across six categories — ready to search, filter, and export.

Built entirely from scratch. Every line of HTML, CSS, JavaScript and Python written by hand. Zero external libraries, start to finish.

---

## ✦ Feature Highlights

### 🔍 Six Data Types — Automatically Detected

| Category | What it captures |
|----------|-----------------|
| **Headings** | h1–h6 with level badges — H1 in gold, H2 in teal, H3–H6 in muted tones |
| **Paragraphs** | All `<p>` blocks over 40 chars — deduplicated, trimmed, fully searchable |
| **Links** | Every href resolved to absolute URL — internal vs external flagged automatically |
| **Images** | `src` + `alt` text — handles `data-src` and lazy-loaded attributes |
| **Prices** | Regex-matched ₹ $ £ € ¥ amounts — parsed to numeric values for comparison |
| **Meta Tags** | Open Graph, Twitter Cards, `description`, `keywords`, charset — full `<meta>` table |

### 📊 Price Tracker
Track any product URL over time. Set a target price, hit refresh — Crawlr fetches the latest price, stores history, and renders sparkline charts inline. A **TARGET HIT** badge fires when your price is reached. All data persists in `localStorage` across sessions. Export your tracking history as CSV at any time.

### 📥 Four Export Formats
Choose exactly which sections to include with checkboxes. Preview the output live before downloading. Files are named automatically with domain + date.

| Format | Best for |
|--------|----------|
| **JSON** | APIs, developer pipelines, structured data |
| **CSV** | Excel, Google Sheets, flat row analysis |
| **Markdown** | GitHub, Notion, Obsidian, readable reports |
| **HTML** | Standalone shareable pages, archiving |

### ⚡ Dual Scraper Modes

**Browser Mode** — No install needed. Paste any URL and go. Uses a 3-proxy fallback chain (`allorigins.win → corsproxy.io → codetabs.com`), each with a 10-second timeout. Usually resolves in 2–5 seconds.

**Python Mode** — Run locally for sites that block proxies. Zero pip installs — pure Python stdlib. Spoofed `User-Agent` headers bypass most basic bot detectors. The dashboard auto-detects `output/result.json` on startup and populates all 8 tabs automatically.

---

## 🚀 Quick Start

### Option A — Browser (No Install)

Open the live app and paste any URL:

**[→ Launch Crawlr](https://saksham653.github.io/web-crawlr/)**

Or open `frontend/index.html` locally in any browser.

### Option B — Python CLI

```bash
# Clone the repo
git clone https://github.com/Saksham653/web-crawlr.git
cd web-crawlr

# Run the scraper (zero pip installs — stdlib only)
python scraper.py https://example.com

# Output saved to output/result.json
# Open frontend/index.html → auto-loads all results
```

Optional args:
```bash
python scraper.py https://example.com -o my-output.json
```

---

## 🗂 Project Structure

```
web-crawlr/
├── scraper.py          ← Python CLI scraper (zero dependencies)
├── frontend/
│   └── index.html      ← Full dashboard UI (8 tabs, search, export)
├── output/
│   └── result.json     ← Generated after running scraper.py
└── README.md
```

---

## 🛠 Tech Stack

Built deliberately minimal — no npm, no frameworks, no build step.

| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | Vanilla HTML + CSS + JS | Zero npm packages, zero build step |
| Typography | Syne · Lora · Fira Code | Google Fonts |
| Python Scraper | Python 3.8+ stdlib | `urllib`, `html.parser`, `json`, `re` |
| CORS Proxies | allorigins · corsproxy · codetabs | Auto-fallback chain |
| Data Storage | `localStorage` + JSON on disk | No servers, no accounts |
| Export Engine | Blob + `URL.createObjectURL` | Native browser APIs only |
| Inspiration | Scrapy 2.14 | Spider → Item → Pipeline philosophy |

---

## ✅ Works Great On

- **Wikipedia** — full articles, all headings, all links
- **GitHub** — repo pages, README content, file listings
- **Hacker News** — posts, titles, comment links
- **News sites** — BBC, Reuters, The Hindu, NDTV
- **Blogs & documentation** — any server-rendered HTML
- **books.toscrape.com** — the classic scraping practice site
- **Static e-commerce** — prices, images, product descriptions

## ⚠️ Known Limitations

- **Flipkart / Amazon India** — Cloudflare blocks all public proxies
- **React / Vue / Angular SPAs** — JS-rendered pages return an empty HTML shell
- **Login-gated content** — requires an authenticated session
- **PDFs & image files** — no document or OCR support
- **Cloudflare-protected sites** — requires a headless browser (Playwright / Puppeteer)

---

## 🕸 How It Works

```
  URL Input
      │
      ▼
  ┌─────────────────────────────────┐
  │   CORS Proxy Fallback Chain     │
  │   allorigins → corsproxy        │
  │              → codetabs         │
  │   (each: 10s AbortSignal)       │
  └─────────────┬───────────────────┘
                │
                ▼
  ┌─────────────────────────────────┐
  │   UniversalParser               │
  │   HTMLParser (stdlib)           │
  │   → Headings  → Paragraphs      │
  │   → Links     → Images          │
  │   → Prices    → Meta            │
  └─────────────┬───────────────────┘
                │
                ▼
  ┌─────────────────────────────────┐
  │   Dashboard (8 tabs)            │
  │   Live search · Stats strip     │
  │   Price tracker · Export        │
  └─────────────────────────────────┘
```

---

## 👤 Author

<div align="center">

**Saksham Srivastava**

*Web scraping · Python · Vanilla frontend*

Built Crawlr as a full-stack web scraping project using Python and vanilla web technologies — designed around the Scrapy framework's philosophy of clean data extraction, structured pipelines, and portable output formats. Every line of code, every design decision, and every feature was built from scratch.

[![GitHub](https://img.shields.io/badge/GitHub-Saksham653-72bba0?style=flat-square&logo=github&logoColor=white&labelColor=0d0d0d)](https://github.com/Saksham653)
[![Email](https://img.shields.io/badge/Email-sakshamsrivastava7000%40gmail.com-c8a050?style=flat-square&logo=gmail&logoColor=white&labelColor=0d0d0d)](mailto:sakshamsrivastava7000@gmail.com)
[![Live App](https://img.shields.io/badge/App-saksham653.github.io%2Fweb--crawlr-3f8066?style=flat-square&labelColor=0d0d0d)](https://saksham653.github.io/web-crawlr/)

</div>

---

<div align="center">

© 2025 Saksham Srivastava &nbsp;·&nbsp; Crawlr v2 — Universal Web Scraper

*Zero dependencies. Start to finish.*

</div>
