from layout import page, phero, chips, SITE

P = "about.html"

TEAM = [("Adrian Gallati", "Founder & CEO", "A320 TRI / TRE, airline pilot and examiner with 20+ years in the industry. Accountable Manager and Head of Training."),
        ("Capt. V. Rister", "Chief Flight Instructor", "SFI A320. Responsible for theoretical training."),
        ("Pascal Lüde", "Compliance Monitoring Manager", "Experienced safety and compliance manager from airlines including Chair."),
        ("Ivan Tallarico", "A320 First Officer · Theory Instructor", "Flew ferry and demo missions around the globe after his rating."),
        ("Tiago Esteves", "A320 First Officer · Head of Sales", "Started flying right after his type rating and has close to 1,000 hours on the A320.")]

CENTERS = [
    ("Zürich", "ZRH · Headquarters", "Ten simulators, with A320 full-flight and fixed-base devices on site. Daylight briefing rooms and airline crew restaurant.", "Cherstrasse 1, 8152 Opfikon · Kloten, Zürich Airport"),
    ("Vienna", "VIE", "Twelve simulators incl. A320 FFS CEO and NEO. Daylight briefing rooms and cafeteria.", "Flughafen Wien, Austrian Airlines Base, Building 974, 1300 Schwechat"),
    ("Frankfurt", "FRA", "One of Europe’s largest centres: 20+ simulators, including six A320 CEO and NEO. Also upset recovery training.", "Flughafen Frankfurt, Airportring Tor 24, 60549 Frankfurt"),
    ("Paris", "CDG", "Six simulators, including two A320 CEO and NEO, at Paris CDG. Daylight rooms and crew rest areas.", "26 Av. de la Demi-Lune, Bâtiment Alizé, 95700 Roissy-en-France"),
]

MAIN = (
    phero("About Jetline", "Instructors and examiners. Worldwide.",
          "A group of experienced instructors and examiners specialised in type ratings, instructor training and initial experience support, mainly on the A320 and B737.",
          chips(P, [("About", "#about"), ("Team", "#team"), ("Locations", "#locations"), ("Approvals", "#approvals")]))
    + f"""
<section class="sec" id="about">
  <div class="wrap">
    <div class="grid g2" style="align-items:start">
      <div class="reveal">
        <span class="eyebrow">Mission &amp; Vision</span>
        <h2 style="font-size:clamp(1.8rem,3.6vw,2.8rem);margin:14px 0 16px">Passionate about forming airline pilots.</h2>
        <p class="lead">We take pilots from ab-initio to a frozen ATPL, through a type rating and on to airline selection, with the highest training standards.</p>
      </div>
      <div class="grid g2 reveal d1">
        <div class="card"><h3>Mission</h3><p>Dedicated, experienced instructors. Airline assessment preparation after the course. Simulators worldwide, to airline standard wherever it suits you.</p></div>
        <div class="card"><h3>Vision</h3><p>After-training support, job-search help and assessment consulting. Airline line training availability for every student. Affordable training for the next pilot generation.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec tint" id="team">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">The Team</span><h2>Who you train with.</h2></div>
    <div class="grid g3">{''.join(f'<div class="card lift reveal"><div class="ic"><svg><use href="#i-user"/></svg></div><h3>{n}</h3><p style="color:var(--blue-600);font-weight:700;font-size:.85rem;margin-bottom:8px">{r}</p><p>{d}</p></div>' for n, r, d in TEAM)}</div>
  </div>
</section>

<section class="sec" id="locations">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Locations</span><h2>Simulator centres across Europe.</h2>
      <p class="lead">Also: Munich, Essen, Berlin, Madrid, Barcelona, Sofia and Lisbon. MCC is offered in Zürich, Vienna, Prague and Budapest.</p></div>
    <div class="grid g2">{''.join(f'<div class="card lift reveal"><span class="tag">{c}</span><h3 style="margin-top:12px">{n}</h3><p>{d}</p><p class="small" style="margin-top:12px">{a}</p></div>' for n, c, d, a in CENTERS)}</div>
    <div class="split block">
      <div class="media reveal"><img src="assets/zurich-airport.jpg" alt="Zürich airport at sunset" width="1400" height="1050" loading="lazy"></div>
      <div class="copy reveal d1"><span class="eyebrow">Headquarters</span><h3>Jetline Training GmbH</h3><p class="lead">Sinserstrasse 67, CH-6330 Cham, Switzerland. German administration office: Bad Homburg.</p></div>
    </div>
  </div>
</section>

<section class="sec tint" id="approvals">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Approvals</span><h2>EASA approved. Swiss supervised.</h2>
      <p class="lead">Jetline Training is an EASA ATO under the oversight of Swiss FOCA. ATO and FSTD certificates are available in the school’s file share.</p></div>
    <div class="grid g3">
      <div class="card reveal"><span class="tag">CH.ATO.0310</span><h3 style="margin-top:12px">Switzerland</h3><p>MCC, type ratings and airline pilot instructor courses.</p></div>
      <div class="card reveal d1"><span class="tag">CZ-ATO-043</span><h3 style="margin-top:12px">Czech Republic</h3><p>Ab-initio to CPL, ME-IR frozen ATPL, aUPRT and MCC.</p></div>
      <div class="card reveal d2"><span class="tag">PL-ATO-032</span><h3 style="margin-top:12px">Poland</h3><p>Ab-initio to CPL, ME-IR frozen ATPL and aUPRT.</p></div>
    </div>
    <p class="small reveal" style="margin-top:18px">Advanced programmes on request: AWO, LVO, wet drill, RVSM and demo pilot courses.</p>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/file-share">File share (students) <svg><use href="#i-arrow"/></svg></a><a class="btn btn-ghost" href="{SITE}/members">Member login</a></div>
  </div>
</section>
"""
)


def build():
    return page(P, "About — Jetline Training",
                "About Jetline Training: mission, team, simulator centres in Zürich, Vienna, Frankfurt and Paris, and EASA ATO approvals.", MAIN)
