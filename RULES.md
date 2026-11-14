# NYC Security Guides — build rules (read fully before every run)

Owner: Anwar Timothy, Abstract Enterprises Security Systems, licensed NYS low-voltage contractor, in security since 2000.
BUSINESS NAME RULE: in anything published (titles, headings, body, meta, schema, FAQs, alt text, link text) always write the full name "Abstract Enterprises Security Systems". NEVER write the abbreviation "AESS" — it is not the brand and nobody searches for it.
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
- Open the matching Abstract Enterprises Security Systems page (https://www.abstractenterprisessecuritysystems.com/<slug>) with Firecrawl. Take ONLY facts from it: services, what's included, area price (if the page shows one), warranty, hours. Never invent a price; if the page has no price, say pricing is on the page and link it.
- Firecrawl search the exact phrase plus variants ("<service> <area> cost", "<service> <area> reddit", "<area> <service> landlord/co-op/permit") and read 2–4 real results: People Also Ask style questions, Reddit threads, local rules. FAQs come from those real questions.
- Local specifics for the area: housing/building stock (brownstones, co-ops, pre-war walk-ups, garden apartments, strip malls, big-lot homes), who usually approves the work (landlord, co-op board, HOA), weather/exposure, noise-hour rules for that city/town, parking/access issues. Only what you can support; no made-up statistics.

## 3. The page (each one genuinely different)
- File: `<slug>/index.html`, self-contained HTML (copy the `<head>` tags block and CSS from `_template.html`).
- `<title>` and H1 START with the exact phrase in title case: e.g. "Security Camera Installation Brooklyn: …". Meta description starts with the same phrase, ≤155 chars.
- First sentence starts with the exact phrase.
- 900–1,500 words. Angle and section order vary by service and area — do not reuse the same outline every time. Mix from: cost & what drives it, building/landlord rules, a comparison table (e.g. wired vs Wi-Fi, repair vs replace, audio vs video intercom), a step-by-step "what happens on install day", a checklist "questions to ask any installer", common problems in that building type, a short local scenario (no customer names/addresses).
- NEVER copy sentences from the Abstract Enterprises Security Systems page or another guide: no run of 8+ identical words. Write fresh.
- UNIQUE CONTENT, NO WORD-SWAPPING (Anwar, Nov 14 2026 — hard rule): every guide is written from scratch for its own service and its own area. Never take an existing guide (or the website page) and swap the area, brand or service names, synonyms or numbers. Two guides for the same service in different areas, or two brands in the same area, must differ in angle, H2 outline, tables, examples, FAQs and local detail — not just in nouns. A Long Island guide talks only about Long Island (its housing, towns, rules, weather); a Hudson Valley guide only about the Hudson Valley; a brand guide only about that brand's real products, apps and quirks.
- UNIQUENESS GATE before publishing (run it in the workbench, every guide, every run): strip HUBNAV, breadcrumb, byline, CTA box and footer, then compare the body text against (a) the matching website page and (b) every existing guide of the same service AND every existing guide in the same area. FAIL if any run of 8+ identical words is shared, or if the H2 outline matches another guide's in the same order. Also FAIL if the guide still makes sense after replacing its area/brand name with another one — rewrite it with real local or brand-specific substance. A failed guide is rewritten, not published.
- 4–6 FAQs from the real questions found; FAQPage JSON-LD matching the visible FAQs; also Article + BreadcrumbList JSON-LD; `<link rel="canonical">` = the guide's own URL.
- Links (plain followed `<a>`, no nofollow):
  - The matching Abstract Enterprises Security Systems page, with anchor = the exact phrase, at least twice (intro + CTA): `https://www.abstractenterprisessecuritysystems.com/<slug>?utm_source=github&utm_medium=referral&utm_campaign=<slug>&utm_content=nyc-security-guides`
  - Parent guide (neighborhood → borough/county guide → hub guide) if it exists in this repo (also covered by the HUBNAV block, section 4); 2 related guides that exist (same area other service, or same service nearby area).
  - The storage calculator https://support677.github.io/security-camera-storage-calculator/ on camera topics.
  - Back to the guides index `../`.
- CTA box: "Get a price" → the Abstract Enterprises Security Systems page; toll-free (800) 486-0943.
- Byline: "By Abstract Enterprises Security Systems — licensed NYS low-voltage contractor, in security since 2000." Date = today.
- Never: fake reviews/testimonials, customer names or addresses, license numbers, competitor bashing, prices not on the Abstract Enterprises Security Systems site, AI-sounding filler ("in today's fast-paced world").
- Do not mention the Abstract Enterprises Security Systems warranty/cancellation terms beyond what the Abstract Enterprises Security Systems page itself says.

## 4. Publish (one commit per run)
The guides site is structured EXACTLY like the Abstract Enterprises Security Systems website: region hub → borough/county → neighborhood/town, one guide per website page, same slug.
Regions: `nyc` (New York City), `long-island`, `hudson-valley`. Parent of a borough/county guide = the same service's hub guide in its region; parent of a neighborhood/town guide = the same service's borough/county guide (or the hub if that guide doesn't exist yet).
In ONE `GITHUB_COMMIT_MULTIPLE_FILES` (Composio, account support677, repo nyc-security-guides, branch main):
- the new `<slug>/index.html` files. Each new guide ends (right before `<footer>`) with a `<!--HUBNAV:START-->…<!--HUBNAV:END-->` block, same layout as the existing guides: "<Service Area> by area" heading with an empty `<!--CHILDREN:START--><!--CHILDREN:END-->` list (child guides go there), "<Service> in other regions" (same service, other hub guides), and "More <Region> guides" (every other guide in the same region/area). Use the existing guides' HUBNAV block as the template.
- every PARENT guide of a new guide (and its hub if different): add `<li><a href="../<child-slug>/"><Short title></a></li>` inside its `<!--CHILDREN:START-->…<!--CHILDREN:END-->` (wrap the items in `<ul>`, replace the "added here as they are published" placeholder line, keep alphabetical). Also add the new guide to the "More <Region> guides" list of every guide in the same area.
- `index.html`: a hub guide goes in its region section `<!--REGION:<region>:START-->…<!--REGION:<region>:END-->` as `<li><a href="<slug>/">Title</a> <span>· YYYY-MM-DD</span>` + `<!--CHILDREN:<slug>:START--><!--CHILDREN:<slug>:END--></li>`, alphabetical by title, and update that region's count in its `<h3>`. A borough/county/neighborhood guide goes as a nested `<ul><li>` inside its hub's `<!--CHILDREN:<hub-slug>:START-->…END-->` markers on the index (neighborhoods nested under their borough). Update the total in `<span id="count">`.
- `sitemap.xml`: add `<url><loc>https://support677.github.io/nyc-security-guides/<slug>/</loc><lastmod>YYYY-MM-DD</lastmod></url>` per guide before `</urlset>`.
- `LOG.md`: one line per guide: `YYYY-MM-DD | <slug> | <title> | <url> | <words> words`.
Read the current files from the repo first and send full updated contents. Every guide still links to its EXACT matching page on abstractenterprisessecuritysystems.com (same slug), as in section 3.

## 5. After publishing
- Verify each new URL with Firecrawl (GitHub Pages can take 1–3 min; retry once after a wait). Report any that 404.
- Append each new guide URL to `INDEXING.md` as `YYYY-MM-DD | <url> | QUEUED` (the Chrome indexing task works that queue).
- Append the new guide URLs to `DISTRIBUTE.md` (date | phrase | guide url | Abstract Enterprises Security Systems page) — the LinkedIn and social posting tasks pick links from there.
- Do NOT submit the sitemap by API: the Search Console property is owned by support@abstractenterprisessecuritysystems.com (not the openeyesales Composio connection). The sitemap was submitted once in the UI; Google re-reads it on its own.

GSC_VERIFIED: yes (Nov 7 2026)
GSC_ACCOUNT: support@abstractenterprisessecuritysystems.com — kept separate from openeyesales (main Abstract Enterprises Security Systems site) so the guides get their own daily "Request indexing" allowance
GSC_PROPERTY: https://support677.github.io/nyc-security-guides/
