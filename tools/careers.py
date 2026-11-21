from layout import page, phero, chips, tick, SITE

P = "careers.html"

AIRLINES = [("SAS & SAS Connect", "via broker assessment centre"), ("Condor", "Condor Flight Group"), ("Wizz Air", "various AOCs"),
            ("Marabu", "Condor Flight Group"), ("Chair", "since 2022"), ("Air Albania", "since 2020"), ("Volotea", "since 2019, FOs and instructors")]

ALUMNI = [
    ("Ryan F.", "European charter airline", "Joined after his type rating with no hours on type. F/O in Munich."),
    ("Anthony L.", "LEAV", "Joined immediately after his type rating. F/O in Köln."),
    ("João S.", "Titan Airways, UK", "Hired by two airlines straight after the rating, with no hours on type."),
    ("Vesterlund", "SAS Connect", "Joined his first airline right after the rating, with 500+ hours on the A320 by summer 2025."),
    ("Marta S.", "Volotea", "Joined Volotea right after her type rating."),
    ("Robin L.", "Air Albania", "Direct-entry F/O on the A320 since 2023."),
    ("Daniel D.", "Skyexpress → BulAir", "300 h on type, then 500+ h line flying, and an A330 with a Spanish airline in 2025."),
    ("Nans S.", "Three airlines", "Found jobs at 3 airlines after the rating and now has 2,000+ hours on type."),
]

STORIES = [
    ("Found a job within 2 months", "i-found-a-job-within-2-months-thanks"),
    ("Fast track to airline assessment", "fast-track-to-airlineassessment-with-a320-typerating"),
    ("My first flight as A320 first officer", "from-dreams-to-reality-my-journey-as-a320-first-officer-on-my-first-flight-from-munich-to-greece"),
    ("Line intro experience", "a320-line-intro-experience-blog-found-a-job-directly-after-type-rating-on-a320-as-first-officer"),
    ("The ACMI and charter fast track", "unlocking-the-acmi-model-or-small-holiday-charter-airline-a-fast-track-to-your-aviation-career"),
    ("Type rating benefits and placement support", "what-are-the-benefits-of-type-rating-courses-like-a320-or-b737-can-i-get-airline-placement-support"),
]

MAIN = (
    phero("Careers", "From type rating to the flight deck.",
          "Airlines hire type-rated first officers, often with no hours on type. See who hires, how graduates got there, and how the line training pathway adds real hours.",
          chips(P, [("First-officer careers", "#first-officer"), ("Line training pathway", "#pathway"), ("Graduates", "#graduates"),
                    ("Student stories", "#stories"), ("Application portal", "#portal")]))
    + f"""
<section class="sec" id="first-officer">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">First-Officer Careers</span><h2>Airlines that hired our graduates.</h2>
      <p class="lead">Many airlines recruit type-rated first officers with no hours on type, and some accept you even when the advert asks for 500 hours. They want a pilot who is ready now, with no bond and no risk of a delayed endorsement.</p></div>
    <div class="airlines reveal">{''.join(f'<div class="airline"><b>{a}</b><small>{b}</small></div>' for a, b in AIRLINES)}</div>
    <div class="note reveal" style="margin-top:22px"><b>Plan your timing.</b> Airline assessment seasons run in December and January. Complete your type rating before spring so it is valid when recruitment opens.</div>
  </div>
</section>

<section class="sec tint" id="pathway">
  <div class="wrap">
    <div class="line-strip reveal">
      <div class="lm"><img src="assets/flightdeck-pair.jpg" alt="Two pilots on an A320 flight deck" width="1400" height="1050" loading="lazy"></div>
      <div class="lb">
        <span class="eyebrow">Line Training Pathway <span class="tag new" style="margin-left:10px">New</span></span>
        <h2>Add real hours on the A320.</h2>
        <p class="lead">Some airlines only hire with 100, 300 or 500 hours on type. Our pathway for type-rated Jetline students builds those hours as a first officer with ACMI and charter partners, at bases across Europe. It is opening soon.</p>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><div><b>Real line experience</b> <span>First-officer hours on type, seasonal.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>Better odds</b> <span>Qualify for airlines that ask for 300 or 500 hours.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>Free info event</b> <span>Meet partner broker or airline HR at Jetline.</span></div></li>
        </ul>
        <div class="note" style="margin-top:20px"><b>An investment, openly explained.</b> Gold members get priority access to partner programmes. Broker costs and partner terms apply, and we explain them before you commit.</div>
        <div class="row-btns"><a class="btn btn-primary" href="#contact">Ask about line training <svg><use href="#i-arrow"/></svg></a></div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="graduates">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Graduates</span><h2>Alumni, now flying.</h2>
      <p class="lead">A selection of Jetline graduates and where they fly today.</p></div>
    <div class="grid g4">{''.join(f'<div class="alum reveal"><b>F/O {n}</b><small>{a}</small><p>{t}</p></div>' for n, a, t in ALUMNI)}</div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/graduates">All graduates <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="sec tint" id="stories">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Student Stories</span><h2>Line intro, in their words.</h2>
      <p class="lead">Graduates write about operator conversion courses, line introduction flights, line checks and release as first officer.</p></div>
    <div class="grid g3">{''.join(f'<a class="card lift reveal" href="{SITE}/post/{u}"><h3>{t}</h3><span class="more">Read the story ↗</span></a>' for t, u in STORIES)}</div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/blog">Read the blog <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="sec" id="portal">
  <div class="wrap">
    <div class="split">
      <div class="copy reveal">
        <span class="eyebrow">Airline Application Portal</span>
        <h2>Apply directly, for a year.</h2>
        <p class="lead">Gold type rating packages include 12 months of direct airline applications through our portal, quarterly airline-ready training, and a recommendation letter.</p>
        <div class="row-btns"><a class="btn btn-ghost" href="type-ratings.html#packages">See Gold <svg><use href="#i-arrow"/></svg></a><a class="btn btn-ghost" href="prep.html#aap">Assessment prep</a></div>
      </div>
      <div class="media reveal d1"><img src="assets/sim-cockpit.jpg" alt="A320 simulator flight deck" width="1280" height="960" loading="lazy"></div>
    </div>
  </div>
</section>
"""
)


def build():
    return page(P, "Careers — Jetline Training",
                "Airlines that hire type-rated A320 first officers, the 300/500 hour line training pathway, graduate stories and the airline application portal.", MAIN)
