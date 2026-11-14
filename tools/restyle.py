"""Restyle NYC Security Guides pages to match abstractenterprisessecuritysystems.com.
Keeps every guide's own text, JSON-LD, links and HUBNAV untouched; only swaps the CSS and the page shell
(header, hero with lead form, section wrapper, footer, sticky call bar). Idempotent: skips pages already restyled.
usage: python3 restyle.py <repo_dir> [files...]
"""
import re, sys, os, glob, html

MARK = '<!--AESS-SHELL v1-->'
PHONE = '(800) 486-0943'
TEL = 'tel:+18004860943'
SITE = 'https://www.abstractenterprisessecuritysystems.com'

CSS = r""":root{--ink:#0c1320;--ink2:#2a3550;--brand:#0d4d92;--brand2:#0a6cb5;--accent:#ffb400;--bg:#f5f7fb;--white:#fff;--line:#e3e9f1;--good:#1d8649;--bad:#b8323a}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:var(--ink);line-height:1.65;background:var(--bg);padding-bottom:72px}
.wrap{max-width:1180px;margin:0 auto;padding:0 18px}
header.top{background:linear-gradient(135deg,#0a2d5a 0%,#0d4d92 100%);color:#fff;padding:14px 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,.15)}
.nav{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:#fff;font-weight:800;font-size:1.05rem;letter-spacing:.2px}
.logo img{border-radius:8px;background:#fff;padding:3px}
.logo span span{color:var(--accent)}
.nav-cta{background:var(--accent);color:#000;padding:9px 16px;border-radius:8px;font-weight:800;text-decoration:none;font-size:.95rem;white-space:nowrap}
.nav-cta:hover{background:#ffc733}
.hero{background:linear-gradient(rgba(10,45,90,.94),rgba(13,77,146,.96));color:#fff;padding:38px 0 38px}
.hero h1{font-size:2.2rem;font-weight:800;line-height:1.18;margin-bottom:12px;color:#fff}
.hero .sub{font-size:1.08rem;opacity:.95;margin-bottom:18px;max-width:760px}
.hero .sub a,.by a{color:#ffd66b}
.hero-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:30px;align-items:start}
@media(max-width:820px){.hero h1{font-size:1.65rem}.hero-grid{grid-template-columns:1fr}}
nav.crumbs{font-size:.85rem;margin-bottom:10px;opacity:.9}
nav.crumbs a{color:#cfe0f5}
.by{font-size:.88rem;opacity:.85;margin-bottom:14px}
.hero-cta{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.btn{display:inline-block;padding:13px 22px;border-radius:9px;font-weight:800;text-decoration:none;font-size:1rem;border:0;cursor:pointer;transition:all .18s;font-family:inherit}
.btn-primary{background:var(--accent);color:#000!important}
.btn-primary:hover{background:#ffc733;transform:translateY(-1px)}
.btn-ghost{background:transparent;color:#fff!important;border:2px solid #fff}
.btn-ghost:hover{background:#fff;color:var(--ink)!important}
.trust-bullets{display:flex;flex-direction:column;gap:7px;font-size:.95rem;opacity:.95}
.trust-bullets li{list-style:none;padding-left:24px;position:relative}
.trust-bullets li::before{content:"✓";position:absolute;left:0;color:var(--accent);font-weight:900}
.lead-form{background:#fff;color:var(--ink);padding:22px;border-radius:14px;box-shadow:0 12px 40px rgba(0,0,0,.25)}
.lead-form h3{font-size:1.15rem;margin:0 0 10px;color:var(--brand)}
.lead-form input,.lead-form select,.lead-form textarea{width:100%;padding:11px;border:1.5px solid var(--line);border-radius:7px;margin-bottom:10px;font-size:.95rem;font-family:inherit;background:#fff;color:var(--ink)}
.lead-form input:focus,.lead-form select:focus,.lead-form textarea:focus{outline:0;border-color:var(--brand2)}
.lead-form .btn{width:100%;font-size:1.05rem}
.lead-form .hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.lead-form .note{font-size:.8rem;color:#6e7894;margin-top:8px}
.sent{background:#e9f7ef;border:1.5px solid var(--good);color:#14532d;padding:12px;border-radius:8px;margin-bottom:10px;font-weight:700;display:none}
.section{padding:42px 0;background:#fff}
.article{max-width:880px}
.article h2{font-size:1.75rem;color:var(--brand);font-weight:800;margin:34px 0 10px;line-height:1.25}
.article h3{font-size:1.2rem;color:var(--ink);font-weight:700;margin:20px 0 8px}
.article p{margin-bottom:12px}
.article ul,.article ol{margin:8px 0 14px 22px}
.article li{margin-bottom:5px}
.article a{color:var(--brand2)}
.article table{width:100%;border-collapse:collapse;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.05);margin:14px 0;font-size:.94rem}
.article th,.article td{padding:11px 14px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
.article th{background:var(--brand);color:#fff;font-weight:700}
.article tr:nth-child(even) td{background:#f9fbfd}
.tablewrap{overflow-x:auto}
.cta{background:linear-gradient(135deg,var(--brand) 0%,var(--brand2) 100%);color:#fff;padding:28px 24px;margin:32px 0;border-radius:12px;text-align:center}
.cta h2{color:#fff;font-size:1.5rem;margin:0 0 10px}
.cta p{color:#fff}
.cta a{color:#fff;font-weight:700}
.cta a.btn{background:var(--accent);color:#000!important;margin:8px 5px 0;text-decoration:none}
.cta a.btn:hover{background:#ffc733}
.related{background:#f5f7fb;border:1px solid var(--line);border-radius:12px;padding:18px 22px;margin-top:26px}
.related h2{font-size:1.3rem!important;margin-top:0!important}
.related h3{font-size:1.05rem;color:var(--brand)}
.silo-footer{background:#0a2d5a;color:#fff;padding:34px 0}
.silo-footer h4{color:var(--accent);margin-bottom:10px;font-size:1rem;text-transform:uppercase;letter-spacing:.5px}
.silo-footer p{color:#cfd9e8;font-size:.93rem;margin-bottom:8px}
.silo-footer a{color:#cfd9e8}
.silo-footer a:hover{color:var(--accent)}
footer.bottom{background:#06182f;color:#9fb1c8;padding:22px 0;text-align:center;font-size:.85rem}
footer.bottom a{color:#d4e1f0}
.photo{margin:24px 0}
.photo img{display:block;width:100%;height:auto;max-height:460px;object-fit:cover;border-radius:12px;box-shadow:0 4px 16px rgba(0,0,0,.08)}
.photo figcaption{font-size:.82rem;color:#6e7894;margin-top:6px}
.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:linear-gradient(90deg,var(--brand) 0%,var(--brand2) 100%);padding:11px 14px;display:flex;justify-content:space-around;align-items:center;box-shadow:0 -4px 18px rgba(0,0,0,.2);z-index:90;gap:8px}
.sticky-bar a{color:#fff;text-decoration:none;font-weight:800;font-size:.94rem;background:rgba(255,255,255,.13);padding:8px 14px;border-radius:7px;text-align:center;flex:1}
.sticky-bar a.primary{background:var(--accent);color:#000}
@media(max-width:560px){.sticky-bar a{font-size:.82rem;padding:7px 9px}.nav-cta{padding:8px 11px;font-size:.88rem}.logo{font-size:.92rem}}
"""

