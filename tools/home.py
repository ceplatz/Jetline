from layout import page, tick

SPLASH = """<div id="splash" role="dialog" aria-label="Welcome to Jetline Training">
  <div class="sp-line" id="spLine"></div>
  <div class="sp-word" id="spWord" aria-hidden="true"></div>
  <div class="sp-final" id="spFinal">
    <img src="assets/logo.svg" alt="Jetline Training" width="1955" height="1080">
    <div class="sp-tag">Airline pilot training <b>academy</b></div>
  </div>
  <button class="sp-skip" id="spSkip" type="button">Skip intro →</button>
</div>
"""

MAIN = """
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="pill reveal"><i><svg><use href="#i-check"/></svg></i> Swiss FOCA approved ATO &nbsp;·&nbsp; CH.ATO.0310</div>
        <h1 class="reveal d1"><span class="one">Type Rated.</span><span>Line Checked.</span><span>Flight Deck Ready.</span></h1>
        <p class="lead reveal d2">A320 type ratings with airline-captain instructors, simulator centres across Europe, and career support to your first airline.</p>
        <div class="row-btns reveal d3">
          <a class="btn btn-primary" href="#contact">Contact us for more information <svg><use href="#i-arrow"/></svg></a>
          <a class="btn btn-ghost" href="type-ratings.html">Explore Type Ratings</a>
        </div>
      </div>
      <div class="hero-media reveal d2">
        <div class="hero-photo"><img src="assets/hero-cockpit.jpg" alt="Pilot at the thrust levers on the A320 flight deck" width="1800" height="1350" fetchpriority="high"></div>
        <div class="float f2"><div class="ic"><svg><use href="#i-land"/></svg></div><div><b>Base training</b><small>guaranteed after<br>your skill test</small></div></div>
        <div class="float f1"><div class="ic"><svg><use href="#i-plane"/></svg></div><div><b>9 variants</b><small>One A320 rating,<br>A318 to A321XLR</small></div></div>
      </div>
    </div>
    <div class="stats reveal">
      <div class="stat"><b>724</b><span>Graduates</span></div>
      <div class="stat"><b>28</b><span>Airlines hired our students, Europe &amp; Asia</span></div>
      <div class="stat"><b>14</b><span>Training aircraft, A320 to Cessna</span></div>
      <div class="stat"><b>10+</b><span>Years training pilots</span></div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Type Ratings</span>
      <h2>The A320 Type Rating, in three steps.</h2>
      <p class="lead">EASA-approved, delivered by airline Captains. From online theory to the flight deck.</p>
    </div>
    <div class="grid g4">
      <div class="step reveal"><div class="n">STEP 01</div><h3>Theory</h3><p>100+ hours online and classroom, with VR.</p><span class="dur">3–4 weeks · at home</span></div>
      <div class="step reveal d1"><div class="n">STEP 02</div><h3>Simulator</h3><p>77+ hours, ending with your skill test.</p><span class="dur">2 weeks · sim centre</span></div>
      <div class="step reveal d2"><div class="n">STEP 03</div><h3>Base training</h3><p>6 landings plus a go-around on a real A320.</p><span class="dur">1 day on site</span></div>
      <div class="step hot reveal d3"><div class="n">TIME TO SHINE</div><h3>Airline assessment</h3><p>Interview and simulator preparation.</p><span class="dur">within 2–6 months</span></div>
    </div>
    <div class="grid g3" style="margin-top:18px">
      <a class="card lift reveal" href="type-ratings.html#packages"><h3>Packages from EUR 10,995</h3><p>Silver for the rating, Gold with assessment prep and airline applications.</p><span class="more">See packages →</span></a>
      <a class="card lift reveal d1" href="type-ratings.html#base"><h3>Base training &amp; LPC</h3><p>Landing training, revalidation and renewals, A320 and B737.</p><span class="more">Base training &amp; LPC →</span></a>
      <a class="card lift reveal d2" href="type-ratings.html#mcc"><h3>MCC / JOC &amp; instructor courses</h3><p>Multi-crew on the A320, SFI/TRI, refreshers, MCF and demo pilot.</p><span class="more">All courses →</span></a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Why Jetline</span>
      <h2>Airline standards. Your schedule.</h2>
    </div>
    <div class="grid g4">
      <div class="card lift reveal"><div class="ic"><svg><use href="#i-user"/></svg></div><h3>Personal mentor</h3><p>One mentor guides you through the whole course.</p></div>
      <div class="card lift reveal d1"><div class="ic"><svg><use href="#i-star"/></svg></div><h3>Captains teach</h3><p>Standardised instructors who currently fly for airlines.</p></div>
      <div class="card lift reveal d2"><div class="ic"><svg><use href="#i-pin"/></svg></div><h3>Flexible by design</h3><p>Pick the centre, the dates and the pace.</p></div>
      <div class="card lift reveal d3"><div class="ic"><svg><use href="#i-land"/></svg></div><h3>Base training guarantee</h3><p>Landing training lined up after your skill test.</p></div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="eyebrow">Explore</span>
      <h2>More ways to fly with Jetline.</h2>
    </div>
    <div class="grid g3">
      <a class="card lift reveal" href="academy.html"><div class="ic"><svg><use href="#i-book"/></svg></div><h3>Airline Academy</h3><p>No licence yet? PPL to frozen ATPL, modular and pay as you go. ICAO to EASA conversion.</p><span class="more">Airline Academy →</span></a>
      <a class="card lift reveal d1" href="careers.html"><div class="ic"><svg><use href="#i-brief"/></svg></div><h3>Careers</h3><p>Airlines that hire type-rated pilots, alumni stories and the line training pathway.</p><span class="more">Careers →</span></a>
      <a class="card lift reveal d2" href="prep.html"><div class="ic"><svg><use href="#i-spark"/></svg></div><h3>Assessment Prep &amp; Online</h3><p>Interview and simulator prep, Maverick the A320 AI tutor, and online courses.</p><span class="more">Assessment prep →</span></a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="line-strip reveal">
      <div class="lm"><img src="assets/flightdeck-pair.jpg" alt="Two pilots on an A320 flight deck" width="1400" height="1050" loading="lazy"></div>
      <div class="lb">
        <span class="eyebrow">Line Training <span class="tag new" style="margin-left:10px">New</span></span>
        <h2>From the simulator to the line.</h2>
        <p class="lead">Many airlines want 100, 300 or 500 hours on type. Our new pathway adds real first-officer hours on the A320, an investment in your career that we explain openly before you commit.</p>
        <div class="row-btns"><a class="btn btn-ghost" href="careers.html#pathway">Line training pathway <svg><use href="#i-arrow"/></svg></a></div>
      </div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">In their words</span><h2>Graduates, now flying.</h2></div>
    <div class="grid g3">
      <div class="quote reveal"><p>Airlines expect qualified pilots, so the next logical step was clear… The instructors are highly competent and experienced, but above all extremely pedagogical and supportive.</p><footer><div class="av">NC</div><div><b>Nicolas C.</b>France</div></footer></div>
      <div class="quote reveal d1"><p>The atmosphere which you will find during the learning process and online sessions with the instructors is so nice and friendly without any push on you.</p><footer><div class="av">YS</div><div><b>Yasir S.</b>Norway</div></footer></div>
      <div class="quote reveal d2"><p>I got a job as a First Officer… the type rating was the best decision I ever made; I received invitations very quickly after the rating.</p><footer><div class="av">AL</div><div><b>Anthony L.</b>Germany</div></footer></div>
    </div>
    <p class="small" style="text-align:center;margin-top:22px">More feedback on <a href="https://www.trustpilot.com/review/www.jetline-training.com" style="color:var(--blue);font-weight:700">Trustpilot</a>.</p>
  </div>
</section>
"""


def build():
    return page("index.html", "Jetline Training — Type Rated. Line Checked. Flight Deck Ready.",
                "A320 type rating training with airline-captain instructors, simulator centres across Europe and career support. Swiss FOCA approved ATO CH.ATO.0310.",
                MAIN, home=True, splash=SPLASH)
