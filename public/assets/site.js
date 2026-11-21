(function(){
  var d=document, root=d.documentElement, body=d.body;

  /* ---------- Header: shadow on scroll, mobile drawer, mega menus ---------- */
  var h=d.querySelector('header.site');
  function onScroll(){ if(h) h.classList.toggle('scrolled', window.scrollY>8); }
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

  var burger=d.querySelector('.burger');
  if(burger) burger.addEventListener('click',function(){
    var o=body.classList.toggle('menu-open'); burger.setAttribute('aria-expanded',o);
  });
  var items=[].slice.call(d.querySelectorAll('.nav li.has-menu'));
  function closeAll(except){ items.forEach(function(li){ if(li!==except){ li.classList.remove('open'); li.firstElementChild.setAttribute('aria-expanded','false'); } }); }
  items.forEach(function(li){
    var btn=li.firstElementChild, t;
    btn.addEventListener('click',function(e){
      e.stopPropagation();
      var o=!li.classList.contains('open'); closeAll(li);
      li.classList.toggle('open',o); btn.setAttribute('aria-expanded',o);
    });
    li.addEventListener('mouseenter',function(){ if(window.innerWidth>940){ clearTimeout(t); closeAll(li); li.classList.add('open'); btn.setAttribute('aria-expanded','true'); } });
    li.addEventListener('mouseleave',function(){ if(window.innerWidth>940){ t=setTimeout(function(){ li.classList.remove('open'); btn.setAttribute('aria-expanded','false'); },180); } });
  });
  d.addEventListener('click',function(){ closeAll(); });
  d.addEventListener('keydown',function(e){ if(e.key==='Escape') closeAll(); });
  d.querySelectorAll('.menu a, .nav>ul>li>a').forEach(function(a){ a.addEventListener('click',function(){ body.classList.remove('menu-open'); closeAll(); }); });

  /* ---------- Reveal on scroll ---------- */
  var els=d.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.1,rootMargin:'0px 0px -5% 0px'});
    els.forEach(function(el){io.observe(el)});
  } else { els.forEach(function(el){el.classList.add('in')}); }

  /* ---------- Splash intro (home page only, once per visit, skippable) ----------
     line sweeps in -> three words, one at a time -> line hands over to the logo -> fade into the page */
  var sp=d.getElementById('splash');
  if(sp && root.classList.contains('js-splash')){
    body.classList.add('locked');
    var word=d.getElementById('spWord'), fin=d.getElementById('spFinal'), timers=[], done=false;
    var WORDS=['Type Rated.','Line Checked.','Flight Deck Ready.'];
    var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var at=function(ms,fn){ timers.push(setTimeout(fn,ms)); };
    var finish=function(){
      if(done) return; done=true; timers.forEach(clearTimeout);
      try{ sessionStorage.setItem('jt-splash','1'); }catch(e){}
      sp.classList.add('out'); body.classList.remove('locked');
      setTimeout(function(){ root.classList.remove('js-splash'); },1000);
    };
    if(reduce){ d.getElementById('spLine').style.display='none'; fin.classList.add('in'); at(1500,finish); }
    else{
      sp.classList.add('glow','sweep');
      var t=900;
      WORDS.forEach(function(w){
        at(t,function(){
          word.classList.remove('in','out');
          word.style.transition='none'; word.textContent=w; void word.offsetWidth; word.style.transition='';
          word.classList.add('in');
        });
        at(t+1000,function(){ word.classList.remove('in'); word.classList.add('out'); });
        t+=1150;
      });
      at(t,function(){ sp.classList.add('merge'); fin.classList.add('in'); });
      at(t+2300,finish);
    }
    sp.addEventListener('click',finish);
    d.addEventListener('keydown',function(e){ if(!done&&(e.key==='Escape'||e.key==='Enter'||e.key===' ')){ e.preventDefault(); finish(); } });
    setTimeout(finish,9000);
  }

  /* ---------- Contact form ---------- */
  // DEMO MODE: while true, the form sends nothing anywhere. Set to false to go live.
  var DEMO=true;
  var SDK='https://www.gstatic.com/firebasejs/10.14.1/';
  var f=d.getElementById('contact-form'), m=d.getElementById('form-msg');
  if(f){
    var show=function(html,err){ m.className='form-msg show'; m.innerHTML=html; m.style.borderColor=err?'#f3b4b4':''; m.style.background=err?'#fff5f5':''; };
    var mailtoFallback=function(x){
      var b='Name: '+x.firstName+' '+x.lastName+'\nEmail: '+x.email+'\nPhone: '+x.phone+'\nNationality + licence CAA: '+x.licence+'\n\n'+x.message;
      window.location.href='mailto:info@jetline-training.com?subject='+encodeURIComponent('Training request from '+x.firstName+' '+x.lastName)+'&body='+encodeURIComponent(b);
      show('Your email app should open with your request ready to send. If it does not, please write to <b>info@jetline-training.com</b> directly.');
    };
    var saveToFirestore=async function(x){
      var cfg=await fetch('/__/firebase/init.json',{cache:'no-store'});
      if(!cfg.ok) throw new Error('no-firebase-config');
      cfg=await cfg.json();
      var app=await import(SDK+'firebase-app.js'), fs=await import(SDK+'firebase-firestore.js');
      var db=fs.getFirestore(app.initializeApp(cfg));
      await fs.addDoc(fs.collection(db,'enquiries'),{firstName:x.firstName,lastName:x.lastName,email:x.email,phone:x.phone,licence:x.licence,message:x.message,source:'website',createdAt:fs.serverTimestamp()});
    };
    f.addEventListener('submit',async function(ev){
      ev.preventDefault();
      var v=function(id){return d.getElementById(id).value.trim()};
      var x={firstName:v('fn'),lastName:v('ln'),email:v('em'),phone:v('ph'),licence:v('lic'),message:v('msg')};
      if(!x.firstName||!x.lastName||!x.email||!x.phone||!x.message){ show('Please fill in the fields marked with *.',true); return; }
      if(!/^.+@.+\..+$/.test(x.email)){ show('Please enter a valid email address.',true); return; }
      if(DEMO){ show('<b>This is a demo site.</b> Your message was not sent. On the live site, this form delivers your request to Jetline Training.'); return; }
      if(d.getElementById('website').value){ show('Thank you. We will get back to you as soon as possible.'); return; }
      var btn=f.querySelector('button[type=submit]'); btn.disabled=true; show('Sending…');
      try{ await saveToFirestore(x); f.reset(); show('<b>Thank you.</b> We have received your request and will get back to you as soon as possible.'); }
      catch(e){ if(e&&e.message==='no-firebase-config'){ mailtoFallback(x); } else { show('Sorry, something went wrong. Please email <b>info@jetline-training.com</b> directly.',true); } }
      btn.disabled=false;
    });
  }
})();