REGIONS = {
    'nyc': ('New York City', ['Manhattan', 'Brooklyn', 'Queens', 'The Bronx', 'Staten Island']),
    'long-island': ('Long Island', ['Nassau County', 'Western Suffolk', 'Central Suffolk', 'Eastern Suffolk / Hamptons']),
    'hudson-valley': ('Hudson Valley', ['Westchester County', 'Rockland County', 'Orange County', 'Putnam County', 'Dutchess County', 'Ulster County', 'Other Hudson Valley']),
}
ALL_AREAS = ['Manhattan', 'Brooklyn', 'Queens', 'The Bronx', 'Staten Island', 'Nassau County', 'Suffolk County', 'Westchester County', 'Rockland County', 'Orange County', 'Putnam County', 'Dutchess County', 'Ulster County']
CAMERA_WORDS = ('camera', 'nvr', 'dvr', 'dmss', 'smart-pss', 'hik-connect', 'guarding-vision', 'super-live', 'surveillance')


def region_of(slug):
    if 'long-island' in slug:
        return 'long-island'
    if 'hudson-valley' in slug:
        return 'hudson-valley'
    if slug.endswith('-nyc') or '-nyc-' in slug:
        return 'nyc'
    return None


def header():
    return (f'<header class="top"><div class="wrap nav">'
            f'<a href="{SITE}/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=nyc-security-guides&amp;utm_content=header" class="logo" aria-label="Abstract Enterprises Security Systems">'
            f'<img src="{SITE}/images/logo.png" alt="Abstract Enterprises Security Systems logo" width="42" height="42">'
            f'<span>Abstract Enterprises <span>Security Systems</span></span></a>'
            f'<a href="{TEL}" class="nav-cta">&#128222; {PHONE}</a></div></header>')


