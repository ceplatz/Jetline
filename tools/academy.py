from layout import page, phero, chips, tick, SITE

P = "academy.html"

MAIN = (
    phero("Airline Academy", "0 to ATPL. Modular and flexible.",
          "No licence yet? Train from private pilot to frozen ATPL and A320 type rating, step by step, with no contract for the whole programme upfront.",
          chips(P, [("Ab-initio", "#ab-initio"), ("Airline Pilot Program", "#program"), ("Modular vs integrated", "#modular"),
                    ("How to become a pilot", "#how-to"), ("ICAO to EASA", "#icao")]))
    + f"""
<section class="sec" id="ab-initio">
  <div class="wrap">
    <div class="split">
      <div class="copy reveal">
        <span class="eyebrow">0 to ATPL · Ab-initio</span>
        <h2>From first flight to the airline flight deck.</h2>
        <p class="lead">Our Airline Academy covers PPL, instrument rating, CPL with ME-IR and your A320 type rating, with airline placement through the Jetline partner network.</p>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><div><b>25+ hiring airlines</b> <span>to apply to as first officer after CPL and A320 type rating.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>No EU passport needed.</b> <span>We support your visa.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>Airline interview guarantee</b> <span>within 1 year of your passed A320 skill test, after the modular ATPL programme.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>From EUR 89,995</b> <span>for the package covering PPL, IR, CPL, integrated MCC and A320 type rating.</span></div></li>
        </ul>
        <div class="row-btns"><a class="btn btn-primary" href="#contact">Ask for a quote <svg><use href="#i-arrow"/></svg></a></div>
      </div>
      <div class="media reveal d1"><img src="assets/academy-tecnam.jpg" alt="Cadet pilot beside a Tecnam training aircraft" width="1400" height="933" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="sec tint" id="program">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Airline Pilot Program</span><h2>Four steps to the flight deck.</h2>
      <p class="lead">Join or pause at any time and pay step by step. Optional flight instructor (FI) rating on top.</p></div>
    <div class="grid g4">
      <div class="step reveal"><div class="n">01</div><h3>PPL</h3><p>Basic flying on a small single-engine aircraft under VFR.</p></div>
      <div class="step reveal d1"><div class="n">02</div><h3>ATPL theory</h3><p>The 14 EASA theory subjects, examined at an EASA exam centre.</p></div>
      <div class="step reveal d2"><div class="n">03</div><h3>Instrument rating</h3><p>Fly by reference to instruments alone under IFR.</p></div>
      <div class="step hot reveal d3"><div class="n">04</div><h3>Multi-engine + CPL</h3><p>EFIS twin (Tecnam P2006T), then your CPL: 200+ hours, 70+ as PIC.</p></div>
    </div>
    <div class="grid g3 block">
      <div class="pic reveal"><img src="assets/academy-ramp.jpg" alt="Training aircraft on the apron" width="1400" height="933" loading="lazy"><div><h3>Poland · Bydgoszcz</h3><p>Premium option at an international airport. New Tecnam fleet, FNPT-II simulator, concrete runway year-round, fast student visa. On-airfield private rooms available.</p></div></div>
      <div class="pic reveal d1"><img src="assets/academy-cessna.jpg" alt="Cessna on final approach" width="1400" height="933" loading="lazy"><div><h3>Czech Republic · Prague</h3><p>Modular budget option near Prague airport. Tecnam, Cessna and Diamond DA42, A320 and FNPT simulators. Student apartments from under EUR 500 a month.</p></div></div>
      <div class="pic reveal d2"><img src="assets/zurich-airport.jpg" alt="Zürich airport" width="1400" height="1050" loading="lazy"><div><h3>Switzerland</h3><p>Flight training and hour building also available in Switzerland. Ask us about the next intake.</p></div></div>
    </div>
    <p class="small" style="margin-top:18px">Non-EU students: flight training starts after your student visa, about 2–3 months after enrolment. PPL online theory can start anytime.</p>
  </div>
</section>

<section class="sec" id="modular">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Modular vs Integrated</span><h2>Pay as you go. Keep your life.</h2>
      <p class="lead">Modular training is typically about 30% cheaper than integrated or MPL, at EUR 55,000–90,000, and you keep around 200 flight hours.</p></div>
    <div class="grid g3">
      <div class="card lift reveal"><h3>Save money</h3><p>Pay each module before you start it. Unused flight hours can be refunded. No premium for brand or campus.</p></div>
      <div class="card lift reveal d1"><h3>Stay flexible</h3><p>Keep your job, pause for months, hop locations for hour building. Your timeline, not ours.</p></div>
      <div class="card lift reveal d2"><h3>Lower risk</h3><p>If a school fails, a modular student loses only the current module. Jetline is a family business backed by major Swiss banks.</p></div>
    </div>
    <div class="note reveal" style="margin-top:22px"><b>Changing school?</b> If your flight school went bankrupt or you are unhappy with your instructor, talk to us. The modular programme lets you continue where you left off.</div>
  </div>
</section>

<section class="sec tint" id="how-to">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">How to become a pilot</span><h2>The EASA roadmap, simplified.</h2>
      <p class="lead">Europe focuses on intensive training that can put you in a jet cockpit with as few as 200 hours. It is a marathon, so plan time, discipline and budget.</p></div>
    <div class="grid g2" style="align-items:start">
      <div class="acc reveal">
        <details open><summary>1 · Check the basics</summary><div class="in"><ul><li><b>Medical:</b> Class 1 at an EASA aero-medical centre.</li><li><b>Education:</b> high school diploma. Maths and physics help.</li><li><b>Age:</b> start at any age, 21 for an ATPL.</li></ul></div></details>
        <details><summary>2 · Modular steps</summary><div class="in"><p>PPL, night VFR, time building, ATPL theory (distance learning), multi-engine and CPL, then multi-engine instrument rating and final exam.</p></div></details>
        <details><summary>3 · Multi-crew + type rating</summary><div class="in"><p>MCC and your A320 type rating make you job-ready for airline selection.</p></div></details>
        <details><summary>4 · Mentoring and simulators</summary><div class="in"><p>Experienced pilots mentor you throughout, and our simulators let you practise before you fly.</p></div></details>
      </div>
      <div class="card reveal d1"><h3>What the job offers</h3><p>Airline pilot salaries are high relative to other professions in Europe or Asia, with strong fringe benefits and growth with experience. A global fleet means a global career.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="icao">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">ICAO to EASA</span><h2>Convert your licence.</h2>
      <p class="lead">We convert third-country ICAO licences to an EASA Part-FCL licence issued by Swiss FOCA. It is not an automatic exchange, but it can be done in 8 to 10 weeks.</p></div>
    <div class="grid g2">
      <div class="card reveal"><h3>CPL conversion</h3><p>Pass ATPL theory, 200+ hours total (100 PIC, a 300 NM cross-country), a 5–15 hour bespoke conversion course, then two CPL skill tests on the Tecnam P2006T.</p><span class="tag" style="margin-top:14px">from EUR 7,300</span></div>
      <div class="card reveal d1"><h3>ATPL conversion</h3><p>For airline pilots: 1,500+ hours incl. 500 on multi-pilot aircraft, ATPL theory and an ATPL skill test in the full flight simulator.</p><span class="tag" style="margin-top:14px">from EUR 2,950</span></div>
    </div>
    <div class="acc reveal" style="margin-top:18px">
      <details><summary>First steps for every candidate</summary><div class="in"><ul><li>EASA medical (Class 1 for CPL/ATPL, Class 2 for PPL) at an aero-medical centre. Get it before you invest in training.</li><li>ICAO English level 4 via a 45-minute online assessment with our language assessors.</li><li>Licence verification from your State of Licence Issue.</li><li>Choose Swiss FOCA as your competent authority and have us audit your logbooks. Start theory early: it takes 2–6 months.</li></ul></div></details>
    </div>
    <div class="row-btns"><a class="btn btn-primary" href="#contact">Get your price quote and checklist <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>
"""
)


def build():
    return page(P, "Airline Academy — Jetline Training",
                "Ab-initio 0 to ATPL pilot training, the airline pilot program, modular vs integrated, how to become a pilot and ICAO to EASA licence conversion.", MAIN)
