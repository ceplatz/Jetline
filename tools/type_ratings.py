from layout import page, phero, chips, tick, SITE

P = "type-ratings.html"

REQS = [
    ("CPL", "with a valid or expired ME-IR"),
    ("70 hours", "pilot in command on aeroplanes"),
    ("ATPL theory", "all subjects passed"),
    ("aUPRT", "advanced upset recovery training certificate. Don’t have it? We offer it."),
    ("MCC", "certificate, or combine it with your rating as integrated iMCC"),
    ("ICAO English 4–6", "or take our ELP exam online"),
    ("Medical Class 1", "valid for the simulator test and base training. Not included in the course price."),
]

MAIN = (
    phero("Type Ratings", "The A320 Type Rating.",
          "Our core course. EASA-approved through Swiss FOCA and taught by Type Rating Instructors with airline experience.",
          chips(P, [("A320 course", "#a320"), ("Packages", "#packages"), ("Base training", "#base"), ("LPC", "#lpc"),
                    ("MCC / JOC", "#mcc"), ("SFI & TRI", "#instructor"), ("Refresher", "#refresher"), ("MCF & Demo", "#mcf")]))
    + f"""
<section class="sec" id="a320">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">A320 Type Rating</span><h2>Four phases to airline-ready.</h2>
      <p class="lead">Training runs through simulator centres in Zürich, Vienna, Frankfurt, Paris and more. Pick the location and dates that suit you.</p></div>
    <div class="grid g4">
      <div class="step reveal"><div class="n">01 · THEORY</div><h3>100+ hours</h3><p>LMS, CBT, VR devices, online mentoring and group exercises, then a theory exam.</p><span class="dur">3–4 weeks · at home</span></div>
      <div class="step reveal d1"><div class="n">02 · SIMULATOR</div><h3>77+ hours</h3><p>About 11 sessions, ending with the License Skill Test (LST) with a TRE or SFE.</p><span class="dur">14–16 days · sim centre</span></div>
      <div class="step reveal d2"><div class="n">03 · BASE TRAINING</div><h3>6 landings + 1 go-around</h3><p>On a real A320 family aircraft. Reduced to 4 landings if you have 500+ hours on CS-25 aircraft.</p><span class="dur">1 day · within 6 months of LST</span></div>
      <div class="step hot reveal d3"><div class="n">04 · AIRLINE BQ</div><h3>Time to shine</h3><p>Airline assessment, psychometric and interview preparation.</p><span class="dur">within 2–6 months</span></div>
    </div>

    <div class="split block">
      <div class="media reveal"><img src="assets/engine.jpg" alt="Technician beside the engine of an Airbus A320 family aircraft" width="1400" height="1050" loading="lazy"></div>
      <div class="copy reveal d1">
        <span class="eyebrow">One rating, nine aircraft</span>
        <h3>The world’s best-selling jet family.</h3>
        <p class="lead">One type rating covers every A320 family variant, with 12,000+ aircraft in service. A Cross Crew Qualification then opens Airbus widebodies.</p>
        <div class="chips"><span class="chip">A318</span><span class="chip">A319</span><span class="chip">A320</span><span class="chip">A321</span>
          <span class="chip neo">A319neo</span><span class="chip neo">A320neo</span><span class="chip neo">A321neo</span><span class="chip neo">A321LR</span><span class="chip neo">A321XLR</span></div>
        <div class="kv" style="grid-template-columns:1fr 1fr;margin-top:24px"><div><small>Validity</small><b>1 year</b></div><div><small>Revalidation</small><b>2-hour LPC</b></div></div>
      </div>
    </div>

    <div class="block reveal">
      <h3>What you need to start</h3>
      <div class="split" style="align-items:start;gap:36px">
        <ul class="ticks" style="margin:0">{''.join(tick(t, b) for b, t in REQS)}</ul>
        <div class="acc">
          <details><summary>Why a type rating makes you employable</summary><div class="in"><p>Airlines prefer “ready entry” pilots: type rated, no wait for licence endorsement, no bonding. A type rating also means higher flexibility across airlines and an easy path to widebodies.</p></div></details>
          <details><summary>Airline placement support</summary><div class="in"><p>Yes. Our Gold package adds CV and interview coaching, simulator assessment prep and our airline application portal. See <a href="#packages" style="color:var(--blue);font-weight:700">packages</a>.</p></div></details>
          <details><summary>Rules to know (EASA FCL)</summary><div class="in"><ul><li>Theory and simulator phases must finish within 6 months.</li><li>Landing training must follow within 6 months of the LST, or the rating starts again.</li><li>Privileges are as per the Type Certificate and Airbus Difference Requirements tables.</li></ul></div></details>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec tint" id="packages">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">Packages &amp; Pricing</span><h2>Choose your A320 package.</h2>
      <p class="lead">Gold unlocks priority airline hiring and partner broker programmes. Start with EUR 2,000 and pay the rest flexibly.</p></div>
    <div class="grid g2">
      <div class="price reveal">
        <span class="name">Silver</span>
        <div class="amt">From EUR 10,995</div>
        <p class="small">A320 type rating as per syllabus. Add modules as you need them.</p>
        <ul class="plist">
          <li><svg><use href="#i-check"/></svg>MCC / JOC optional</li>
          <li><svg><use href="#i-check"/></svg>Airline assessment prep and BQ support optional</li>
          <li><svg><use href="#i-check"/></svg>Base training from EUR 9,000, on top</li>
        </ul>
      </div>
      <div class="price gold reveal d1">
        <span class="name">Gold</span>
        <div class="amt">EUR 11,995 <small>flexible option</small></div>
        <div class="alt"><b>EUR 24,995</b> fixed price, paid upfront, with base training included.</div>
        <ul class="plist">
          <li><svg><use href="#i-check"/></svg>A320 type rating, integrated MCC if required</li>
          <li><svg><use href="#i-check"/></svg>12 months of direct airline applications via our portal</li>
          <li><svg><use href="#i-check"/></svg>Up to 8 hours simulator refresher and assessment prep (ZRH)</li>
          <li><svg><use href="#i-check"/></svg>Private interview simulation and quarterly airline-ready training</li>
          <li><svg><use href="#i-check"/></svg>Airline BQ diploma and recommendation letter</li>
          <li><svg><use href="#i-check"/></svg>LPC discount coupon worth EUR 1,000 (12 months)</li>
          <li><svg><use href="#i-check"/></svg>AI instructor 12 months, PASS software 3 months</li>
          <li><svg><use href="#i-check"/></svg>Examination, SFE, TRE and CAA fees included</li>
        </ul>
        <p class="small">Flexible option: base training from EUR 9,000 on top.</p>
      </div>
    </div>
    <div class="grid g2 reveal" style="margin-top:18px">
      <div class="card"><h3>Integrated MCC + A320</h3><p>For pilots without an MCC: EUR 26,995 total, minimum 2 students. Already took a stand-alone MCC? Book a Gold type rating within 6 months and the iMCC simulator part is credited on your invoice.</p></div>
      <div class="card"><h3>Good to know</h3><p>Base training is normally planned within 2 months of the passed sim check. An express 1-month option is available at extra cost. Subject to training slots. Airline broker costs and insurance are not included. See your personal offer and the terms.</p></div>
    </div>
  </div>
</section>

<section class="sec" id="base">
  <div class="wrap">
    <div class="split">
      <div class="copy reveal">
        <span class="eyebrow">Base Training</span>
        <h2>A320 &amp; B737 landing training.</h2>
        <p class="lead">Missing your landing training? We fly every month and welcome students from any ICAO or EASA ATO. Slots are available with no waiting time.</p>
        <div class="tblwrap" style="margin-top:22px"><table class="tbl">
          <tr><th>Option</th><th>Price</th></tr>
          <tr><td>6 landings + 1 go-around, A320</td><td>EUR 13,600</td></tr>
          <tr><td>4 landings + 1 go-around, A320 (500+ h on CS-25)</td><td>EUR 11,950</td></tr>
        </table></div>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><div><b>You need</b> <span>valid Class 1 medical, passport or visa, a passed LST within 6 months, and prepayment.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>Stay flexible</b> <span>plan 1–3 days at the airfield for weather, roster or technical changes.</span></div></li>
        </ul>
        <div class="row-btns"><a class="btn btn-primary" href="{SITE}/base-training-a320">Book base training <svg><use href="#i-arrow"/></svg></a></div>
      </div>
      <div class="media reveal d1"><img src="assets/sim-dark.jpg" alt="A320 flight deck at dusk" width="1400" height="1050" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="sec tint" id="lpc">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">LPC &amp; Revalidation</span><h2>Keep your type rating valid.</h2>
      <p class="lead">Book at least 90 days before expiry and you extend your rating by 12 months. The check covers all mandatory EASA exercises, such as engine failure after V1, rejected take-offs and single-engine go-arounds.</p></div>
    <div class="grid g2" style="align-items:start">
      <div class="tblwrap reveal"><table class="tbl">
        <tr><th>A320 LPC with examiner</th><th>Price</th></tr>
        <tr><td>Zürich (ZRH)</td><td>EUR 1,985</td></tr>
        <tr><td>Vienna (VIE)</td><td>EUR 1,865</td></tr>
        <tr><td>Berlin (BER)</td><td>EUR 1,865</td></tr>
      </table></div>
      <div class="acc reveal d1">
        <details open><summary>Revalidation or renewal?</summary><div class="in"><p><b>Valid rating:</b> book your LPC online (EASA FCL holders only, 14 days’ lead time).</p><p><b>Expired rating:</b> we offer a refresher programme and check. Contact us.</p></div></details>
        <details><summary>Save with Jetline</summary><div class="in"><p>Gold package members may get a discount coupon, so they pay only examiner fees and travel. Sim rental with instructor and V-Prep CBT bundles are available on request.</p></div></details>
        <details><summary>Booking tips</summary><div class="in"><p>Choose a slot with another booked seat to avoid waiting for a fellow co-pilot. Travel and accommodation are not included. Wait for the examiner’s confirmation before booking travel.</p></div></details>
      </div>
    </div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/typeratingcheck">Book your LPC <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="sec" id="mcc">
  <div class="wrap">
    <div class="split rev">
      <div class="copy reveal">
        <span class="eyebrow">MCC / JOC</span>
        <h2>Your bridge to the multi-pilot jet.</h2>
        <p class="lead">Move from single-pilot flying to airline crew work on the A320 simulator. Teamwork, communication and decision-making, with Airline Orientation Training built in.</p>
        <div class="kv" style="grid-template-columns:1fr 1fr;margin-top:22px"><div><small>Theory</small><b>~30 h online</b></div><div><small>Simulator</small><b>5 days · ~35 h</b></div></div>
        <div class="tblwrap" style="margin-top:22px"><table class="tbl">
          <tr><th>MCC + JOC, A320 FTD</th><th>Price</th></tr>
          <tr><td>Prague (PRG)</td><td>from EUR 2,995</td></tr>
          <tr><td>Vienna / Budapest</td><td>EUR 3,862</td></tr>
          <tr><td>Zürich (ZRH)</td><td>EUR 4,995</td></tr>
        </table></div>
        <p class="small" style="margin-top:12px">Start online anytime. Entry: CPL or PPL, English level 4, 40+ hours as PIC, valid or expired ME-IR.</p>
        <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/mcc-joc">Book MCC / JOC <svg><use href="#i-arrow"/></svg></a></div>
      </div>
      <div class="media reveal d1"><img src="assets/sim-crew.jpg" alt="Two students in the A320 simulator" width="1400" height="1050" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="sec tint" id="instructor">
  <div class="wrap">
    <div class="sec-head reveal"><span class="eyebrow">SFI &amp; TRI Instructor</span><h2>Teach the next generation.</h2>
      <p class="lead">Become an A320 or B737 airline instructor and work freelance or employed, worldwide. Courses from EUR 4,995.</p></div>
    <div class="grid g2">
      <div class="card reveal"><h3>TRI: Type Rating Instructor</h3><p>Turns experienced airline pilots into educators: teaching techniques, simulator operation and type-specific instruction. With extra assessments you can conduct base training and line flying under supervision.</p></div>
      <div class="card reveal d1"><h3>SFI: Synthetic Flight Instructor</h3><p>Instruction in the simulator, with teaching skills and session management. A320 and B737.</p></div>
    </div>
    <div class="acc reveal" style="margin-top:18px">
      <details><summary>Prerequisites (EASA Part-FCL)</summary><div class="in"><p><b>TRI (MPA):</b> valid CPL, MPL or ATPL and type rating; teaching and learning course; 1,500 hours on multi-pilot aeroplanes; 30 route sectors in the past 12 months (15 may be in an FFS).</p><p><b>SFI (A):</b> CPL, MPL or ATPL held; teaching and learning course; type proficiency check in an FFS within 12 months; 1,500 hours on multi-pilot aeroplanes; recent route sectors or line-oriented simulator sessions. Always check the current FCL revision.</p></div></details>
    </div>
    <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/instructor-courses">SFI / TRI course details <svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>

<section class="sec" id="refresher">
  <div class="wrap">
    <div class="grid g2" style="align-items:start">
      <div class="reveal">
        <span class="eyebrow">TRI / SFI Refresher</span>
        <h2 style="font-size:clamp(1.7rem,3.2vw,2.5rem);margin:14px 0 16px">Online instructor refresher.</h2>
        <p class="lead">Self-paced seminar for SFI or TRI revalidation or renewal, at the discretion of our Head of Training. Content follows FCL.940: licensing refresher, CBTA assessment and report writing, briefing techniques and TEM.</p>
        <div class="kv" style="grid-template-columns:1fr 1fr;margin-top:22px"><div><small>Price</small><b>EUR 795</b></div><div><small>Format</small><b>38 online steps</b></div></div>
        <div class="row-btns"><a class="btn btn-ghost" href="{SITE}/challenge-page/tri-online-refresher">Join the refresher <svg><use href="#i-arrow"/></svg></a></div>
      </div>
      <div class="reveal d1" id="mcf">
        <span class="eyebrow">MCF &amp; Demo Pilot</span>
        <h2 style="font-size:clamp(1.7rem,3.2vw,2.5rem);margin:14px 0 16px">Maintenance check flights.</h2>
        <p class="lead">EASA SPO requires a course before maintenance check flights (Level A) and demo flights. Types: A320, A330/350, B737, ATR and Embraer E170–195. Our instructors have extensive demo and test-flight experience, including lessee changes and returns to lessor.</p>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg><div><b>Content</b> <span>SPO.SPEC.MCF regulation, risk management, flight profiles, ATC coordination, reports.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>Format</b> <span>Theory plus Level D simulator. On request from two participants.</span></div></li>
          <li><svg><use href="#i-check"/></svg><div><b>For</b> <span>type-rated pilots (PIC: 1,000 h on similar aircraft) and task specialists.</span></div></li>
        </ul>
        <div class="row-btns"><a class="btn btn-ghost" href="#contact">Enquire <svg><use href="#i-arrow"/></svg></a></div>
      </div>
    </div>
  </div>
</section>
"""
)


def build():
    return page(P, "Type Ratings — Jetline Training",
                "A320 type rating course, packages and prices, base training, LPC revalidation, MCC/JOC, SFI/TRI instructor courses and MCF demo pilot courses.", MAIN)
