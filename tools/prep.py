from layout import page, phero, chips, tick, SITE

P = "prep.html"

MAIN = (
    phero("Assessment Prep & Online", "Ready for the airline interview.",
          "Interview and simulator preparation, an A320 AI tutor, and online courses you can study from home.",
          chips(P, [("Airline assessment prep", "#aap"), ("A320 AI tutor", "#maverick"), ("Online courses", "#courses"), ("Other bookings", "#shop")]))
    + f"""
<section class="sec" id="aap">
  <div class="wrap">
    <div class="split">
      <div class="copy reveal">
        <span class="eyebrow">Airline Assessment Prep</span>
        <h2>Interview and simulator, rehearsed.</h2>
        <p class="lead">Book a classroom interview day and a simulator refresher on site. Programmes are tailored to the airline that invited you, for both the interview stages and the simulator screening.</p>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><div><b>Airline-specific</b> <span>preparation briefing with an airline pilot.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>CV and cover letter</b> <span>plus A320 technical interview preparation.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>Gold members</b> <span>get discounted rates, or join free per their course agreement.</span></div></li>
        </ul>
        <div class="row-btns"><a class="btn btn-primary" href="{SITE}/airline-assessment-preparation">See available dates <svg><use href="#i-arrow"/></svg></a></div>
      </div>
      <div class="media reveal d1"><img src="assets/sim-crew.jpg" alt="Two pilots in the A320 simulator" width="1400" height="1050" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="sec tint" id="maverick">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">A320 AI Tutor</span><h2>Meet Maverick.</h2>
      <p class="lead">Our A320 training AI teacher gives interactive dialogue and personalised feedback to prepare you for your type rating, LPC, OPC, airline training or assessment, based on Airbus manuals.</p></div>
    <div class="grid g3">
      <div class="price reveal"><span class="name">Basic</span><div class="amt">EUR 9 <small>per week</small></div>
        <ul class="plist"><li><svg><use href="#i-check"/></svg>Maverick AI access: FCOM, FCTM, QRH, Airbus tutorial slides</li><li><svg><use href="#i-check"/></svg>A320 file share access</li><li><svg><use href="#i-check"/></svg>1-day free trial</li></ul></div>
      <div class="price reveal d1"><span class="name">Silver · Airline Assessment</span><div class="amt">EUR 18 <small>per week</small></div>
        <ul class="plist"><li><svg><use href="#i-check"/></svg>Everything in Basic</li><li><svg><use href="#i-check"/></svg>A320 tutorials and exterior walk-around training</li><li><svg><use href="#i-check"/></svg>CV and cover letter courses</li><li><svg><use href="#i-check"/></svg>7-day free trial</li></ul></div>
      <div class="price gold reveal d2"><span class="name">Gold · Personal Airline Prep</span><div class="amt">EUR 99 <small>per month</small></div>
        <ul class="plist"><li><svg><use href="#i-check"/></svg>Everything in Silver</li><li><svg><use href="#i-check"/></svg>Individual airline assessment preparation</li><li><svg><use href="#i-check"/></svg>One on-site screening simulation</li><li><svg><use href="#i-check"/></svg>V-Prep A320 full video access</li></ul></div>
    </div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/pricing-plans/a320-ai-membershipplans">Try Maverick <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="sec" id="courses">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Online Courses</span><h2>Study at home, at your pace.</h2></div>
    <div class="grid g3">
      <div class="card lift reveal"><h3>A320 exterior inspection</h3><p>How to do the walk-around. One week of access.</p><span class="tag">EUR 99</span></div>
      <div class="card lift reveal d1"><h3>A320 technical interview prep</h3><p>Exam preparation, part of Airline Assessment Prep.</p><span class="tag">EUR 24</span></div>
      <div class="card lift reveal d2"><h3>Aviation CV &amp; cover letter</h3><p>Two courses that get you through airline screening. Plans available.</p><span class="tag">2 plans</span></div>
      <div class="card lift reveal"><h3>MCC / JOC online part</h3><p>Online theory for the A320 MCC course.</p><span class="tag">Free</span></div>
      <div class="card lift reveal d1"><h3>Instructor course parts</h3><p>Teaching and learning online for SFI and TRI (MPA) courses.</p><span class="tag">Free</span></div>
      <div class="card lift reveal d2"><h3>TRI / SFI refresher</h3><p>Online seminar for revalidation or renewal, 38 steps.</p><span class="tag">EUR 795</span></div>
    </div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/online-programs">All online programs <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="sec tint" id="shop">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Other Bookings</span><h2>Online shop.</h2>
      <p class="lead">Book quick-start options and add-ons online.</p></div>
    <div class="tblwrap reveal"><table class="tbl">
      <tr><th>Item</th><th>Price</th></tr>
      <tr><td>Down payment, A320 type rating course (quick start)</td><td>EUR 2,000</td></tr>
      <tr><td>Down payment, teaching &amp; learning or SFI / TRI courses</td><td>EUR 1,000</td></tr>
      <tr><td>TRI / SFI teaching &amp; learning course only</td><td>EUR 1,495</td></tr>
      <tr><td>Advanced upset recovery training (aUPRT)</td><td>EUR 2,950</td></tr>
      <tr><td>ELP language proficiency exam</td><td>EUR 595</td></tr>
      <tr><td>Conversion / licence validation support with Swiss TRE and FOCA</td><td>EUR 885</td></tr>
    </table></div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/online-pilot-shop">Open the shop <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>
"""
)


def build():
    return page(P, "Assessment Prep & Online — Jetline Training",
                "Airline assessment preparation, Maverick the A320 AI tutor with membership plans, online courses and the Jetline online shop.", MAIN)
