"""Shared layout for the Jetline site generator: head, header + dropdown menus, contact block, footer."""

SITE = "https://www.jetline-training.com"  # original site (booking shop, member area, blog)

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-chev" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4l4 4 4-4"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.3 8-8 9-4.7-1-8-4.5-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></symbol>
<symbol id="i-user" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.7 5.7 6.3.8-4.6 4.3 1.2 6.2L12 17l-5.6 3 1.2-6.2L3 9.5l6.3-.8L12 3z"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.2 7-11.5A7 7 0 005 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
<symbol id="i-plane" viewBox="0 0 24 24" fill="currentColor"><path d="M21 15.5v-1.7l-8-5V3.5a1.5 1.5 0 00-3 0v5.3l-8 5v1.7l8-2.5v4.3l-2 1.5V21l3.5-1 3.5 1v-1.7l-2-1.5V13l8 2.5z"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M3.5 7.5l8.5 6 8.5-6"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/></symbol>
<symbol id="i-land" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><path d="M4 7l16 6-3 1.5L9 12 6 13.5 4 7z"/></symbol>
<symbol id="i-book" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 012-2h13v16H6a2 2 0 00-2 2V5z"/><path d="M4 19a2 2 0 012-2h13"/></symbol>
<symbol id="i-brief" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="18" height="13" rx="3"/><path d="M9 7V5a2 2 0 012-2h2a2 2 0 012 2v2M3 13h18"/></symbol>
<symbol id="i-spark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8L12 3zM19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8L19 16z"/></symbol>
</defs></svg>"""

# (label, page, [(title, small, anchor-or-url)])
NAV = [
    ("Type Ratings", "type-ratings.html", [
        ("A320 Type Rating", "Course, requirements, validity", "#a320"),
        ("Packages & Pricing", "Silver and Gold", "#packages"),
        ("Base Training", "A320 & B737 landings", "#base"),
        ("LPC & Revalidation", "Keep your rating current", "#lpc"),
        ("MCC / JOC", "Multi-crew on the A320", "#mcc"),
        ("SFI & TRI Instructor", "A320 | B737", "#instructor"),
        ("TRI/SFI Refresher", "Online, for revalidation", "#refresher"),
        ("MCF & Demo Pilot", "Maintenance check flights", "#mcf"),
    ]),
    ("Airline Academy", "academy.html", [
        ("0 to ATPL, Ab-initio", "PPL to frozen ATPL", "#ab-initio"),
        ("Airline Pilot Program", "Four steps, pay as you go", "#program"),
        ("Modular vs Integrated", "Why modular", "#modular"),
        ("How to Become a Pilot", "The EASA roadmap", "#how-to"),
        ("ICAO to EASA", "Licence conversion", "#icao"),
    ]),
    ("Careers", "careers.html", [
        ("Line Training Pathway", "300 / 500 hour building", "#pathway"),
        ("First-Officer Careers", "Airlines that hire", "#first-officer"),
        ("Graduates", "Alumni working as pilots", "#graduates"),
        ("Student Stories", "Line intro blog", "#stories"),
        ("Airline Application Portal", "Direct applications", "#portal"),
    ]),
    ("Assessment Prep", "prep.html", [
        ("Airline Assessment Prep", "Interview + simulator", "#aap"),
        ("A320 AI Tutor", "Maverick plans", "#maverick"),
        ("Online Courses", "Study at home", "#courses"),
        ("Other Bookings", "ELP, aUPRT, conversion support", "#shop"),
    ]),
    ("About", "about.html", [
        ("About Jetline", "Who we are", "#about"),
        ("The Team", "Instructors & management", "#team"),
        ("Locations", "ZRH · VIE · FRA · CDG", "#locations"),
        ("Approvals", "EASA ATO details", "#approvals"),
        ("Members & File Share", "Student login", "EXT:/members"),
        ("Terms & Privacy", "Legal", "EXT:/terms"),
    ]),
]


def href(page, target):
    if target.startswith("EXT:"):
        return SITE + target[4:]
    return page + target


def head(title, desc, home=False):
    splash_js = ""
    if home:
        splash_js = ("<script>try{if(!sessionStorage.getItem('jt-splash')&&!/[?&]skip/.test(location.search))"
                     "document.documentElement.classList.add('js-splash')}catch(e){document.documentElement.classList.add('js-splash')}</script>")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
<script>document.documentElement.classList.add('js')</script>
{splash_js}
</head>
<body>
{ICONS}
"""


def header(current):
    items = []
    for label, page, links in NAV:
        lis = "".join(
            f'<a href="{href(page, t)}"{" class=ext" if t.startswith("EXT:") else ""}><b>{ti}</b><small>{sm}</small></a>'
            for ti, sm, t in links
        )
        cur = ' aria-current="page"' if page == current else ""
        items.append(
            f'<li class="has-menu"><button class="top" aria-expanded="false"{cur}>{label}<svg><use href="#i-chev"/></svg></button>'
            f'<div class="menu">{lis}</div></li>'
        )
    return f"""<header class="site" id="top">
  <div class="wrap nav">
    <a class="brand" href="index.html?skip" aria-label="Jetline Training — home"><img src="assets/logo.svg" alt="Jetline Training" width="1955" height="1080"></a>
    <ul id="menu">
      {''.join(items)}
      <li><a class="btn btn-primary btn-sm" href="#contact">Contact us</a></li>
    </ul>
    <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</header>
"""


