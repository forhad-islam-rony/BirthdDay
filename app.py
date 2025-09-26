# app.py
import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="Happy Birthday Ayman Zerin 🎂", page_icon="🎉", layout="wide")


# --------- Config ----------
CRUSH_NAME = "Ayman Zerin"
BIRTHDAY_MONTH = 9
BIRTHDAY_DAY = 26

from datetime import datetime, date, time

now = datetime.now()
today = now.date()

# Birthday this year
bday_this_year = date(now.year, BIRTHDAY_MONTH, BIRTHDAY_DAY)

if today == bday_this_year:
    next_bday = today   # Today is birthday
elif today < bday_this_year:
    next_bday = bday_this_year
else:
    # Birthday passed this year
    next_bday = date(now.year + 1, BIRTHDAY_MONTH, BIRTHDAY_DAY)

# Countdown target: end of birthday day
target_iso = datetime.combine(next_bday, time(23, 59, 59)).isoformat()



# --------- HTML Template (raw string, will replace placeholders) ----------
html_template = r"""
<!doctype html>
<html>
<head>
  <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
  <style>
    /* Reset + layout */
    *{box-sizing:border-box;margin:0;padding:0}
    html,body{height:100%;width:100%;font-family:Inter, "Helvetica Neue", Arial, sans-serif;background:#020617;overflow:hidden}
    .scene{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;color:white}
    /* sky gradient */
    .sky{position:absolute;inset:0;background:
      radial-gradient(1200px 400px at 10% 10%, rgba(30,35,80,0.35), transparent 20%),
      radial-gradient(900px 300px at 90% 25%, rgba(70,30,90,0.22), transparent 18%),
      linear-gradient(180deg,#010117 0%, #07102a 50%, #071428 100%);filter:blur(0.0px);}

    /* stars */
    .star {
    position: absolute;
    background: radial-gradient(circle, #fff 0%, rgba(255,255,255,0) 60%);
    border-radius: 50%;
    animation: twinkle 2s infinite alternate;
}
@keyframes twinkle {
    0% { opacity: 0.2; }
    50% { opacity: 0.7; }
    100% { opacity: 0.3; }
}

    /* moon */
 .moon {
    width: 120px; 
    height: 120px;
    border-radius: 50%;
    background: radial-gradient(circle at 30% 30%, #fdf9e3, #d6d6d6);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4), inset -5px -3px 20px rgba(0,0,0,0.05);
    position: absolute;
    top: 60px;       /* Adjust vertical position */
    right: 80px;     /* Adjust horizontal position */
    overflow: visible;
}
.moon::before {
    content:""; 
    position:absolute;
    width: 20px; height: 20px; border-radius:50%;
    background: rgba(0,0,0,0.05);
    top:30px; left:50px;
}
.moon::after {
    content:""; 
    position:absolute;
    width: 12px; height: 12px; border-radius:50%;
    background: rgba(0,0,0,0.04);
    top:70px; left:80px;
}
.moon-glow {
    position:absolute; 
    left:50%; top:50%; 
    transform:translate(-50%,-50%);
    width: 400px; height:400px; border-radius:50%;
    background: radial-gradient(circle, rgba(255,255,210,0.12), transparent 40%);
    filter: blur(28px);
}


    /* central card (transparent) */
    .card{
      position:relative;
      width:94%;max-width:720px;margin:auto;padding:24px;border-radius:18px;
      display:flex;flex-direction:column;align-items:center;gap:14px;
      background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      backdrop-filter: blur(6px) saturate(120%);
      box-shadow: 0 12px 40px rgba(2,6,20,0.6);
    }

    /* big floating text in sky */
    .sky-text {
      font-weight:900;
      font-size:clamp(22px, 7.5vw, 46px);
      text-align:center;
      letter-spacing: -0.6px;
      color: transparent;
      -webkit-text-stroke: 0.8px rgba(255,255,255,0.08);
      text-shadow:
        0 6px 26px rgba(126,123,255,0.08),
        0 2px 8px rgba(255,70,99,0.03);
      position:relative;
      padding: 6px 14px;
      z-index:10;
    }

    /* neon fill effect using pseudo element */
    .sky-text::before{
      content: attr(data-text);
      position:absolute;left:0;top:0;right:0;bottom:0;
      color: #fff;
      background: linear-gradient(90deg,#FF6A86 0%, #FF4663 28%, #7E7BFF 60%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 8px 28px rgba(126,123,255,0.14)) drop-shadow(0 6px 20px rgba(255,70,99,0.06));
      transform-origin: center;
      animation: floatText 6.8s ease-in-out infinite;
      will-change: transform, opacity;
    }

    @keyframes floatText {
      0%{transform:translateY(0) scale(1);opacity:1}
      50%{transform:translateY(-10px) scale(1.02);opacity:0.95}
      100%{transform:translateY(0) scale(1);opacity:1}
    }

    /* small subtitle */
    .sub, .note {color:rgba(255,255,255,0.75);font-weight:600;font-size:14px}

    /* countdown boxes */
    .countdown{display:flex;gap:10px;margin-top:6px}
    .countbox{min-width:66px;background:linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.02));padding:10px;border-radius:12px;text-align:center;box-shadow: 0 8px 22px rgba(2,6,20,0.6)}
    .countnum{font-weight:800;font-size:18px;color:#ffd166}
    .countlabel{font-size:11px;color:rgba(255,255,255,0.6);margin-top:6px}

    /* controls */
    .controls{display:flex;gap:8px;margin-top:12px}
    .btn{padding:9px 12px;border-radius:10px;border:none;font-weight:700;cursor:pointer}
    .btn-primary{background:linear-gradient(90deg,#FF6A86,#FF4663);color:#fff;box-shadow:0 8px 26px rgba(255,70,99,0.12)}
    .btn-soft{background:transparent;border:1px solid rgba(255,255,255,0.06);color:#fff}


    /* fireworks canvas */
    canvas#fire{position:fixed;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:5}

    /* responsive tweaks */
    @media (max-width:520px){
      .moon{width:92px;height:92px}
      .moon-wrap{right:5vw;top:6vh}
      .card{padding:16px;border-radius:12px}
      .sky-text::before{font-size:clamp(20px,9vw,34px)}
    }
  </style>
</head>
<body>
  <div class="sky"></div>
  <div class="stars" id="stars"></div>

  <div class="moon-wrap">
    <div class="moon"></div>
    <div class="moon-glow"></div>
  </div>

  <canvas id="fire"></canvas>

  <div class="scene">
    <div class="card" id="card">
      <div class="sky-text" id="skyText" data-text="Happy Birthday {CRUSH_NAME}">Happy Birthday {CRUSH_NAME}</div>
      <div class="sub">Wishing you a night full of magic and a year full of dreams come true ✨</div>
      <div class="countdown" id="countdown">
        <div class="countbox"><div class="countnum" id="days">--</div><div class="countlabel">DAYS</div></div>
        <div class="countbox"><div class="countnum" id="hours">--</div><div class="countlabel">HOURS</div></div>
        <div class="countbox"><div class="countnum" id="minutes">--</div><div class="countlabel">MIN</div></div>
        <div class="countbox"><div class="countnum" id="seconds">--</div><div class="countlabel">SEC</div></div>
      </div>

      <div class="controls">
        <button class="btn btn-primary" id="surpriseBtn">Surprise Me 🎆</button>
      </div>
      <div class="note">You are the prettiest girl, with the most beautiful soul that lights up the world".</div>
    </div>
  </div>


<script>
  // inject dynamic values from Python
  const targetISO = "{TARGET_ISO}";
  const crushName = "{CRUSH_NAME}";

  // ---------- create stars ----------
  const starsEl = document.getElementById('stars');
  const starCount = 120;
  for (let i=0;i<starCount;i++){
    const s = document.createElement('div');
    s.className = 'star';
    const size = 4 + Math.random()*2.6 + 0.6;
    s.style.width = size + 'px';
    s.style.height = size + 'px';
    s.style.left = (Math.random()*100) + '%';
    s.style.top = (Math.random()*100) + '%';
    s.style.opacity = 0.4 + Math.random()*0.8;
    s.style.transform = `translateZ(0)`;
    starsEl.appendChild(s);
  }

  // subtle twinkle (randomized)
  function twinkle(){
    const children = starsEl.children;
    for (let i=0;i<children.length;i++){
      const t = children[i];
      t.style.transition = 'opacity 1.2s ease-in-out';
      t.style.opacity = 0.2 + Math.random()*0.9;
    }
  }
  setInterval(twinkle, 1400);

  // ---------- countdown ----------
  // ---------- countdown ----------
let targetDate = new Date(targetISO);

const storageKey = 'birthdayCelebrationStart';



function startCelebration(){
    // launch fireworks every 3s
    launchFireworks(50);
    window.celebrationInterval = setInterval(()=>launchFireworks(50), 3000);
}

function celebrateBirthday() {
    // Prevent multiple triggers
    if (window.celebrationActive) return;
    window.celebrationActive = true;

    // Hide original card & countdown
    const card = document.getElementById('card');
    if (card) card.style.display = 'none';

    // Create fullscreen celebration container
    const celebrationLayer = document.createElement('div');
    celebrationLayer.id = 'celebrationLayer';
    celebrationLayer.style.position = 'fixed';
    celebrationLayer.style.top = 0;
    celebrationLayer.style.left = 0;
    celebrationLayer.style.width = '100%';
    celebrationLayer.style.height = '100%';
    celebrationLayer.style.background = 'linear-gradient(180deg, #0a0a1f, #1b1b3f)';
    celebrationLayer.style.overflow = 'hidden';
    celebrationLayer.style.zIndex = '9999';
    celebrationLayer.style.display = 'flex';
    celebrationLayer.style.flexDirection = 'column';
    celebrationLayer.style.alignItems = 'center';
    celebrationLayer.style.justifyContent = 'center';
    document.body.appendChild(celebrationLayer);

    // Add soft animated stars in background
    const starCount = 150;
    for (let i = 0; i < starCount; i++) {
        const s = document.createElement('div');
        s.className = 'celebrationStar';
        s.style.width = s.style.height = (1 + Math.random() * 3) + 'px';
        s.style.background = 'white';
        s.style.borderRadius = '50%';
        s.style.position = 'absolute';
        s.style.left = Math.random() * 100 + '%';
        s.style.top = Math.random() * 100 + '%';
        s.style.opacity = 0.2 + Math.random() * 0.5;
        celebrationLayer.appendChild(s);
    }

    // Animate stars gently
    function animateStars() {
        const stars = document.querySelectorAll('.celebrationStar');
        stars.forEach(s => {
            let top = parseFloat(s.style.top);
            top += 0.02 + Math.random() * 0.1;
            if (top > 100) top = 0;
            s.style.top = top + '%';
        });
        requestAnimationFrame(animateStars);
    }
    animateStars();

    // Add glowing, pulsing "Happy Birthday" text
    const text = document.createElement('h1');
    text.textContent = `🎉 Happy Birthday ${crushName}! 🎉`;
    text.style.color = '#FFD166';
    text.style.fontSize = 'clamp(32px, 8vw, 80px)';
    text.style.fontWeight = '900';
    text.style.textAlign = 'center';
    text.style.textShadow = '0 0 10px #FF6A86, 0 0 20px #FF4663, 0 0 30px #7E7BFF';
    text.style.animation = 'pulseGlow 2.5s infinite alternate';
    celebrationLayer.appendChild(text);

    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes pulseGlow {
            0% { text-shadow: 0 0 10px #FF6A86, 0 0 20px #FF4663, 0 0 30px #7E7BFF; }
            50% { text-shadow: 0 0 20px #FFD166, 0 0 40px #FF6A86, 0 0 60px #7E7BFF; }
            100% { text-shadow: 0 0 10px #FF6A86, 0 0 20px #FF4663, 0 0 30px #7E7BFF; }
        }
    `;
    document.head.appendChild(style);

    // Add falling confetti
    const confettiCount = 80;
    for (let i = 0; i < confettiCount; i++) {
        const conf = document.createElement('div');
        conf.style.width = conf.style.height = (4 + Math.random() * 6) + 'px';
        conf.style.background = ['#FFD166', '#FF6A86', '#FF4663', '#7E7BFF', '#FFFFFF'][Math.floor(Math.random() * 5)];
        conf.style.position = 'absolute';
        conf.style.left = Math.random() * 100 + '%';
        conf.style.top = -10 + 'px';
        conf.style.borderRadius = '50%';
        conf.style.opacity = 0.8;
        celebrationLayer.appendChild(conf);

        const speed = 1 + Math.random() * 2;
        const angle = (Math.random() - 0.5) * 0.3;
        function animateConf() {
            let top = parseFloat(conf.style.top);
            let left = parseFloat(conf.style.left);
            top += speed;
            left += angle;
            if (top > window.innerHeight) top = -10;
            if (left < 0) left = 100;
            if (left > 100) left = 0;
            conf.style.top = top + 'px';
            conf.style.left = left + '%';
            requestAnimationFrame(animateConf);
        }
        animateConf();
    }

    // Launch fireworks on canvas (reuse your canvas #fire)
    launchFireworks(60);
    if (!window.fireworksInterval) {
        window.fireworksInterval = setInterval(() => launchFireworks(50 + Math.random() * 40), 800);
    }

    // Save celebration start to localStorage
    localStorage.setItem(storageKey, new Date().toISOString());
}


// ---------- countdown update ----------
function updateCountdown() {
    const now = new Date();
    let diff = targetDate - now;
    diff = -1;
    if (diff <= 0) {
        // Trigger birthday celebration
        celebrateBirthday();

        // Set next year's birthday without modifying const directly
        const nextYearDate = new Date(targetDate);
        nextYearDate.setFullYear(nextYearDate.getFullYear() + 1);
        targetDate = nextYearDate;

        // Save to localStorage for 7-day celebration
        localStorage.setItem(storageKey, new Date().toISOString());
        diff = targetDate - now;
    }

    const s = Math.floor(diff / 1000);
    const days = Math.floor(s / (3600*24));
    const hours = Math.floor((s % (3600*24)) / 3600);
    const minutes = Math.floor((s % 3600) / 60);
    const seconds = s % 60;

    document.getElementById('days').textContent = days;
    document.getElementById('hours').textContent = hours.toString().padStart(2,'0');
    document.getElementById('minutes').textContent = minutes.toString().padStart(2,'0');
    document.getElementById('seconds').textContent = seconds.toString().padStart(2,'0');
}

setInterval(updateCountdown, 1000);
updateCountdown();


  // ---------- fireworks (canvas) ----------
  const canvas = document.getElementById('fire');
  const ctx = canvas.getContext('2d');
  let W = canvas.width = window.innerWidth;
  let H = canvas.height = window.innerHeight;
  window.addEventListener('resize', ()=>{ W=canvas.width=window.innerWidth; H=canvas.height=window.innerHeight; });

  function rand(a,b){ return a + Math.random()*(b-a); }
  let particles = [];

  function launchFireworks(count=50){
    const centerX = rand(0.15*W, 0.85*W);
    const centerY = rand(0.15*H, 0.6*H);
    for (let i=0;i<count;i++){
      const angle = Math.PI*2 * Math.random();
      const speed = rand(1.6, 7.8);
      particles.push({
        x: centerX,
        y: centerY,
        vx: Math.cos(angle)*speed,
        vy: Math.sin(angle)*speed,
        life: rand(800, 1600),
        age: 0,
        r: rand(1.8,4.8),
        color: ['#FF6A86','#FF4663','#7E7BFF','#FFD166','#FFB4A2'][Math.floor(Math.random()*5)],
      });
    }
    if (!animating) { animating = true; requestAnimationFrame(loop); }
  }

  let animating = false;
  function loop(ts){
    ctx.clearRect(0,0,W,H);
    for (let i=particles.length-1;i>=0;i--){
      const p = particles[i];
      p.age += 16;
      p.vy += 0.06; // gravity
      p.x += p.vx;
      p.y += p.vy;
      p.r *= 0.997;
      const alpha = Math.max(0, 1 - p.age / p.life);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = p.color;
      ctx.beginPath();
      ctx.arc(p.x, p.y, Math.max(0.6, p.r), 0, Math.PI*2);
      ctx.fill();
      if (p.age > p.life || p.r < 0.5) particles.splice(i,1);
    }
    ctx.globalAlpha = 1;
    if (particles.length>0) requestAnimationFrame(loop);
    else animating = false;
  }

  // button handlers
  document.getElementById('surpriseBtn').addEventListener('click', ()=>{
    // launch multiple bursts
    for (let i=0;i<6;i++){
      setTimeout(()=> launchFireworks(36 + Math.floor(Math.random()*30)), i*280);
    }
    // small shake of the sky text
    const txt = document.getElementById('skyText');
    txt.style.transition = 'transform 320ms cubic-bezier(.2,.8,.2,1)';
    txt.style.transform = 'translateY(-8px) scale(1.02)';
    setTimeout(()=> txt.style.transform = '', 520);
  });


  // attempt autoplay on first user gesture (mobile browsers block autoplay)
  function initOnGesture(){
    document.removeEventListener('click', initOnGesture);
    try { if (bg.src) bg.play().catch(()=>{}); } catch(e){}
  }
  document.addEventListener('click', initOnGesture);

  // set the sky text content (in case CRUSH_NAME contains quotes)
  (function setText(){
    const el = document.getElementById('skyText');
    el.setAttribute('data-text', `Happy Birthday ${crushName}`);
    el.textContent = `Happy Birthday ${crushName}`;
  })();

  // responsive: small gentle entrance
  const card = document.getElementById('card');
  card.style.opacity = 0; card.style.transform = 'translateY(8px) scale(.995)';
  setTimeout(()=>{ card.style.transition='all 700ms cubic-bezier(.2,.9,.2,1)'; card.style.opacity=1; card.style.transform=''; }, 90);

</script>
</body>
</html>
"""


# Prepare the HTML with replacements
html = html_template.replace("{CRUSH_NAME}", CRUSH_NAME).replace("{TARGET_ISO}", target_iso)

# --------- Render in Streamlit ----------
st.components.v1.html(html, height=900, scrolling=False)


import streamlit as st


# Hide Streamlit header/footer and menu

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}      /* hides menu (top-right hamburger) */
    footer {visibility: hidden;}         /* hides footer (Streamlit branding) */
    header {visibility: hidden;}         /* hides top bar completely */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