def lead_form(slug, phrase, region):
    areas = REGIONS[region][1] if region else ALL_AREAS
    opts = ''.join(f'<option>{a}</option>' for a in areas)
    service = phrase
    for suf in [' NYC', ' Long Island', ' Hudson Valley']:
        if service.endswith(suf):
            service = service[: -len(suf)]
    rname = REGIONS[region][0] if region else 'NYC, Long Island & Hudson Valley'
    title = f'Get Your {html.escape(service)} Quote' if service and service != phrase else 'Get a Free Quote'
    if not slug:
        title = 'Get a Free Quote'
    hid = lambda n, v: f'<input type="hidden" name="{n}" value="{html.escape(v, quote=True)}">'
    return (
        '<div class="lead-form" id="quote">'
        f'<h3>{title}</h3>'
        '<div class="sent" id="sent">Thanks! Your request was sent. We\'ll call you shortly.</div>'
        f'<form action="{SITE}/api/contact" method="POST">'
        + hid('subject', f'{phrase} — Guide Lead (GitHub guides)')
        + hid('from_name', 'NYC Security Guides')
        + hid('page', f'https://support677.github.io/nyc-security-guides/{slug + "/" if slug else ""}')
        + hid('page_slug', slug or 'guides-index')
        + hid('lead_service', service or 'General')
        + hid('lead_area', rname)
        + hid('lead_region', region or 'all')
        + hid('utm_source', 'github') + hid('utm_medium', 'referral')
        + hid('utm_campaign', slug or 'nyc-security-guides') + hid('utm_content', 'nyc-security-guides-form')
        + '<label class="hp">Leave this empty <input type="text" name="botcheck" tabindex="-1" autocomplete="off"></label>'
        '<input type="text" name="name" placeholder="Your name" required autocomplete="name">'
        '<input type="tel" name="phone" placeholder="Phone number" required autocomplete="tel">'
        f'<select name="area" required><option value="">Area</option>{opts}</select>'
        '<select name="property" required><option value="">Property type</option><option>House / brownstone</option>'
        '<option>2–6 unit building</option><option>Apartment building / co-op / condo</option>'
        '<option>Business / office / retail</option><option>School / church / nonprofit</option><option>Other</option></select>'
        '<textarea name="message" rows="2" placeholder="What do you need? (optional)"></textarea>'
        '<button type="submit" class="btn btn-primary">Get My Quote &rarr;</button>'
        f'<p class="note">Or call/text <a href="{TEL}">{PHONE}</a></p>'
        '</form></div>')


def footer(slug):
    return (
        '<section class="silo-footer"><div class="wrap">'
        '<h4>Abstract Enterprises Security Systems</h4>'
        '<p>Licensed NYS low-voltage contractor, in security since 2000. Security cameras, intercoms, door buzzers, access control, alarms and network cabling across the five NYC boroughs, Long Island and the Hudson Valley.</p>'
        f'<p><a href="{SITE}/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=nyc-security-guides&amp;utm_content=footer">abstractenterprisessecuritysystems.com</a> · <a href="{TEL}">{PHONE}</a> · '
        f'<a href="{"../" if slug else "./"}">All NYC security guides</a></p>'
        '</div></section>'
        '<footer class="bottom"><div class="wrap">'
        f'<p>© 2026 Abstract Enterprises Security Systems · <a href="{TEL}">{PHONE}</a> · <a href="{SITE}/privacy-policy">Privacy</a></p>'
        '</div></footer>'
        '<div class="sticky-bar">'
        f'<a href="{TEL}" class="primary">&#128222; Call Now</a>'
        '<a href="sms:8004860943">&#128172; Text</a>'
        '<a href="#quote">&#9889; Quote</a>'
        '</div>'
        '<script>try{if(/[?&]sent=1/.test(location.search)){var s=document.getElementById("sent");if(s){s.style.display="block";s.scrollIntoView({block:"center"});}}}catch(e){}</script>')