CONTACT = """<section class="sec tint" id="contact">
  <div class="wrap">
    <div class="cta-band reveal">
      <span class="eyebrow" style="color:#cfe0ff">Get in touch</span>
      <h2>Contact us for more information.</h2>
      <p>Tell us your licence and your goals. We reply with a personal offer.</p>
      <a class="btn btn-white" href="#message">Send us a message <svg><use href="#i-arrow"/></svg></a>
    </div>
    <div class="cgrid">
      <div class="panel reveal">
        <h3>Let’s talk.</h3>
        <ul class="cinfo">
          <li><div class="ic"><svg><use href="#i-mail"/></svg></div><div><small>Email</small><a href="mailto:info@jetline-training.com">info@jetline-training.com</a></div></li>
          <li><div class="ic"><svg><use href="#i-phone"/></svg></div><div><small>Phone</small><a href="tel:+41786855034">+41 78 685 50 34</a></div></li>
          <li><div class="ic"><svg><use href="#i-pin"/></svg></div><div><small>Headquarters</small><b>Jetline Training GmbH<br>Sinserstrasse 67, CH-6330 Cham, Switzerland</b></div></li>
        </ul>
        <div class="social">
          <a href="https://www.instagram.com/jetlinetraining/">Instagram</a>
          <a href="https://www.facebook.com/Jetline-Training-108712041266705">Facebook</a>
          <a href="https://www.youtube.com/@jetlinetraining">YouTube</a>
          <a href="https://www.trustpilot.com/review/www.jetline-training.com">Trustpilot</a>
        </div>
      </div>
      <div class="panel reveal d1" id="message">
        <h3>Tell us about your training request.</h3>
        <form id="contact-form" novalidate>
          <div class="row">
            <div class="f"><label for="fn">First name *</label><input id="fn" name="fn" autocomplete="given-name" required></div>
            <div class="f"><label for="ln">Last name *</label><input id="ln" name="ln" autocomplete="family-name" required></div>
          </div>
          <div class="row">
            <div class="f"><label for="em">Email *</label><input id="em" name="em" type="email" autocomplete="email" required></div>
            <div class="f"><label for="ph">Phone *</label><input id="ph" name="ph" type="tel" autocomplete="tel" required></div>
          </div>
          <div class="f"><label for="lic">Nationality + licence CAA</label><input id="lic" name="lic" placeholder="e.g. German, EASA CPL/IR"></div>
          <div class="f"><label for="msg">Your message *</label><textarea id="msg" name="msg" placeholder="Type your pilot training request here." required></textarea></div>
          <div style="position:absolute;left:-9999px;height:0;overflow:hidden" aria-hidden="true"><label for="website">Leave empty</label><input id="website" name="website" tabindex="-1" autocomplete="off"></div>
          <button class="btn btn-primary" type="submit" style="width:100%">Send message <svg><use href="#i-arrow"/></svg></button>
          <div class="form-msg" id="form-msg" role="status"></div>
        </form>
      </div>
    </div>
  </div>
</section>
"""


def footer():
    cols = []
    for label, page, links in NAV:
        lis = "".join(f'<li><a href="{href(page, t)}">{ti}</a></li>' for ti, sm, t in links[:6])
        cols.append(f'<div><h4><a href="{page}">{label}</a></h4><ul>{lis}</ul></div>')
    return f"""<footer class="site">
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img src="assets/logo.svg" alt="Jetline Training" width="1955" height="1080">
        <p><b style="color:var(--navy)">Type Rated. Line Checked. Flight Deck Ready.</b></p>
      </div>
      {''.join(cols)}
    </div>
    <div class="legal">
      © JETLINE TRAINING GmbH, Switzerland. All rights reserved. Swiss ATO approval CH.ATO.0310.
      <a href="{SITE}/terms" style="text-decoration:underline">Terms &amp; Conditions</a> ·
      <a href="{SITE}/privacy" style="text-decoration:underline">Privacy Policy</a><br>
      All information is for information only. Course content is as per the individual accepted offer and approved training manual. Not for real navigation or aircraft operation. National or EASA rules prevail. Prices shown are as published on jetline-training.com and may change: always refer to your personal offer.
      <div class="concept">Website redesign concept, built from the content and branding of jetline-training.com.</div>
    </div>
  </div>
  <div class="powered"><a href="https://viridiansuite.com" target="_blank" rel="noopener" aria-label="Empowered by Viridian Suite"><img src="assets/viridian.webp" width="168" height="65" alt="Empowered by Viridian"></a></div>
</footer>
<div class="mobile-cta"><a class="btn btn-primary" href="#contact">Contact us for more information <svg><use href="#i-arrow"/></svg></a></div>
<script src="assets/site.js"></script>
</body>
</html>
"""


def page(current, title, desc, main, home=False, splash=""):
    return head(title, desc, home) + splash + header(current) + "<main>\n" + main + "\n" + CONTACT + "</main>\n" + footer()


def phero(eyebrow, h1, lead, chips=""):
    return f"""<section class="phero"><div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <div class="chips">{chips}</div>
</div></section>
"""


def chips(page, items):
    return "".join(f'<a class="chip" href="{page}{a}">{t}</a>' for t, a in items)


def tick(text, bold=None):
    b = f"<b>{bold}</b> " if bold else ""
    return f'<li><svg><use href="#i-check"/></svg><div>{b}<span>{text}</span></div></li>'
