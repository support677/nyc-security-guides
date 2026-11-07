# NYC Security Guides — build rules (read fully before every run)

Owner: Anwar Timothy, Abstract Enterprises Security Systems (AESS), licensed NYS low-voltage contractor, in security since 2000.
Live site: https://support677.github.io/nyc-security-guides/  ·  Repo: support677/nyc-security-guides (branch main, GitHub Pages from root).
Purpose: parasite SEO + real backlinks. Each guide targets ONE exact "service × area" search phrase, mirrors one page on
abstractenterprisessecuritysystems.com, and links to it with a normal (followed) link.

## 1. The queue (same order as the website blueprint)
Source of truth = the website repo support677/abstract-enterprises-site: every `*.html` file in its root is a page; slug = filename without `.html`.
Skip slugs that contain `pricing`, end in `-prices`, or are not a service × area page (about-us, contact, index, blog, privacy, terms, 404, thank-you, etc.).
A slug is DONE when the folder `<slug>/index.html` already exists in this repo.
Pick the next undone slugs in this order:
1. Tier 1 hubs — slug ends `-nyc`, `-long-island`, `-hudson-valley`
2. Tier 2 boroughs/counties — ends `-brooklyn`, `-queens`, `-bronx`, `-manhattan`, `-staten-island`, or `-<name>-county`
3. Tier 3 neighborhoods/towns — everything else (e.g. `-park-slope-brooklyn-ny`)
Inside each tier, services in this priority, then alphabetical:
security-camera-installation, intercom-installation, intercom-repair, access-control-installation, security-camera-repair,
door-buzzer-repair, alarm-installation, commercial-security-camera-installation, apartment-intercom-system, mag-lock-installation,
doorbell-camera-installation, residential-security-camera-installation, tv-installation, cat6-installation, structured-cabling-installation,
fire-alarm-installation, then all others. Within one service, hub order = nyc, long-island, hudson-valley; boroughs = brooklyn, queens, bronx, manhattan, staten-island, then counties.
Interleave services (don't do 30 areas of one service in a row): take the next undone slug of each service in priority order, round-robin.

## 2. Research before writing (every guide)
- Open the matching AESS page (https://www.abstractenterprisessecuritysystems.com/<slug>) with Firecrawl. Take ONLY facts from it: services, what's included, area price (if the page shows one), warranty, hours. Never invent a price; if the page has no price, say pricing is on the page and link it.
- Firecrawl search the exact phrase plus variants ("<service> <area> cost", "<service> <area> reddit", "<area> <service> landlord/co-op/permit") and read 2–4 real results: People Also Ask style questions, Reddit threads, local rules. FAQs come from those real questions.
- Local specifics for the area: housing/building stock (brownstones, co-ops, pre-war walk-ups, garden apartments, strip malls, big-lot homes), who usually approves the work (landlord, co-op board, HOA), weather/exposure, noise-hour rules for that city/town, parking/access issues. Only what you can support; no made-up statistics.

## 3. The page (each one genuinely different)
- File: `<slug>/index.html`, self-contained HTML (copy the `<head>` tags block and CSS from `_template.html`).
- `<title>` and H1 START with the exact phrase in title case: e.g. "Security Camera Installation Brooklyn: …". Meta description starts with the same phrase, ≤155 chars.
- First sentence starts with the exact phrase.
- 900–1,500 words. Angle and section order vary by service and area — do not reuse the same outline every time. Mix from: cost & what drives it, building/landlord rules, a comparison table (e.g. wired vs Wi-Fi, repair vs replace, audio vs video intercom), a step-by-step "what happens on install day", a checklist "questions to ask any installer", common problems in that building type, a short local scenario (no customer names/addresses).
- NEVER copy sentences from the AESS page or another guide: no run of 8+ identical words. Write fresh.
- 4–6 FAQs from the real questions found; FAQPage JSON-LD matching the visible FAQs; also Article + BreadcrumbList JSON-LD; `<link rel="canonical">` = the guide's own URL.
- Links (plain followed `<a>`, no nofollow):
  - The matching AESS page, with anchor = the exact phrase, at least twice (intro + CTA): `https://www.abstractenterprisessecuritysystems.com/<slug>?utm_source=github&utm_medium=referral&utm_campaign=<slug>&utm_content=nyc-security-guides`
  - Parent guide (neighborhood → borough/county guide → hub guide) if it exists in this repo; 2 related guides that exist (same area other service, or same service nearby area).
  - The storage calculator https://support677.github.io/security-camera-storage-calculator/ on camera topics.
  - Back to the guides index `../`.
- CTA box: "Get a price" → the AESS page; toll-free (800) 486-0943.
- Byline: "By Abstract Enterprises Security Systems — licensed NYS low-voltage contractor, in security since 2000." Date = today.
- Never: fake reviews/testimonials, customer names or addresses, license numbers, competitor bashing, prices not on the AESS site, AI-sounding filler ("in today's fast-paced world").
- Do not mention the AESS warranty/cancellation terms beyond what the AESS page itself says.

## 4. Publish (one commit per run)
In ONE `GITHUB_COMMIT_MULTIPLE_FILES` (Composio, account support677, repo nyc-security-guides, branch main):
- the new `<slug>/index.html` files
- `index.html`: insert one `<li>` per new guide right after `<!--GUIDES:START-->` (newest first): `<li><a href="<slug>/">Title</a> <span>· YYYY-MM-DD</span></li>`; update the count in `<span id="count">`.
- `sitemap.xml`: add `<url><loc>https://support677.github.io/nyc-security-guides/<slug>/</loc><lastmod>YYYY-MM-DD</lastmod></url>` per guide before `</urlset>`.
- `LOG.md`: one line per guide: `YYYY-MM-DD | <slug> | <title> | <url> | <words> words`.
Read the current index.html/sitemap.xml/LOG.md from the repo first and send full updated contents.

## 5. After publishing
- Verify each new URL with Firecrawl (GitHub Pages can take 1–3 min; retry once after a wait). Report any that 404.
- If `GSC_VERIFIED: yes` below, submit the sitemap https://support677.github.io/nyc-security-guides/sitemap.xml with Composio Google Search Console (account under openeyesales@gmail.com).
- Append the new guide URLs to `DISTRIBUTE.md` (date | phrase | guide url | AESS page) — the LinkedIn and social posting tasks pick links from there.

GSC_VERIFIED: no
GSC_PROPERTY: https://support677.github.io/nyc-security-guides/