TRUST = ('<ul class="trust-bullets"><li>Licensed NYS low-voltage contractor</li>'
         '<li>In security since 2000</li>'
         '<li>NYC, Long Island &amp; Hudson Valley</li></ul>')


def head_fix(h):
    h = re.sub(r'<style>.*?</style>', '<style>\n' + CSS + '</style>', h, count=1, flags=re.S)
    if 'name="referrer"' not in h:
        h = h.replace('<meta name="viewport"', '<meta name="referrer" content="no-referrer-when-downgrade">\n<meta name="viewport"', 1)
    return h


def restyle_guide(h, slug):
    if MARK in h:
        return None
    h = head_fix(h)
    m = re.search(r'(<body>\s*<noscript>.*?</noscript>)\s*<div class="wrap">\s*(.*)</div>\s*</body>\s*</html>\s*$', h, re.S)
    assert m, slug
    pre, inner = m.group(1), m.group(2)
    crumbs = re.search(r'<nav class="crumbs">.*?</nav>', inner, re.S).group(0)
    h1 = re.search(r'<h1>(.*?)</h1>', inner, re.S)
    by = re.search(r'<p class="by">.*?</p>', inner, re.S).group(0)
    rest = inner[by and inner.index(by) + len(by):]
    rest = re.sub(r'\s*<footer>.*?</footer>\s*$', '', rest, flags=re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    title = re.sub(r'<[^>]+>', '', h1.group(1))
    phrase = title.split(':')[0].strip()
    region = region_of(slug)
    hero = (
        '<section class="hero"><div class="wrap"><div class="hero-grid"><div>'
        f'{crumbs}<h1>{h1.group(1)}</h1>{by}'
        f'<p class="sub">{desc}</p>'
        '<div class="hero-cta">'
        f'<a href="{TEL}" class="btn btn-primary">&#128222; Call {PHONE}</a>'
        '<a href="#quote" class="btn btn-ghost">&#9889; Free Quote</a></div>'
        f'{TRUST}</div>{lead_form(slug, phrase, region)}</div></div></section>')
    body = (f'{pre}\n{MARK}\n{header()}\n{hero}\n'
            f'<main class="section"><div class="wrap"><article class="article">\n{rest.strip()}\n</article></div></main>\n'
            f'{footer(slug)}\n</body>\n</html>\n')
    return h[:m.start()] + body


def restyle_index(h):
    if MARK in h:
        return None
    h = head_fix(h)
    m = re.search(r'(<body>\s*<noscript>.*?</noscript>)\s*<div class="wrap">\s*(.*)</div>\s*</body>\s*</html>\s*$', h, re.S)
    assert m, 'index'
    pre, inner = m.group(1), m.group(2)
    h1 = re.search(r'<h1>(.*?)</h1>', inner, re.S)
    by = re.search(r'<p class="by">(.*?)</p>', inner, re.S)
    rest = inner[inner.index(by.group(0)) + len(by.group(0)):]
    rest = re.sub(r'\s*<footer>.*?</footer>\s*$', '', rest, flags=re.S)
    hero = (
        '<section class="hero"><div class="wrap"><div class="hero-grid"><div>'
        f'<h1>{h1.group(1)}</h1><p class="sub">{by.group(1)}</p>'
        '<div class="hero-cta">'
        f'<a href="{TEL}" class="btn btn-primary">&#128222; Call {PHONE}</a>'
        '<a href="#quote" class="btn btn-ghost">&#9889; Free Quote</a></div>'
        f'{TRUST}</div>{lead_form("", "NYC Security Guides", None)}</div></div></section>')
    body = (f'{pre}\n{MARK}\n{header()}\n{hero}\n'
            f'<main class="section"><div class="wrap"><article class="article">\n{rest.strip()}\n</article></div></main>\n'
            f'{footer("")}\n</body>\n</html>\n')
    return h[:m.start()] + body


if __name__ == '__main__':
    repo = sys.argv[1]
    files = sys.argv[2:] or sorted(glob.glob(os.path.join(repo, '*/index.html'))) + [os.path.join(repo, 'index.html')]
    changed = []
    for f in files:
        h = open(f, encoding='utf-8').read()
        if os.path.abspath(f) == os.path.abspath(os.path.join(repo, 'index.html')):
            out = restyle_index(h)
        else:
            out = restyle_guide(h, os.path.basename(os.path.dirname(f)))
        if out:
            open(f, 'w', encoding='utf-8').write(out)
            changed.append(f)
    print(len(changed), 'restyled')
