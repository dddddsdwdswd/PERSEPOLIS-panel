# pages.py - پنل تخت جمشید با ساب‌لینک حرفه‌ای

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏛️ ورود · تخت جمشید</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#08080d;--card:rgba(10,10,30,0.75);--card-b:rgba(139,92,246,0.12);--accent:#8B5CF6;--accent2:#22D3EE;--accent3:#6D28D9;--t1:#EDEDF7;--t2:#B4AEDD;--t3:#69647F;--border:rgba(139,92,246,0.08);--glow:0 0 80px rgba(139,92,246,0.05)}
body{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#08080d,#0a0714,#08080d);padding:20px;color:var(--t1);position:relative;overflow:hidden}
.stars{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.star{position:absolute;border-radius:50%;background:#22D3EE;animation:twinkle 3s ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:0.15}50%{opacity:0.6}}
.glow-orb{position:fixed;border-radius:50%;filter:blur(150px);z-index:0;animation:orbFloat 6s ease-in-out infinite;pointer-events:none}
.orb1{width:500px;height:500px;background:rgba(139,92,246,0.04);top:-200px;right:-100px}
.orb2{width:400px;height:400px;background:rgba(34,211,238,0.03);bottom:-100px;left:-80px;animation-delay:2s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(30px,-30px) scale(1.1)}}
@property --angle{syntax:'<angle>';inherits:false;initial-value:0deg}
.container{position:relative;z-index:10;display:grid;grid-template-columns:1fr 1fr;max-width:1100px;width:100%;background:var(--card);backdrop-filter:blur(40px) saturate(160%);border-radius:24px;overflow:hidden;box-shadow:var(--glow),0 25px 80px rgba(0,0,0,0.6)}
.container::before{content:'';position:absolute;inset:0;border-radius:24px;padding:1.5px;background:conic-gradient(from var(--angle),#8B5CF6,#22D3EE,#6D28D9,#8B5CF6);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;animation:auraSpin 7s linear infinite;pointer-events:none;z-index:1}
@keyframes auraSpin{to{--angle:360deg}}
.login-section{padding:48px 40px}
.brand{display:flex;align-items:center;gap:12px;margin-bottom:32px}
.brand-icon{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#8B5CF6,#6D28D9,#22D3EE);display:flex;align-items:center;justify-content:center;font-size:22px;box-shadow:0 0 40px rgba(139,92,246,0.2);animation:brandPulse 3s ease-in-out infinite}
@keyframes brandPulse{0%,100%{box-shadow:0 0 40px rgba(139,92,246,0.2);transform:scale(1)}50%{box-shadow:0 0 55px rgba(139,92,246,0.35);transform:scale(1.04)}}
.brand-text{font-size:16px;font-weight:800;background:linear-gradient(135deg,#22D3EE,#8B5CF6);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.brand-sub{font-size:9px;color:var(--t3);-webkit-text-fill-color:var(--t3);display:flex;align-items:center;gap:5px}
.live-dot{width:6px;height:6px;border-radius:50%;background:#34D399;box-shadow:0 0 8px #34D399;display:inline-block;animation:livePulse 1.6s ease-in-out infinite}
@keyframes livePulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(1.3)}}
.welcome{font-size:22px;font-weight:800;background:linear-gradient(90deg,var(--t1) 20%,var(--accent2) 50%,var(--t1) 80%);background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px;animation:textShine 4s linear infinite}
@keyframes textShine{to{background-position:-200% center}}
.sub-text{font-size:13px;color:var(--t3);margin-bottom:28px}
.field{margin-bottom:18px}
.field label{display:block;font-size:10px;font-weight:600;color:var(--t2);margin-bottom:4px}
.field input{width:100%;padding:12px 14px;border-radius:10px;border:1px solid var(--border);background:rgba(0,0,20,.3);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:.3s}
.field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(139,92,246,.08),0 0 30px rgba(139,92,246,.04)}
.field input::placeholder{color:var(--t3)}
.options{display:flex;justify-content:space-between;align-items:center;margin:14px 0 20px;font-size:12px}
.options label{display:flex;align-items:center;gap:6px;color:var(--t2);cursor:pointer}
.options label input[type="checkbox"]{accent-color:var(--accent);width:16px;height:16px;cursor:pointer}
.btn-login{width:100%;padding:12px;border-radius:10px;border:none;cursor:pointer;background:linear-gradient(135deg,#8B5CF6,#6D28D9,#22D3EE);background-size:200% 200%;animation:gradientMove 4s ease infinite;color:#0a0714;font-family:inherit;font-size:15px;font-weight:700;transition:all .3s;box-shadow:0 4px 30px rgba(139,92,246,.25)}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-login:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(139,92,246,.35)}
.btn-login:disabled{opacity:.5;cursor:not-allowed;transform:none}
.or-divider{display:flex;align-items:center;gap:14px;margin:20px 0;color:var(--t3);font-size:11px}
.or-divider::before,.or-divider::after{content:'';flex:1;height:1px;background:var(--border)}
.connect-btn{width:100%;padding:12px;border-radius:10px;border:1px solid var(--border);background:rgba(139,92,246,0.03);color:var(--t1);font-family:inherit;font-size:13px;font-weight:600;cursor:pointer;transition:.3s;display:flex;align-items:center;justify-content:center;gap:8px}
.connect-btn:hover{background:rgba(139,92,246,0.06);border-color:rgba(139,92,246,0.2)}
.error-box{display:none;background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.15);border-radius:8px;padding:10px 12px;margin-bottom:14px;font-size:12px;color:#F87171;align-items:center;gap:8px}
.error-box.show{display:flex}
.info-section{background:linear-gradient(135deg,#08080d,#0a0714);padding:48px 36px;display:flex;flex-direction:column;justify-content:center;border-right:1px solid var(--border)}
.info-title{font-size:22px;font-weight:800;color:var(--t1);margin-bottom:6px}
.info-sub{font-size:13px;color:var(--t3);margin-bottom:24px}
.features{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.feature{background:rgba(139,92,246,0.03);border-radius:12px;padding:14px 12px;text-align:center;border:1px solid rgba(139,92,246,0.04)}
.feature .icon{font-size:28px;display:block;margin-bottom:4px;animation:emojiFloat 3s ease-in-out infinite}
.feature:nth-child(1) .icon{animation-delay:0s}
.feature:nth-child(2) .icon{animation-delay:.25s}
.feature:nth-child(3) .icon{animation-delay:.5s}
.feature:nth-child(4) .icon{animation-delay:.75s}
@keyframes emojiFloat{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-4px) rotate(-6deg)}}
.feature .name{font-size:11px;font-weight:600;color:var(--t1)}
.feature .desc{font-size:8px;color:var(--t3);margin-top:2px}
.lang-toggle{position:fixed;top:20px;left:20px;z-index:50;display:flex;gap:6px;background:var(--card);backdrop-filter:blur(28px) saturate(160%);border:1px solid var(--border);border-radius:10px;padding:4px}
.lang-toggle button{background:none;border:none;color:var(--t3);font-family:inherit;font-size:11px;font-weight:600;padding:4px 10px;border-radius:6px;cursor:pointer;transition:.3s}
.lang-toggle button.active{background:linear-gradient(135deg,#8B5CF6,#6D28D9);color:#0a0714}
.lang-toggle button:hover:not(.active){color:var(--t1)}
@media(max-width:900px){.container{grid-template-columns:1fr}.info-section{display:none}.login-section{padding:32px 24px}}
@media(max-width:480px){.login-section{padding:24px 16px}.welcome{font-size:19px}}
</style>
</head>
<body>
<div class="stars">
    <div class="star" style="width:2px;height:2px;top:10%;left:5%;animation-delay:0s"></div>
    <div class="star" style="width:3px;height:3px;top:20%;left:15%;animation-delay:1s"></div>
    <div class="star" style="width:1px;height:1px;top:30%;left:25%;animation-delay:2s"></div>
    <div class="star" style="width:2px;height:2px;top:15%;left:35%;animation-delay:0.5s"></div>
    <div class="star" style="width:3px;height:3px;top:40%;left:45%;animation-delay:1.5s"></div>
    <div class="star" style="width:1px;height:1px;top:25%;left:55%;animation-delay:2.5s"></div>
    <div class="star" style="width:2px;height:2px;top:50%;left:65%;animation-delay:0.7s"></div>
    <div class="star" style="width:3px;height:3px;top:60%;left:75%;animation-delay:1.8s"></div>
    <div class="star" style="width:1px;height:1px;top:70%;left:85%;animation-delay:2.2s"></div>
    <div class="star" style="width:2px;height:2px;top:80%;left:95%;animation-delay:1.2s"></div>
</div>
<div class="glow-orb orb1"></div><div class="glow-orb orb2"></div>
<div class="lang-toggle">
    <button class="active" onclick="setLang('fa')">🇮🇷 فارسی</button>
    <button onclick="setLang('en')">🇬🇧 English</button>
</div>
<div class="container">
    <div class="login-section">
        <div class="brand"><div class="brand-icon">🏛️</div><div><div class="brand-text">تخت جمشید</div><div class="brand-sub"><span class="live-dot"></span>مدیریت کاربران · آنلاین</div></div></div>
        <div class="welcome" id="welcome-text">خوش آمدید</div>
        <div class="sub-text" id="sub-text">وارد پنل مدیریت شوید</div>
        <div class="error-box" id="error-box"><i class="ti ti-alert-circle"></i><span id="error-text"></span></div>
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="field">
                <label id="label-username">نام کاربری</label>
                <input type="text" id="username" placeholder="نام کاربری را وارد کنید" value="admin" dir="ltr">
            </div>
            <div class="field">
                <label id="label-password">رمز عبور</label>
                <input type="password" id="password" placeholder="رمز عبور را وارد کنید" dir="ltr">
            </div>
            <div class="options"><label><input type="checkbox" id="remember"> <span id="remember-text">مرا به خاطر بسپار</span></label></div>
            <button class="btn-login" type="submit" id="login-btn"><i class="ti ti-login-2"></i> <span id="login-text">ورود</span></button>
        </form>
        <div class="or-divider"><span id="or-text">یا</span></div>
        <button class="connect-btn" onclick="quickConnect()"><i class="ti ti-plug"></i> <span id="connect-text">ورود با یک کلیک</span></button>
    </div>
    <div class="info-section">
        <div class="info-title" id="info-title">🏛️ تخت جمشید</div>
        <div class="info-sub" id="info-sub">سریع‌ترین و امن‌ترین اتصال</div>
        <div class="features">
            <div class="feature"><span class="icon">🔒</span><div class="name" id="f-secure">امن</div><div class="desc" id="f-secure-d">حریم خصوصی شما</div></div>
            <div class="feature"><span class="icon">⚡</span><div class="name" id="f-fast">سریع</div><div class="desc" id="f-fast-d">سرعت برق آسا</div></div>
            <div class="feature"><span class="icon">🌍</span><div class="name" id="f-global">جهانی</div><div class="desc" id="f-global-d">سرورهای جهانی</div></div>
            <div class="feature"><span class="icon">🕵️</span><div class="name" id="f-anon">ناشناس</div><div class="desc" id="f-anon-d">خصوصی بمانید</div></div>
        </div>
    </div>
</div>
<script>
const translations={
fa:{
welcome:"خوش آمدید",
sub:"وارد پنل مدیریت شوید",
username:"نام کاربری",
password:"رمز عبور",
remember:"مرا به خاطر بسپار",
login:"ورود",
or:"یا",
connect:"ورود با یک کلیک",
secure:"امن",
secure_d:"حریم خصوصی شما",
fast:"سریع",
fast_d:"سرعت برق آسا",
global:"جهانی",
global_d:"سرورهای جهانی",
anon:"ناشناس",
anon_d:"خصوصی بمانید",
info_title:"🏛️ تخت جمشید",
info_sub:"سریع‌ترین و امن‌ترین اتصال"
},
en:{
welcome:"Welcome Back",
sub:"Login to panel",
username:"Username",
password:"Password",
remember:"Remember me",
login:"Login",
or:"OR",
connect:"Quick Login",
secure:"Secure",
secure_d:"Your Privacy",
fast:"Fast",
fast_d:"Lightning Speed",
global:"Global",
global_d:"Worldwide Servers",
anon:"Anonymous",
anon_d:"Stay Private",
info_title:"🏛️ Persepolis Panel",
info_sub:"Fastest & Most Secure Connection"
}};
let currentLang=localStorage.getItem('persepolis-lang')||'fa';
const ADMIN_USERNAME="admin";
const ADMIN_PASSWORD="PERSEPOLIS";

function setLang(lang){currentLang=lang;localStorage.setItem('persepolis-lang',lang);document.querySelectorAll('.lang-toggle button').forEach(b=>b.classList.toggle('active',b.textContent.includes(lang==='fa'?'فارسی':'English')));updateTexts()}
function updateTexts(){const t=translations[currentLang];document.getElementById('welcome-text').textContent=t.welcome;document.getElementById('sub-text').textContent=t.sub;document.getElementById('label-username').textContent=t.username;document.getElementById('label-password').textContent=t.password;document.getElementById('remember-text').textContent=t.remember;document.getElementById('login-text').textContent=t.login;document.getElementById('or-text').textContent=t.or;document.getElementById('connect-text').textContent=t.connect;document.getElementById('f-secure').textContent=t.secure;document.getElementById('f-secure-d').textContent=t.secure_d;document.getElementById('f-fast').textContent=t.fast;document.getElementById('f-fast-d').textContent=t.fast_d;document.getElementById('f-global').textContent=t.global;document.getElementById('f-global-d').textContent=t.global_d;document.getElementById('f-anon').textContent=t.anon;document.getElementById('f-anon-d').textContent=t.anon_d;document.getElementById('info-title').textContent=t.info_title;document.getElementById('info-sub').textContent=t.info_sub}

async function handleLogin(e){
e.preventDefault();
const btn=document.getElementById('login-btn');
const err=document.getElementById('error-box');
const errText=document.getElementById('error-text');
err.classList.remove('show');
btn.disabled=true;
btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';

try{
const username=document.getElementById('username').value;
const password=document.getElementById('password').value;
const remember=document.getElementById('remember').checked;

const r=await fetch('/api/login',{
method:'POST',
headers:{'Content-Type':'application/json'},
body:JSON.stringify({username,password,remember})
});

if(!r.ok){
const d=await r.json().catch(()=>({}));
errText.textContent=d.detail||'یوزرنیم یا رمز عبور اشتباه است';
err.classList.add('show');
btn.disabled=false;
btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;
return;
}
window.location.href='/dashboard';
}catch(e){
errText.textContent='خطا در ارتباط با سرور';
err.classList.add('show');
btn.disabled=false;
btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;
}
}

function quickConnect(){
document.getElementById('username').value=ADMIN_USERNAME;
document.getElementById('password').value=ADMIN_PASSWORD;
document.getElementById('remember').checked=true;
document.getElementById('login-form').dispatchEvent(new Event('submit'));
}

document.getElementById('password').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});
document.getElementById('username').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});
setLang(currentLang);
</script>
</body></html>"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏛️ تخت جمشید · خانه</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/plugins/rangePlugin.js"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/l10n/fa.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#08080d;--bg2:#0f0f1a;--bg3:#181828;--card:rgba(10,10,30,0.7);--card-b:rgba(139,92,246,0.08);--card-bh:rgba(139,92,246,0.15);--accent:#8B5CF6;--accent2:#22D3EE;--accent3:#6D28D9;--green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-t:#34D399;--red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-t:#F87171;--amber:#F59E0B;--amber-bg:rgba(245,158,11,0.08);--amber-t:#FCD34D;--t1:#EDEDF7;--t2:#B4AEDD;--t3:#69647F;--sidebar-w:180px;--radius:16px;--shadow:0 8px 32px rgba(0,0,0,0.55),0 0 70px rgba(139,92,246,0.06)}
body{font-family:'Vazirmatn',sans-serif;background:radial-gradient(ellipse 900px 500px at 15% -10%,rgba(139,92,246,0.10),transparent 60%),radial-gradient(ellipse 800px 500px at 100% 10%,rgba(34,211,238,0.06),transparent 55%),var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:13px;position:relative;overflow-x:hidden;transition:background .4s,color .4s}
.stars-bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
.star-bg{position:absolute;border-radius:50%;background:var(--accent2);animation:twinkleBg 4s ease-in-out infinite}
@keyframes twinkleBg{0%,100%{opacity:0.08}50%{opacity:0.3}}
.glow-main{position:fixed;border-radius:50%;filter:blur(200px);z-index:0;pointer-events:none}
.glow-left{width:600px;height:600px;background:rgba(139,92,246,0.02);top:-300px;left:-200px;animation:glowFloat 8s ease-in-out infinite}
.glow-right{width:500px;height:500px;background:rgba(34,211,238,0.02);bottom:-200px;right:-100px;animation:glowFloat 10s ease-in-out infinite reverse}
@keyframes glowFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(50px,-30px) scale(1.1)}}
body.rgb-mode{transition:none}
body.rgb-mode .glow-left{background:var(--glow-1,rgba(139,92,246,0.02));transition:background .1s linear}
body.rgb-mode .glow-right{background:var(--glow-2,rgba(34,211,238,0.02));transition:background .1s linear}
body.rgb-mode .logo-icon{box-shadow:0 0 40px var(--card-bh)}
body.rgb-mode .stat-card:hover,body.rgb-mode .conn-card:hover,body.rgb-mode .stat-mini:hover{box-shadow:0 0 30px var(--card-bh)}
body.rgb-mode .switch.on{box-shadow:0 0 16px var(--card-bh)}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--card);backdrop-filter:blur(40px) saturate(160%);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .4s cubic-bezier(0.34,1.56,0.64,1),background .4s;box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:10px;padding:16px 12px 12px;border-bottom:1px solid var(--card-b)}
.logo-icon{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent3),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;box-shadow:0 0 30px rgba(139,92,246,0.15);animation:pulseLogo 3s ease-in-out infinite}
@keyframes pulseLogo{0%,100%{box-shadow:0 0 30px rgba(139,92,246,0.15)}50%{box-shadow:0 0 50px rgba(139,92,246,0.25)}}
.logo-name{font-size:13px;font-weight:800;background:linear-gradient(135deg,var(--accent2),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo-sub{font-size:7px;color:var(--t3)}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0;position:relative;z-index:1}
.nav-it{display:flex;align-items:center;gap:8px;padding:8px 10px;color:var(--t3);font-size:11px;cursor:pointer;border-right:2px solid transparent;transition:all .3s cubic-bezier(0.34,1.56,0.64,1);margin:1px 4px;border-radius:6px}
.nav-it i{font-size:14px;width:18px;text-align:center;flex-shrink:0;transition:transform .3s}
.nav-it.on i{animation:softPulse 2.2s ease-in-out infinite}
.nav-it:hover{background:rgba(139,92,246,0.05);color:var(--t2)}
.nav-it:hover i{transform:scale(1.1)}
.nav-it.on{background:rgba(139,92,246,0.08);color:var(--t1);border-right-color:var(--accent);font-weight:600;box-shadow:0 0 30px rgba(139,92,246,0.03)}
.nav-it.on i{color:var(--accent)}
.sb-foot{padding:10px 12px;border-top:1px solid var(--card-b)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--red-bg);color:var(--red-t);border-radius:6px;padding:6px;font-size:10px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.1);cursor:pointer;width:100%;transition:.3s}
.logout-btn:hover{background:rgba(239,68,68,0.15);transform:scale(1.02)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:48px;background:var(--card);backdrop-filter:blur(40px) saturate(160%);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 10px;transition:background .4s}
.mob-top .ml{display:flex;align-items:center;gap:6px}
.mob-logo{width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,var(--accent),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:13px}
.mob-title{color:var(--t1);font-size:11px;font-weight:700}
.menu-btn{background:rgba(139,92,246,0.05);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:6px;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.3s}
.menu-btn:hover{background:rgba(139,92,246,0.1);transform:scale(1.05)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:190;backdrop-filter:blur(6px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:16px 20px 80px;min-width:0;transition:margin .4s;position:relative;z-index:1}
.pg{display:none;animation:pageIn .4s cubic-bezier(0.34,1.56,0.64,1)}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(20px) scale(0.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.topbar{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.tb-title{font-size:17px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.tb-title i{animation:softPulse 2.4s ease-in-out infinite;color:var(--accent)}
@keyframes softPulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.15);opacity:.75}}
.tb-title i{color:var(--accent);font-size:19px;animation:titleIcon 3s ease-in-out infinite}
@keyframes titleIcon{0%,100%{transform:rotate(0deg)}50%{transform:rotate(-5deg)}}
.tb-sub{font-size:10px;color:var(--t3);margin-top:1px}
.tb-right{display:flex;align-items:center;gap:5px;flex-wrap:wrap}
.badge{font-size:8px;padding:2px 8px;border-radius:12px;font-weight:700;display:inline-flex;align-items:center;gap:3px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:rgba(139,92,246,0.1);color:var(--accent)}
.bg-fire{background:rgba(139,92,246,0.08);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.dot{width:5px;height:5px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green);animation:dotPulse 1.5s ease-in-out infinite}
.dr{background:var(--red);animation:dotPulse 1.8s ease-in-out infinite}
.da{background:var(--amber);animation:dotPulse 2s ease-in-out infinite}
.db{background:var(--accent);animation:dotPulse 1.2s ease-in-out infinite}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.7)}}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.stats-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-bottom:16px}
.stat-card{background:var(--card);backdrop-filter:blur(28px) saturate(160%);border:1px solid var(--card-b);border-radius:var(--radius);padding:12px 8px;transition:all .4s cubic-bezier(0.34,1.56,0.64,1);text-align:center;position:relative;overflow:hidden}
.stat-card::before{content:'';position:absolute;top:-50%;right:-50%;width:100px;height:100px;background:radial-gradient(circle,rgba(139,92,246,0.03),transparent 70%);pointer-events:none}
.stat-card:hover{border-color:var(--card-bh);transform:translateY(-4px) scale(1.02);box-shadow:var(--shadow)}
.stat-card .icon{font-size:18px;margin-bottom:3px;display:block;animation:emojiFloat2 3.2s ease-in-out infinite}
.stat-card:nth-child(1) .icon{animation-delay:0s}
.stat-card:nth-child(2) .icon{animation-delay:.2s}
.stat-card:nth-child(3) .icon{animation-delay:.4s}
.stat-card:nth-child(4) .icon{animation-delay:.6s}
.stat-card:nth-child(5) .icon{animation-delay:.8s}
.stat-card:nth-child(6) .icon{animation-delay:1s}
@keyframes emojiFloat2{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-3px) rotate(-5deg)}}
.stat-card .number{font-size:18px;font-weight:800;color:var(--t1);line-height:1.2}
.stat-card .number.small{font-size:13px}
.stat-card .label{font-size:9px;color:var(--t3);margin-top:2px;font-weight:500}
.stat-card .sub{font-size:7px;color:var(--t3);margin-top:0px;opacity:.6}

.chart-section{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:16px;margin:12px 0;transition:background .4s}
.chart-section .chart-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px}
.chart-section .chart-title{font-size:13px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:6px}
.chart-section .chart-title i{color:var(--accent)}
.chart-section .chart-sub{font-size:9px;color:var(--t3)}
.chart-section .chart-actions{display:flex;gap:4px;flex-wrap:wrap}

.stat-mini{background:var(--card);border:1px solid var(--card-b);border-radius:8px;padding:8px 12px;display:flex;align-items:center;gap:8px;transition:all .3s cubic-bezier(0.34,1.56,0.64,1)}
.stat-mini:hover{transform:translateY(-2px);border-color:var(--card-bh)}
.stat-mini-icon{font-size:16px;display:inline-block;animation:softPulse 2.8s ease-in-out infinite}
.stat-mini-num{font-size:16px;font-weight:800;color:var(--t1)}
.stat-mini-label{font-size:9px;color:var(--t3)}

.users-table{width:100%;border-collapse:collapse;font-size:12px}
.users-table thead th{padding:10px 12px;text-align:right;color:var(--t2);font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;border-bottom:1px solid var(--card-b);background:rgba(139,92,246,0.02)}
.users-table tbody td{padding:8px 12px;border-bottom:1px solid var(--card-b);color:var(--t1);vertical-align:middle}
.users-table tbody tr{transition:background .3s}
.users-table tbody tr:hover{background:rgba(139,92,246,0.02)}
.users-table .status-badge{display:inline-flex;align-items:center;gap:5px;padding:2px 10px;border-radius:12px;font-size:9px;font-weight:700}
.users-table .status-badge .status-dot{width:6px;height:6px;border-radius:50%;display:inline-block;animation:statusPulse 1.5s ease-in-out infinite}
.users-table .status-badge.active .status-dot{background:var(--green-t)}
.users-table .status-badge.expired .status-dot{background:var(--red-t)}
.users-table .status-badge.disabled .status-dot{background:var(--amber-t)}
@keyframes statusPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.6)}}
.users-table .status-badge.active{background:var(--green-bg);color:var(--green-t)}
.users-table .status-badge.expired{background:var(--red-bg);color:var(--red-t)}
.users-table .status-badge.disabled{background:var(--amber-bg);color:var(--amber-t)}
.users-table .usage-bar{display:flex;align-items:center;gap:6px}
.users-table .usage-bar .bar{width:80px;height:5px;border-radius:4px;background:rgba(139,92,246,0.06);overflow:hidden;box-shadow:inset 0 0 4px rgba(0,0,0,0.3)}
.users-table .usage-bar .bar .fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#FF3CAC,#784BA0,#2B86C5,#22D3EE,#8B5CF6,#FF3CAC);background-size:300% 100%;animation:rgbBarFlow 5s linear infinite;box-shadow:0 0 8px rgba(139,92,246,.55);transition:width .8s cubic-bezier(0.34,1.56,0.64,1)}
@keyframes rgbBarFlow{0%{background-position:0% 50%}100%{background-position:300% 50%}}
.users-table .usage-text{font-size:9px;color:var(--t2);white-space:nowrap}
.users-table .duration-bar{display:flex;flex-direction:column;gap:3px;min-width:64px}
.users-table .duration-bar .bar{width:64px;height:5px;border-radius:4px;background:rgba(139,92,246,0.06);overflow:hidden;box-shadow:inset 0 0 4px rgba(0,0,0,0.3)}
.users-table .duration-bar .bar .fill{height:100%;border-radius:4px;background:linear-gradient(90deg,#FF3CAC,#784BA0,#2B86C5,#22D3EE,#8B5CF6,#FF3CAC);background-size:300% 100%;animation:rgbBarFlow 5s linear infinite;box-shadow:0 0 8px rgba(139,92,246,.55);transition:width .8s cubic-bezier(0.34,1.56,0.64,1)}
.users-table .duration-text{font-size:9px;color:var(--t2);white-space:nowrap}
.users-table .duration-text.warn{color:var(--amber-t)}
.users-table .duration-text.crit{color:var(--red-t)}
.users-table .action-btns{display:flex;gap:3px;justify-content:center;flex-wrap:wrap}
.users-table .action-btns .btn{padding:2px 6px;font-size:8px;border-radius:4px}
.user-name-cell{display:flex;align-items:center;gap:6px}
.user-name-cell .avatar{width:24px;height:24px;border-radius:6px;background:linear-gradient(135deg,var(--accent),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:10px;color:#0a0714;flex-shrink:0;transition:transform .3s;animation:softPulse 2.6s ease-in-out infinite}
.user-name-cell:hover .avatar{transform:scale(1.1) rotate(-5deg)}
.user-name-cell .name{font-weight:600;color:var(--t1)}
.user-name-cell .uuid-short{font-size:7px;color:var(--t3);font-family:monospace}

.btn{font-family:inherit;font-size:10px;font-weight:600;border-radius:6px;padding:5px 10px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:all .3s cubic-bezier(0.34,1.56,0.64,1);white-space:nowrap}
.btn i{font-size:11px;transition:transform .3s}
.btn:hover i{transform:scale(1.1)}
.btn-p{background:linear-gradient(135deg,var(--accent),var(--accent3),var(--accent2));background-size:200% 200%;animation:btnGradient 4s ease infinite;color:#0a0714;box-shadow:0 3px 15px rgba(139,92,246,.2)}
@keyframes btnGradient{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(139,92,246,.3)}
.btn-o{background:rgba(255,255,255,0.02);border:1px solid var(--card-b);color:var(--t2)}
.btn-o:hover{background:rgba(139,92,246,0.05);transform:translateY(-1px)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.1)}
.btn-d:hover{background:rgba(239,68,68,.15);transform:translateY(-1px)}
.btn-pur{background:rgba(139,92,246,0.08);color:var(--accent);border:1px solid rgba(139,92,246,.1)}
.btn-pur:hover{background:rgba(139,92,246,0.15);transform:translateY(-1px)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,0.1)}
.btn-amber:hover{background:rgba(245,158,11,0.15);transform:translateY(-1px)}
.btn-sm{padding:2px 6px;font-size:8px;border-radius:4px}
.btn-icon{width:22px;height:22px;padding:0;justify-content:center}
.btn-generate{background:rgba(139,92,246,0.08);color:var(--accent);border:1px solid rgba(139,92,246,0.1);padding:6px 10px;flex-shrink:0}
.btn-generate:hover{background:rgba(139,92,246,0.15);transform:scale(1.05)}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(8px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);backdrop-filter:blur(40px) saturate(160%);border:1px solid var(--card-b);border-radius:14px;padding:20px 18px;max-width:560px;width:calc(100% - 20px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .4s cubic-bezier(0.34,1.56,0.64,1);box-shadow:var(--shadow)}
@keyframes modalIn{from{opacity:0;transform:scale(0.9) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-close{position:absolute;top:10px;left:10px;background:rgba(139,92,246,0.05);border:1px solid var(--card-b);color:var(--t2);width:24px;height:24px;border-radius:6px;font-size:12px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.3s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg)}
.modal-title{font-size:14px;font-weight:700;color:var(--t1);margin-bottom:12px;display:flex;align-items:center;gap:6px}
.modal-title i{animation:softPulse 2s ease-in-out infinite;color:var(--accent)}
.modal-title i{color:var(--accent);font-size:15px}
.fg{display:flex;flex-direction:column;gap:2px;margin-bottom:8px}
.fg label{font-size:8px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em;display:flex;align-items:center;gap:3px}
.fi{width:100%;padding:6px 10px;border-radius:6px;border:1px solid var(--card-b);background:rgba(0,0,20,.2);color:var(--t1);font-family:inherit;font-size:10px;outline:none;transition:.3s}
.fi-rgb{position:relative}
.fi-rgb::after{content:'';position:absolute;left:0;right:0;bottom:-3px;height:3px;border-radius:3px;background:linear-gradient(90deg,#FF3CAC,#784BA0,#2B86C5,#22D3EE,#8B5CF6,#FF3CAC);background-size:300% 100%;animation:rgbBarFlow 5s linear infinite;box-shadow:0 0 8px rgba(139,92,246,.55)}
.fi:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(139,92,246,.06)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer}
.fi-date{color:var(--t1);background:rgba(0,0,20,.2);border:1px solid var(--card-b);border-radius:6px;padding:6px 10px;width:100%;font-family:inherit;font-size:10px;outline:none;transition:.3s;cursor:pointer}
.fi-date:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(139,92,246,.06)}
.fi-date::placeholder{color:var(--t3)}
.fg-row{display:flex;gap:6px;align-items:center}
.fg-row .fg{flex:1}

.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}
.conn-card{background:var(--card);backdrop-filter:blur(28px) saturate(160%);border:1px solid var(--card-b);border-radius:10px;padding:10px 12px;transition:.3s}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.conn-card .ip{font-family:monospace;font-size:11px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:4px}
.conn-card .label{font-size:8px;color:var(--t3);margin-top:1px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:4px;font-size:8px;color:var(--t2);gap:3px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:5px;height:5px;border-radius:50%;background:#34D399;animation:pulse 1.5s infinite;margin-left:3px}

.settings-card{background:var(--card);backdrop-filter:blur(28px) saturate(160%);border:1px solid var(--card-b);border-radius:var(--radius);padding:14px 16px;max-width:480px;margin-bottom:10px;position:relative;overflow:hidden;transition:all .3s}
.settings-card:hover{border-color:var(--card-bh)}
.settings-card::before{content:'';position:absolute;top:-50%;right:-50%;width:150px;height:150px;background:radial-gradient(circle,rgba(139,92,246,0.02),transparent 70%);pointer-events:none}
.settings-card .title{font-size:13px;font-weight:700;color:var(--t1);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.settings-card .title i{color:var(--accent)}
.settings-card .field{margin-bottom:8px}
.settings-card .field label{font-size:9px;color:var(--t3);display:block;margin-bottom:2px;font-weight:600}
.settings-card .field input{width:100%;padding:6px 10px;border-radius:6px;border:1px solid var(--card-b);background:rgba(0,0,20,.2);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:.3s}
.settings-card .field input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(139,92,246,.06)}
.settings-card .btn{width:100%;justify-content:center;margin-top:3px;font-size:11px;padding:6px}
.settings-card .toggle-row{display:flex;align-items:center;justify-content:space-between;padding:8px 0;border-bottom:1px solid var(--card-b)}
.settings-card .toggle-row .toggle-label{font-size:11px;color:var(--t2);display:flex;align-items:center;gap:5px}
.switch{position:relative;width:36px;height:20px;background:var(--t3);border-radius:10px;cursor:pointer;transition:.4s;flex-shrink:0}
.switch.on{background:linear-gradient(135deg,var(--accent),var(--accent3))}
.switch .slider{position:absolute;top:2px;right:2px;width:16px;height:16px;background:#0a0714;border-radius:50%;transition:.4s cubic-bezier(0.34,1.56,0.64,1);box-shadow:0 2px 4px rgba(0,0,0,0.2)}
.switch.on .slider{right:18px}

.toast{position:fixed;bottom:70px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--card);backdrop-filter:blur(40px) saturate(160%);border:1px solid var(--card-b);color:var(--t1);border-radius:8px;padding:8px 16px;font-size:11px;opacity:0;transition:all .4s cubic-bezier(0.34,1.56,0.64,1);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:5px}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.2);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.2);background:var(--red-bg);color:var(--red-t)}
.toast.warn{border-color:rgba(245,158,11,.2);background:var(--amber-bg);color:var(--amber-t)}

.empty{text-align:center;padding:30px 15px;color:var(--t3)}
.empty i{font-size:28px;opacity:.3;display:block;margin-bottom:6px}
.empty p{font-size:10px}

.bottom-nav{display:none;position:fixed;bottom:0;right:0;left:0;background:var(--card);backdrop-filter:blur(40px) saturate(160%);border-top:1px solid var(--card-b);z-index:300;padding:4px 2px 6px;justify-content:space-around;align-items:center}
.bottom-nav .nav-item{display:flex;flex-direction:column;align-items:center;gap:1px;color:var(--t3);font-size:7px;cursor:pointer;padding:3px 6px;border-radius:6px;transition:all .3s;border:none;background:none;font-family:inherit;min-width:40px;position:relative}
.bottom-nav .nav-item i{font-size:16px;transition:all .3s}
.bottom-nav .nav-item:hover{color:var(--t2);transform:translateY(-2px)}
.bottom-nav .nav-item.active{color:var(--accent)}
.bottom-nav .nav-item.active i{transform:scale(1.1)}
.bottom-nav .nav-item .notif-dot{position:absolute;top:0;right:0;width:6px;height:6px;background:var(--red);border-radius:50%;animation:pulse 1.5s infinite}

@media(max-width:768px){.bottom-nav{display:flex !important}.main{padding-bottom:65px !important;margin-right:0 !important;padding-top:55px !important}.sidebar{transform:translateX(100%);padding-bottom:60px}.sidebar.open{transform:translateX(0)}.mob-top{display:flex}.stats-grid{grid-template-columns:repeat(3,1fr)}.stat-mini{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.stats-grid{grid-template-columns:1fr 1fr}.main{padding:50px 8px 65px}.bottom-nav .nav-item{min-width:32px;padding:2px 4px}.bottom-nav .nav-item i{font-size:14px}.bottom-nav .nav-item span{font-size:6px}.users-table thead th{font-size:7px;padding:6px 4px}.users-table tbody td{font-size:9px;padding:6px 4px}.users-table .usage-bar .bar{width:40px}.stat-mini{padding:6px 8px}.stat-mini-num{font-size:13px}}
@media(min-width:769px){.bottom-nav{display:none !important}}

body.light-theme{--bg:#f0f0f5;--bg2:#e8e8f0;--bg3:#dddde8;--card:rgba(255,255,255,0.85);--card-b:rgba(139,92,246,0.12);--card-bh:rgba(139,92,246,0.2);--t1:#1a1a2e;--t2:#4a4a6a;--t3:#7a7a9a;--shadow:0 8px 32px rgba(0,0,0,0.08),0 0 60px rgba(139,92,246,0.02)}
body.light-theme .stars-bg .star-bg{background:#8888BB}
body.light-theme .glow-main{display:none}
body.light-theme .stat-card::before{background:radial-gradient(circle,rgba(139,92,246,0.05),transparent 70%)}
body.light-theme .fi{background:rgba(255,255,255,0.7)}
body.light-theme .btn-o{background:rgba(0,0,0,0.03);border-color:rgba(139,92,246,0.1);color:var(--t2)}
body.light-theme .btn-o:hover{background:rgba(139,92,246,0.06)}
body.light-theme .users-table thead th{background:rgba(139,92,246,0.03)}
body.light-theme .users-table tbody tr:hover{background:rgba(139,92,246,0.03)}
body.light-theme .stat-mini{background:rgba(255,255,255,0.8)}
body.light-theme .conn-card{background:rgba(255,255,255,0.8)}
body.light-theme .settings-card{background:rgba(255,255,255,0.8)}
body.light-theme .chart-section{background:rgba(255,255,255,0.8)}

/* استایل‌های تقویم Flatpickr */
.flatpickr-calendar{background:var(--card) !important;backdrop-filter:blur(40px) saturate(160%) !important;border:1px solid var(--card-b) !important;border-radius:12px !important;box-shadow:var(--shadow) !important}
.flatpickr-calendar .flatpickr-months .flatpickr-month{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-weekday{color:var(--t2) !important}
.flatpickr-calendar .flatpickr-day{color:var(--t1) !important;border-radius:6px !important}
.flatpickr-calendar .flatpickr-day:hover{background:rgba(139,92,246,0.1) !important}
.flatpickr-calendar .flatpickr-day.selected{background:linear-gradient(135deg,var(--accent),var(--accent3)) !important;color:#0a0714 !important;border-color:var(--accent) !important}
.flatpickr-calendar .flatpickr-day.today{border-color:var(--accent) !important}
.flatpickr-calendar .flatpickr-day.inRange{background:rgba(139,92,246,0.08) !important}
.flatpickr-calendar .flatpickr-day.startRange,.flatpickr-calendar .flatpickr-day.endRange{background:linear-gradient(135deg,var(--accent),var(--accent3)) !important;color:#0a0714 !important}
.flatpickr-calendar .flatpickr-day.disabled{color:var(--t3) !important}
.flatpickr-calendar .flatpickr-current-month .flatpickr-monthDropdown-months{color:var(--t1) !important;background:transparent !important}
.flatpickr-calendar .flatpickr-current-month input.cur-year{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-prev-month,.flatpickr-calendar .flatpickr-next-month{color:var(--t3) !important}
.flatpickr-calendar .flatpickr-prev-month:hover,.flatpickr-calendar .flatpickr-next-month:hover{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-rContainer .flatpickr-weekdays{background:transparent !important}
.flatpickr-time{background:var(--card) !important;border-top:1px solid var(--card-b) !important;border-radius:0 0 12px 12px !important}
.flatpickr-time input{color:var(--t1) !important}
.flatpickr-time .flatpickr-time-separator{color:var(--t3) !important}
.flatpickr-time .numInputWrapper:hover{background:rgba(139,92,246,0.05) !important}
</style>
</head>
<body>
<div class="stars-bg">
    <div class="star-bg" style="width:2px;height:2px;top:5%;left:10%;animation-delay:0s"></div>
    <div class="star-bg" style="width:3px;height:3px;top:15%;left:30%;animation-delay:1.5s"></div>
    <div class="star-bg" style="width:1px;height:1px;top:25%;left:50%;animation-delay:0.8s"></div>
    <div class="star-bg" style="width:2px;height:2px;top:40%;left:70%;animation-delay:2.2s"></div>
    <div class="star-bg" style="width:3px;height:3px;top:55%;left:15%;animation-delay:0.5s"></div>
    <div class="star-bg" style="width:1px;height:1px;top:70%;left:85%;animation-delay:1.8s"></div>
    <div class="star-bg" style="width:2px;height:2px;top:85%;left:40%;animation-delay:2.5s"></div>
</div>
<div class="glow-main glow-left"></div><div class="glow-main glow-right"></div>
<div class="toast" id="toast"></div>

<!-- Modal User -->
<div class="modal-bg" id="modal-user">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> <span id="modal-user-title">ساخت کاربر جدید</span></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;position:relative;">
        <label><i class="ti ti-tag"></i> <span id="f-label-name">نام کاربری</span></label>
        <div style="display:flex;gap:4px;">
          <input class="fi" id="user-label" placeholder="مثلاً: علی" value="کاربر" style="flex:1">
          <button class="btn btn-generate btn-sm" onclick="generateRandomUsername()" title="ساخت نام تصادفی" style="padding:6px 10px;flex-shrink:0;">
            <i class="ti ti-dice"></i>
          </button>
        </div>
      </div>
      <div class="fg"><label><i class="ti ti-database"></i> <span id="f-label-quota">حجم (GB)</span></label><div class="fi-rgb"><input class="fi" id="user-quota" type="number" min="0.5" step="0.5" value="2"></div></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> <span id="f-label-expiry">انقضا</span></label>
        <input class="fi-date" id="user-expiry-date" type="text" placeholder="انتخاب تاریخ">
      </div>
      <div class="fg"><label><i class="ti ti-devices"></i> <span id="f-label-devices">دستگاه</span></label><input class="fi" id="user-devices" type="number" min="0" max="10" value="1"></div>
    </div>
    <div class="fg"><label><i class="ti ti-fingerprint"></i> <span id="f-label-fingerprint">انگشت‌نگاری</span></label>
      <select class="fi" id="user-fingerprint">
        <option value="chrome">🌐 Chrome</option><option value="firefox">🦊 Firefox</option>
        <option value="safari">🧭 Safari</option><option value="edge">🌊 Edge</option>
        <option value="ios">📱 iOS</option><option value="android">🤖 Android</option>
        <option value="safari_ios">🍏 Safari iOS</option><option value="random">🎲 Random</option><option value="none">🚫 None</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-settings"></i> <span id="f-label-protocol">پروتکل</span></label>
      <select class="fi" id="user-protocol">
        <option value="vless-ws">🚀 VLESS-WS</option>
        <option value="vless-grpc">⚡ VLESS-gRPC</option>
        <option value="vless-xhttp">🛡️ VLESS-XHTTP</option>
        <option value="vless-http2">📶 VLESS-HTTP/2</option>
        <option value="trojan-ws">🔒 Trojan-WS</option>
        <option value="shadowsocks">🌊 Shadowsocks</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-cloud"></i> <span id="f-label-http">HTTP نسخه</span></label>
      <select class="fi" id="user-http">
        <option value="h2">🚀 HTTP/2</option>
        <option value="h3">⚡ HTTP/3 (QUIC)</option>
        <option value="h1">📶 HTTP/1.1</option>
        <option value="auto">🔄 Auto</option>
      </select>
    </div>
    <div class="fg"><label><i class="ti ti-lock"></i> <span id="f-label-password">رمز (اختیاری)</span></label><input class="fi" id="user-password" type="password" placeholder="برای ویرایش/حذف" dir="ltr"></div>
    <div style="display:flex;gap:6px;margin-top:10px"><button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> <span id="btn-create-user">ساخت کاربر</span></button><button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1"><span id="btn-cancel">انصراف</span></button></div>
  </div>
</div>

<!-- Modal Edit -->
<div class="modal-bg" id="modal-edit">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> <span id="modal-edit-title">ویرایش کاربر</span></div>
    <input type="hidden" id="edit-uuid">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;"><label><i class="ti ti-tag"></i> <span id="e-label-name">نام</span></label><input class="fi" id="edit-label" placeholder="نام کاربری"></div>
      <div class="fg" id="edit-password-section"><label><i class="ti ti-lock"></i> <span id="e-label-password">رمز جدید</span></label><input class="fi" id="edit-password" type="password" placeholder="برای تغییر" dir="ltr"></div>
      <div class="fg"><label><i class="ti ti-database"></i> <span id="e-label-quota">حجم (GB)</span></label><div class="fi-rgb"><input class="fi" id="edit-quota" type="number" min="0" step="0.5"></div></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> <span id="e-label-expiry">انقضا</span></label>
        <input class="fi-date" id="edit-expiry-date" type="text" placeholder="انتخاب تاریخ">
      </div>
      <div class="fg"><label><i class="ti ti-devices"></i> <span id="e-label-devices">دستگاه</span></label><input class="fi" id="edit-devices" type="number" min="0" max="10"></div>
      <div class="fg"><label><i class="ti ti-toggle-left"></i> <span id="e-label-status">وضعیت</span></label><select class="fi" id="edit-status"><option value="true">✅ فعال</option><option value="false">❌ غیرفعال</option></select></div>
    </div>
    <div class="fg"><label><i class="ti ti-fingerprint"></i> <span id="e-label-fingerprint">انگشت‌نگاری</span></label>
      <select class="fi" id="edit-fingerprint">
        <option value="chrome">🌐 Chrome</option><option value="firefox">🦊 Firefox</option>
        <option value="safari">🧭 Safari</option><option value="edge">🌊 Edge</option>
        <option value="ios">📱 iOS</option><option value="android">🤖 Android</option>
        <option value="safari_ios">🍏 Safari iOS</option><option value="random">🎲 Random</option><option value="none">🚫 None</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-settings"></i> <span id="e-label-protocol">پروتکل</span></label>
      <select class="fi" id="edit-protocol">
        <option value="vless-ws">🚀 VLESS-WS</option>
        <option value="vless-grpc">⚡ VLESS-gRPC</option>
        <option value="vless-xhttp">🛡️ VLESS-XHTTP</option>
        <option value="vless-http2">📶 VLESS-HTTP/2</option>
        <option value="trojan-ws">🔒 Trojan-WS</option>
        <option value="shadowsocks">🌊 Shadowsocks</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-cloud"></i> <span id="e-label-http">HTTP نسخه</span></label>
      <select class="fi" id="edit-http">
        <option value="h2">🚀 HTTP/2</option>
        <option value="h3">⚡ HTTP/3 (QUIC)</option>
        <option value="h1">📶 HTTP/1.1</option>
        <option value="auto">🔄 Auto</option>
      </select>
    </div>
    <div style="display:flex;gap:6px;margin-top:10px"><button class="btn btn-p" onclick="saveEdit()" style="flex:2"><i class="ti ti-check"></i> <span id="btn-save">ذخیره</span></button><button class="btn btn-o" onclick="closeModal('modal-edit')" style="flex:1"><span id="btn-cancel2">انصراف</span></button></div>
  </div>
</div>

<!-- Modal Delete -->
<div class="modal-bg" id="modal-delete">
  <div class="modal" style="max-width:340px">
    <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-trash"></i> <span id="modal-delete-title">حذف کاربر</span></div>
    <input type="hidden" id="delete-uuid">
    <p style="font-size:10px;color:var(--t2);margin-bottom:10px" id="delete-desc">برای حذف، رمز کانفیگ را وارد کنید.</p>
    <div class="fg"><label><i class="ti ti-lock"></i> <span id="d-label-password">رمز</span></label><input class="fi" id="delete-password" type="password" placeholder="رمز کانفیگ" dir="ltr"></div>
    <div style="display:flex;gap:6px;margin-top:10px"><button class="btn btn-d" onclick="confirmDelete()" style="flex:2"><i class="ti ti-trash"></i> <span id="btn-delete">حذف</span></button><button class="btn btn-o" onclick="closeModal('modal-delete')" style="flex:1"><span id="btn-cancel3">انصراف</span></button></div>
  </div>
</div>

<!-- Modal QR Code -->
<div class="modal-bg" id="modal-qr">
  <div class="modal" style="max-width:400px;text-align:center">
    <button class="modal-close" onclick="closeModal('modal-qr')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-qrcode"></i> <span id="qr-title">QR Code</span></div>
    <div id="qrcode-container" style="display:flex;justify-content:center;padding:10px 0;"></div>
    <p style="font-size:9px;color:var(--t3);margin-top:4px" id="qr-desc">اسکن کنید تا ساب‌لینک اضافه شود</p>
    <button class="btn btn-p btn-sm" onclick="downloadQR()" style="margin-top:6px"><i class="ti ti-download"></i> <span id="qr-download">دانلود QR</span></button>
  </div>
</div>

<div class="mob-top">
  <div class="ml"><div class="mob-logo">🏛️</div><span class="mob-title">تخت جمشید</span></div>
  <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
</div>
<div class="overlay" id="overlay"></div>

<aside class="sidebar" id="sb">
  <div class="logo"><div class="logo-icon">🏛️</div><div><div class="logo-name">تخت جمشید</div><div class="logo-sub">مدیریت کاربران</div></div></div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="dashboard"><i class="ti ti-layout-dashboard"></i> <span id="nav-home">خانه</span></div>
    <div class="nav-it" data-pg="users"><i class="ti ti-users"></i> <span id="nav-users">کاربران</span></div>
    <div class="nav-it" data-pg="inbound"><i class="ti ti-plug"></i> <span id="nav-inbound">اینباند</span></div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> <span id="nav-connections">اتصالات</span></div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> <span id="nav-settings">تنظیمات</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-notes"></i> <span id="nav-logs">لاگ‌ها</span></div>
    <div class="nav-it" data-pg="backup"><i class="ti ti-database"></i> <span id="nav-backup">بکاپ</span></div>
  </div>
  <div class="sb-foot"><button class="logout-btn" onclick="logout()"><i class="ti ti-logout"></i> <span id="nav-logout">خروج</span></button></div>
</aside>

<div class="bottom-nav" id="bottomNav">
  <button class="nav-item active" data-pg="dashboard" onclick="navTo('dashboard')"><i class="ti ti-layout-dashboard"></i><span id="b-home">خانه</span></button>
  <button class="nav-item" data-pg="users" onclick="navTo('users')"><i class="ti ti-users"></i><span id="b-users">کاربران</span></button>
  <button class="nav-item" data-pg="inbound" onclick="navTo('inbound')"><i class="ti ti-plug"></i><span id="b-inbound">اینباند</span></button>
  <button class="nav-item" data-pg="settings" onclick="navTo('settings')"><i class="ti ti-settings"></i><span id="b-settings">تنظیمات</span></button>
</div>

<main class="main">
<!-- صفحه خانه -->
<section class="pg on" id="pg-dashboard">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> <span id="dash-title">خانه</span></div><div class="tb-sub" id="last-update">بروزرسانی: لحظه‌ای</div></div>
    <div class="tb-right">
      <span class="badge bg-fire" id="online-badge"><span class="dot dg"></span> ۰ آنلاین</span>
      <button class="btn btn-p btn-sm" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> <span id="dash-add-user">کاربر</span></button>
    </div>
  </div>
  
  <div class="stats-grid">
    <div class="stat-card"><span class="icon">📊</span><div class="number" id="stat-traffic">۰</div><div class="label" id="s-traffic">ترافیک</div><div class="sub">MB</div></div>
    <div class="stat-card"><span class="icon">📨</span><div class="number" id="stat-requests">۰</div><div class="label" id="s-requests">درخواست‌ها</div><div class="sub" id="s-count">تعداد</div></div>
    <div class="stat-card"><span class="icon">⏱️</span><div class="number" id="stat-uptime">۰۰:۰۰:۰۰</div><div class="label" id="s-uptime">آپتایم</div><div class="sub" id="s-time">زمان</div></div>
    <div class="stat-card"><span class="icon">💾</span><div class="number small" id="stat-disk">۰ GB</div><div class="label" id="s-disk">فضای دیسک</div><div class="sub" id="stat-disk-used">استفاده</div></div>
    <div class="stat-card"><span class="icon">📶</span><div class="number small" id="stat-speed">۰ B/s</div><div class="label" id="s-speed">سرعت</div><div class="sub" id="s-live">لحظه‌ای</div></div>
    <div class="stat-card"><span class="icon">👥</span><div class="number" id="stat-users">۰</div><div class="label" id="s-users">کاربران</div><div class="sub" id="stat-users-active">۰ فعال</div></div>
  </div>

  <!-- نمودار مصرف -->
  <div class="chart-section">
    <div class="chart-header">
      <div>
        <span class="chart-title"><i class="ti ti-chart-bar"></i> <span id="chart-title-text">مصرف روزانه</span></span>
        <span class="chart-sub" id="chart-sub-text">آخرین ۷ روز</span>
      </div>
      <div class="chart-actions">
        <button class="btn btn-sm btn-pur" onclick="loadChart('7d')" id="chart-7d">۷ روز</button>
        <button class="btn btn-sm btn-o" onclick="loadChart('30d')" id="chart-30d">۳۰ روز</button>
        <button class="btn btn-sm btn-o" onclick="loadChart('90d')" id="chart-90d">۹۰ روز</button>
      </div>
    </div>
    <div style="position:relative;height:180px;width:100%">
      <canvas id="trafficChart"></canvas>
    </div>
  </div>

  <div style="background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:10px 12px;margin-top:4px;transition:background .4s">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
      <span style="font-size:11px;font-weight:700;color:var(--t1)">🆕 <span id="recent-users-title">کاربران اخیر</span></span>
      <button class="btn btn-sm btn-o" onclick="loadDashboard()"><i class="ti ti-refresh"></i></button>
    </div>
    <div id="recent-users" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:4px"></div>
  </div>
</section>

<!-- صفحه کاربران -->
<section class="pg" id="pg-users">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-users"></i> <span id="users-title">کاربران</span></div><div class="tb-sub" id="users-sub">لیست کانفیگ‌ها، سهمیه و انقضا</div></div><div class="tb-right"><button class="btn btn-o btn-sm" onclick="loadUsers()"><i class="ti ti-refresh"></i></button></div></div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px;">
    <div class="stat-mini"><span class="stat-mini-icon">👥</span><span class="stat-mini-num" id="users-total">0</span><span class="stat-mini-label" id="u-total">کل کاربران</span></div>
    <div class="stat-mini"><span class="stat-mini-icon">🟢</span><span class="stat-mini-num" id="users-active">0</span><span class="stat-mini-label" id="u-active">فعال</span></div>
    <div class="stat-mini"><span class="stat-mini-icon">🔴</span><span class="stat-mini-num" id="users-expired">0</span><span class="stat-mini-label" id="u-expired">منقضی</span></div>
    <div class="stat-mini"><span class="stat-mini-icon">📊</span><span class="stat-mini-num" id="users-traffic">0</span><span class="stat-mini-label" id="u-traffic">مصرف کل</span></div>
  </div>
  <div style="background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);overflow:hidden;backdrop-filter:blur(28px) saturate(160%);transition:background .4s">
    <div style="overflow-x:auto;"><table class="users-table" id="users-table"><thead><tr><th id="th-name">نام</th><th id="th-account">اکانت</th><th id="th-status">وضعیت</th><th id="th-usage">مصرف دیتا</th><th id="th-duration">مدت</th><th style="text-align:center;" id="th-actions">عملیات</th></tr></thead><tbody id="users-tbody"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);" id="no-users">هیچ کاربری وجود ندارد</td></tr></tbody></table></div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:10px 14px;border-top:1px solid var(--card-b);flex-wrap:wrap;gap:8px;"><div style="font-size:9px;color:var(--t3);"><span id="users-count-label">۰ کاربر</span></div><div style="display:flex;gap:6px;"><button class="btn btn-p btn-sm" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> <span id="add-user-btn">افزودن کاربر جدید</span></button></div></div>
  </div>
</section>

<!-- صفحه اینباند -->
<section class="pg" id="pg-inbound">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-plug"></i> <span id="inbound-title">اینباند</span></div><div class="tb-sub" id="inbound-sub">تنظیمات ورودی</div></div></div>
  <div style="background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:12px 14px;margin-bottom:10px;transition:background .4s">
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">
      <div style="text-align:center"><div style="font-size:14px;font-weight:700;color:var(--t1)" id="inbound-port">۴۴۳</div><div style="font-size:8px;color:var(--t3)" id="inb-port-label">پورت</div></div>
      <div style="text-align:center"><div style="font-size:14px;font-weight:700;color:var(--t1)" id="inbound-protocol">VLESS-WS</div><div style="font-size:8px;color:var(--t3)" id="inb-protocol-label">پروتکل</div></div>
      <div style="text-align:center"><div style="font-size:12px;font-weight:700;color:var(--t1)" id="inbound-host">—</div><div style="font-size:8px;color:var(--t3)" id="inb-host-label">هاست</div></div>
      <div style="text-align:center"><div style="font-size:14px;font-weight:700;color:#34D399">✅ <span id="inb-status-label">فعال</span></div><div style="font-size:8px;color:var(--t3)" id="inb-status-title">وضعیت</div></div>
    </div>
  </div>
</section>

<!-- صفحه اتصالات -->
<section class="pg" id="pg-connections">
  <div class="topbar"><div><div class="tb-title">🔌 <span id="conn-title">اتصالات</span></div><div class="tb-sub" id="conn-count">۰ اتصال</div></div><div class="tb-right"><span class="badge bg-green"><span class="dot dg pulse"></span> <span id="conn-active-label">فعال</span></span><button class="btn btn-sm btn-o" onclick="loadConnections()"><i class="ti ti-refresh"></i></button></div></div>
  <div id="conns-grid" class="conn-grid"><div class="empty"><i class="ti ti-plug-off"></i><p id="no-conn">هیچ اتصالی وجود ندارد</p></div></div>
</section>

<!-- صفحه تنظیمات -->
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> <span id="settings-title">تنظیمات</span></div><div class="tb-sub" id="settings-sub">مدیریت پنل</div></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-color-swatch"></i> <span id="set-theme-title">تم پنل</span></div><div style="display:flex;gap:8px;margin-top:4px;"><button class="btn" onclick="setTheme('dark')" id="theme-dark-btn" style="flex:1;font-size:11px;padding:6px 12px;background:var(--card);border:1px solid var(--card-b);color:var(--t1);transition:all .3s">🌙 <span id="set-dark">تاریک</span></button><button class="btn" onclick="setTheme('light')" id="theme-light-btn" style="flex:1;font-size:11px;padding:6px 12px;background:var(--card);border:1px solid var(--card-b);color:var(--t1);transition:all .3s">☀️ <span id="set-light">روشن</span></button></div><div style="font-size:9px;color:var(--t3);margin-top:6px;">💡 <span id="set-current-theme">تم فعلی</span>: <span id="current-theme-label">تاریک</span></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-language"></i> <span id="set-lang-title">زبان پنل</span></div><div style="display:flex;gap:6px;margin-top:4px"><button class="btn btn-pur" onclick="setLang('fa')" style="flex:1;font-size:11px;padding:6px 12px" id="lang-fa-btn">🇮🇷 فارسی</button><button class="btn btn-o" onclick="setLang('en')" style="flex:1;font-size:11px;padding:6px 12px" id="lang-en-btn">🇬🇧 English</button></div><div style="font-size:9px;color:var(--t3);margin-top:6px">💡 <span id="set-current-lang">زبان فعلی</span>: <span id="current-lang-label">فارسی</span></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-color-swatch"></i> <span id="set-rgb-title">تم RGB</span></div><div class="toggle-row" style="border-bottom:none"><div class="toggle-label"><i class="ti ti-color-palette" style="background:linear-gradient(135deg,#ff0000,#00ff00,#0000ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent"></i> RGB</div><div class="switch" id="rgb-switch" onclick="toggleRGB()"><div class="slider"></div></div></div><div style="font-size:9px;color:var(--t3);margin-top:2px">🌈 وقتی روشنه، رنگ‌بندی کل پنل به‌آرومی مثل نور RGB می‌چرخه</div></div>

  <div class="settings-card" style="max-width:480px">
    <div class="title"><i class="ti ti-lock"></i> تغییر نام کاربری و رمز عبور</div>
    <div class="field"><label>رمز عبور فعلی</label><input type="password" id="cred-current-pass" placeholder="رمز عبور فعلی خود را وارد کنید" autocomplete="current-password"></div>
    <div class="field"><label>نام کاربری جدید (اختیاری)</label><input type="text" id="cred-new-user" placeholder="خالی بگذارید تا تغییر نکند" autocomplete="off"></div>
    <div class="field"><label>رمز عبور جدید (اختیاری)</label><input type="password" id="cred-new-pass" placeholder="خالی بگذارید تا تغییر نکند" autocomplete="new-password"></div>
    <div class="field"><label>تکرار رمز عبور جدید</label><input type="password" id="cred-new-pass2" placeholder="تکرار رمز عبور جدید" autocomplete="new-password"></div>
    <button class="btn btn-p" onclick="changeCredentials()" id="cred-submit-btn"><i class="ti ti-shield-check"></i> ذخیره تغییرات</button>
    <div style="font-size:9px;color:var(--t3);margin-top:6px">🔒 پس از تغییر، سایر نشست‌های ورود باطل می‌شوند و برای بار بعد باید از اطلاعات جدید استفاده کنید.</div>
  </div>
  
</section>

<!-- صفحه لاگ‌ها -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-notes"></i> <span id="logs-title">لاگ‌ها</span></div><div class="tb-sub" id="logs-count">۰ لاگ</div></div><div class="tb-right"><button class="btn btn-sm btn-o" onclick="loadLogs()"><i class="ti ti-refresh"></i></button></div></div>
  <div style="background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:8px 10px;max-height:400px;overflow-y:auto;transition:background .4s"><div id="logs-container" style="font-family:monospace;font-size:9px;color:var(--t2);direction:ltr;text-align:left;line-height:1.5"></div></div>
</section>

<!-- صفحه بکاپ -->
<section class="pg" id="pg-backup">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-database"></i> <span id="backup-title">بکاپ</span></div><div class="tb-sub" id="backup-sub">ذخیره و بازیابی</div></div></div>
  <div class="settings-card"><div class="title"><i class="ti ti-download"></i> <span id="backup-download-title">بکاپ‌گیری</span></div><div style="display:flex;gap:6px;flex-wrap:wrap"><button class="btn btn-p btn-sm" onclick="createBackup()" style="flex:2"><i class="ti ti-download"></i> <span id="backup-download-btn">دانلود</span></button><button class="btn btn-o btn-sm" onclick="document.getElementById('restore-input').click()" style="flex:1"><i class="ti ti-upload"></i> <span id="backup-restore-btn">بازیابی</span></button><input type="file" id="restore-input" accept=".json" style="display:none" onchange="restoreBackup(event)"></div></div>
</section>
</main>

<script>
// ===== ترجمه‌ها =====
const translations = {
  fa: {
    nav_home: 'خانه', nav_users: 'کاربران', nav_inbound: 'اینباند',
    nav_connections: 'اتصالات', nav_settings: 'تنظیمات', nav_logs: 'لاگ‌ها',
    nav_backup: 'بکاپ', nav_logout: 'خروج',
    dash_title: 'خانه', dash_add_user: 'کاربر',
    s_traffic: 'ترافیک', s_requests: 'درخواست‌ها', s_uptime: 'آپتایم',
    s_disk: 'فضای دیسک', s_speed: 'سرعت', s_users: 'کاربران',
    s_count: 'تعداد', s_time: 'زمان', s_live: 'لحظه‌ای',
    chart_title: 'مصرف روزانه', chart_sub: 'آخرین ۷ روز',
    recent_users: 'کاربران اخیر',
    users_title: 'کاربران', users_sub: 'لیست کانفیگ‌ها، سهمیه و انقضا',
    u_total: 'کل کاربران', u_active: 'فعال', u_expired: 'منقضی', u_traffic: 'مصرف کل',
    th_name: 'نام', th_account: 'اکانت', th_status: 'وضعیت', th_usage: 'مصرف دیتا',
    th_duration: 'مدت', th_actions: 'عملیات',
    add_user_btn: 'افزودن کاربر جدید', no_users: 'هیچ کاربری وجود ندارد',
    inbound_title: 'اینباند', inbound_sub: 'تنظیمات ورودی',
    inb_port: 'پورت', inb_protocol: 'پروتکل', inb_host: 'هاست', inb_status: 'وضعیت',
    conn_title: 'اتصالات', conn_active: 'فعال', no_conn: 'هیچ اتصالی وجود ندارد',
    settings_title: 'تنظیمات', settings_sub: 'مدیریت پنل',
    set_theme: 'تم پنل', set_dark: 'تاریک', set_light: 'روشن',
    set_current_theme: 'تم فعلی', set_lang: 'زبان پنل', set_current_lang: 'زبان فعلی',
    set_rgb: 'تم RGB',
    backup_title: 'بکاپ', backup_sub: 'ذخیره و بازیابی',
    backup_download: 'بکاپ‌گیری', backup_download_btn: 'دانلود', backup_restore_btn: 'بازیابی',
    logs_title: 'لاگ‌ها',
    modal_user_title: 'ساخت کاربر جدید',
    f_label_name: 'نام کاربری', f_label_quota: 'حجم (GB)',
    f_label_expiry: 'انقضا', f_label_devices: 'دستگاه',
    f_label_fingerprint: 'انگشت‌نگاری', f_label_protocol: 'پروتکل',
    f_label_http: 'HTTP نسخه', f_label_password: 'رمز (اختیاری)',
    btn_create_user: 'ساخت کاربر', btn_cancel: 'انصراف',
    modal_edit_title: 'ویرایش کاربر',
    e_label_name: 'نام', e_label_password: 'رمز جدید',
    e_label_quota: 'حجم (GB)', e_label_expiry: 'انقضا',
    e_label_devices: 'دستگاه', e_label_status: 'وضعیت',
    e_label_fingerprint: 'انگشت‌نگاری', e_label_protocol: 'پروتکل',
    e_label_http: 'HTTP نسخه',
    btn_save: 'ذخیره',
    modal_delete_title: 'حذف کاربر', delete_desc: 'برای حذف، رمز کانفیگ را وارد کنید.',
    d_label_password: 'رمز', btn_delete: 'حذف',
    qr_title: 'QR Code', qr_desc: 'اسکن کنید تا ساب‌لینک اضافه شود',
    qr_download: 'دانلود QR'
  },
  en: {
    nav_home: 'Home', nav_users: 'Users', nav_inbound: 'Inbound',
    nav_connections: 'Connections', nav_settings: 'Settings', nav_logs: 'Logs',
    nav_backup: 'Backup', nav_logout: 'Logout',
    dash_title: 'Dashboard', dash_add_user: 'User',
    s_traffic: 'Traffic', s_requests: 'Requests', s_uptime: 'Uptime',
    s_disk: 'Disk', s_speed: 'Speed', s_users: 'Users',
    s_count: 'Count', s_time: 'Time', s_live: 'Live',
    chart_title: 'Daily Usage', chart_sub: 'Last 7 days',
    recent_users: 'Recent Users',
    users_title: 'Users', users_sub: 'Link list, quota and expiry',
    u_total: 'Total Users', u_active: 'Active', u_expired: 'Expired', u_traffic: 'Total Usage',
    th_name: 'Name', th_account: 'Account', th_status: 'Status', th_usage: 'Data Usage',
    th_duration: 'Duration', th_actions: 'Actions',
    add_user_btn: 'Add New User', no_users: 'No users found',
    inbound_title: 'Inbound', inbound_sub: 'Inbound Settings',
    inb_port: 'Port', inb_protocol: 'Protocol', inb_host: 'Host', inb_status: 'Status',
    conn_title: 'Connections', conn_active: 'Active', no_conn: 'No active connections',
    settings_title: 'Settings', settings_sub: 'Panel Settings',
    set_theme: 'Theme', set_dark: 'Dark', set_light: 'Light',
    set_current_theme: 'Current Theme', set_lang: 'Language', set_current_lang: 'Current Language',
    set_rgb: 'RGB Mode',
    backup_title: 'Backup', backup_sub: 'Save & Restore',
    backup_download: 'Backup', backup_download_btn: 'Download', backup_restore_btn: 'Restore',
    logs_title: 'Logs',
    modal_user_title: 'Create New User',
    f_label_name: 'Username', f_label_quota: 'Quota (GB)',
    f_label_expiry: 'Expiry', f_label_devices: 'Devices',
    f_label_fingerprint: 'Fingerprint', f_label_protocol: 'Protocol',
    f_label_http: 'HTTP Version', f_label_password: 'Password (Optional)',
    btn_create_user: 'Create User', btn_cancel: 'Cancel',
    modal_edit_title: 'Edit User',
    e_label_name: 'Name', e_label_password: 'New Password',
    e_label_quota: 'Quota (GB)', e_label_expiry: 'Expiry',
    e_label_devices: 'Devices', e_label_status: 'Status',
    e_label_fingerprint: 'Fingerprint', e_label_protocol: 'Protocol',
    e_label_http: 'HTTP Version',
    btn_save: 'Save',
    modal_delete_title: 'Delete User', delete_desc: 'Enter the config password to delete.',
    d_label_password: 'Password', btn_delete: 'Delete',
    qr_title: 'QR Code', qr_desc: 'Scan to add subscription',
    qr_download: 'Download QR'
  }
};

let currentLang = localStorage.getItem('persepolis-lang') || 'fa';
let currentTheme = localStorage.getItem('persepolis-theme') || 'dark';
let trafficChart = null;
let chartPeriod = '7d';
let qrCodeInstance = null;
let expiryPicker = null;
let editExpiryPicker = null;

// ===== تولید یوزرنیم رندوم =====
function generateRandomUsername() {
    const prefixes = ['Cyber', 'Tech', 'Shadow', 'Neon', 'Nova', 'Apex', 'Zen', 'Vex', 'Zion', 'Knight', 'Phoenix', 'Falcon', 'Titan', 'Ghost', 'Raven', 'Wolf', 'Eagle', 'Hawk', 'Storm', 'Blaze', 'Quantum', 'Echo', 'Omega', 'Alpha', 'Delta', 'Sigma', 'Cipher', 'Dragon', 'Tiger', 'Viper'];
    const suffixes = ['X', 'Z', 'Y', 'V', 'W', 'K', 'G', 'P', 'R', 'M', 'H', 'T', 'N', 'S', 'D', 'F', 'Q', 'L', 'J', 'C'];
    const middle = ['flow', 'star', 'dark', 'light', 'storm', 'fire', 'ice', 'wind', 'cloud', 'shadow', 'nova', 'neon', 'cyber', 'ghost', 'raven', 'wolf', 'titan', 'zen', 'vex', 'apex', 'surge', 'pulse', 'cipher'];
    
    let username = '';
    const useMiddle = Math.random() > 0.4;
    
    if (useMiddle) {
        username = prefixes[Math.floor(Math.random() * prefixes.length)] + 
                    middle[Math.floor(Math.random() * middle.length)] +
                    Math.floor(Math.random() * 100);
    } else {
        username = prefixes[Math.floor(Math.random() * prefixes.length)] + 
                    suffixes[Math.floor(Math.random() * suffixes.length)] +
                    Math.floor(Math.random() * 1000);
    }
    
    document.getElementById('user-label').value = username;
    toast('✅ ' + (currentLang === 'fa' ? 'نام کاربری ساخته شد' : 'Username generated'), 'ok');
}

// ===== توابع =====
function t(key) { return translations[currentLang]?.[key] || key; }

function setTheme(theme) {
  currentTheme = theme;
  localStorage.setItem('persepolis-theme', theme);
  if (theme === 'light') {
    document.body.classList.add('light-theme');
    document.getElementById('current-theme-label').textContent = currentLang === 'fa' ? 'روشن' : 'Light';
    document.getElementById('theme-dark-btn').className = 'btn btn-o';
    document.getElementById('theme-light-btn').className = 'btn btn-pur';
  } else {
    document.body.classList.remove('light-theme');
    document.getElementById('current-theme-label').textContent = currentLang === 'fa' ? 'تاریک' : 'Dark';
    document.getElementById('theme-dark-btn').className = 'btn btn-pur';
    document.getElementById('theme-light-btn').className = 'btn btn-o';
  }
  fetch('/api/settings/theme', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ theme: theme })
  }).catch(() => {});
}

async function loadThemeFromServer() {
  try {
    const r = await fetch('/api/settings');
    const data = await r.json();
    if (data.theme) {
      currentTheme = data.theme;
      localStorage.setItem('persepolis-theme', data.theme);
      setTheme(data.theme);
    } else {
      setTheme(currentTheme);
    }
  } catch(e) { setTheme(currentTheme); }
}

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('persepolis-lang', lang);
  document.getElementById('lang-fa-btn').className = 'btn ' + (lang === 'fa' ? 'btn-pur' : 'btn-o');
  document.getElementById('lang-en-btn').className = 'btn ' + (lang === 'en' ? 'btn-pur' : 'btn-o');
  document.getElementById('current-lang-label').textContent = lang === 'fa' ? 'فارسی' : 'English';
  updateUITexts();
  fetch('/api/settings/language', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ language: lang })
  }).catch(() => {});
  
  // بروزرسانی تقویم
  if (expiryPicker) {
    expiryPicker.set('locale', lang === 'fa' ? 'fa' : 'en');
  }
  if (editExpiryPicker) {
    editExpiryPicker.set('locale', lang === 'fa' ? 'fa' : 'en');
  }
}

function updateUITexts() {
  const t = translations[currentLang];
  if (!t) return;
  
  document.getElementById('nav-home').textContent = t.nav_home;
  document.getElementById('nav-users').textContent = t.nav_users;
  document.getElementById('nav-inbound').textContent = t.nav_inbound;
  document.getElementById('nav-connections').textContent = t.nav_connections;
  document.getElementById('nav-settings').textContent = t.nav_settings;
  document.getElementById('nav-logs').textContent = t.nav_logs;
  document.getElementById('nav-backup').textContent = t.nav_backup;
  document.getElementById('nav-logout').textContent = t.nav_logout;
  
  document.getElementById('b-home').textContent = t.nav_home;
  document.getElementById('b-users').textContent = t.nav_users;
  document.getElementById('b-inbound').textContent = t.nav_inbound;
  document.getElementById('b-settings').textContent = t.nav_settings;
  
  document.getElementById('dash-title').textContent = t.dash_title;
  document.getElementById('dash-add-user').textContent = t.dash_add_user;
  document.getElementById('s-traffic').textContent = t.s_traffic;
  document.getElementById('s-requests').textContent = t.s_requests;
  document.getElementById('s-uptime').textContent = t.s_uptime;
  document.getElementById('s-disk').textContent = t.s_disk;
  document.getElementById('s-speed').textContent = t.s_speed;
  document.getElementById('s-users').textContent = t.s_users;
  document.getElementById('s-count').textContent = t.s_count;
  document.getElementById('s-time').textContent = t.s_time;
  document.getElementById('s-live').textContent = t.s_live;
  document.getElementById('chart-title-text').textContent = t.chart_title;
  document.getElementById('chart-sub-text').textContent = t.chart_sub;
  document.getElementById('recent-users-title').textContent = t.recent_users;
  
  document.getElementById('users-title').textContent = t.users_title;
  document.getElementById('users-sub').textContent = t.users_sub;
  document.getElementById('u-total').textContent = t.u_total;
  document.getElementById('u-active').textContent = t.u_active;
  document.getElementById('u-expired').textContent = t.u_expired;
  document.getElementById('u-traffic').textContent = t.u_traffic;
  document.getElementById('th-name').textContent = t.th_name;
  document.getElementById('th-account').textContent = t.th_account;
  document.getElementById('th-status').textContent = t.th_status;
  document.getElementById('th-usage').textContent = t.th_usage;
  document.getElementById('th-duration').textContent = t.th_duration;
  document.getElementById('th-actions').textContent = t.th_actions;
  document.getElementById('add-user-btn').textContent = t.add_user_btn;
  document.getElementById('no-users').textContent = t.no_users;
  
  document.getElementById('inbound-title').textContent = t.inbound_title;
  document.getElementById('inbound-sub').textContent = t.inbound_sub;
  document.getElementById('inb-port-label').textContent = t.inb_port;
  document.getElementById('inb-protocol-label').textContent = t.inb_protocol;
  document.getElementById('inb-host-label').textContent = t.inb_host;
  document.getElementById('inb-status-label').textContent = t.inb_status;
  document.getElementById('inb-status-title').textContent = t.inb_status;
  
  document.getElementById('conn-title').textContent = t.conn_title;
  document.getElementById('conn-active-label').textContent = t.conn_active;
  document.getElementById('no-conn').textContent = t.no_conn;
  
  document.getElementById('settings-title').textContent = t.settings_title;
  document.getElementById('settings-sub').textContent = t.settings_sub;
  document.getElementById('set-theme-title').textContent = t.set_theme;
  document.getElementById('set-dark').textContent = t.set_dark;
  document.getElementById('set-light').textContent = t.set_light;
  document.getElementById('set-current-theme').textContent = t.set_current_theme;
  document.getElementById('set-lang-title').textContent = t.set_lang;
  document.getElementById('set-current-lang').textContent = t.set_current_lang;
  document.getElementById('set-rgb-title').textContent = t.set_rgb;
  
  document.getElementById('backup-title').textContent = t.backup_title;
  document.getElementById('backup-sub').textContent = t.backup_sub;
  document.getElementById('backup-download-title').textContent = t.backup_download;
  document.getElementById('backup-download-btn').textContent = t.backup_download_btn;
  document.getElementById('backup-restore-btn').textContent = t.backup_restore_btn;
  
  document.getElementById('logs-title').textContent = t.logs_title;
  
  document.getElementById('modal-user-title').textContent = t.modal_user_title;
  document.getElementById('f-label-name').textContent = t.f_label_name;
  document.getElementById('f-label-quota').textContent = t.f_label_quota;
  document.getElementById('f-label-expiry').textContent = t.f_label_expiry;
  document.getElementById('f-label-devices').textContent = t.f_label_devices;
  document.getElementById('f-label-fingerprint').textContent = t.f_label_fingerprint;
  document.getElementById('f-label-protocol').textContent = t.f_label_protocol;
  document.getElementById('f-label-http').textContent = t.f_label_http;
  document.getElementById('f-label-password').textContent = t.f_label_password;
  document.getElementById('btn-create-user').textContent = t.btn_create_user;
  document.getElementById('btn-cancel').textContent = t.btn_cancel;
  
  document.getElementById('modal-edit-title').textContent = t.modal_edit_title;
  document.getElementById('e-label-name').textContent = t.e_label_name;
  document.getElementById('e-label-password').textContent = t.e_label_password;
  document.getElementById('e-label-quota').textContent = t.e_label_quota;
  document.getElementById('e-label-expiry').textContent = t.e_label_expiry;
  document.getElementById('e-label-devices').textContent = t.e_label_devices;
  document.getElementById('e-label-status').textContent = t.e_label_status;
  document.getElementById('e-label-fingerprint').textContent = t.e_label_fingerprint;
  document.getElementById('e-label-protocol').textContent = t.e_label_protocol;
  document.getElementById('e-label-http').textContent = t.e_label_http;
  document.getElementById('btn-save').textContent = t.btn_save;
  document.getElementById('btn-cancel2').textContent = t.btn_cancel;
  
  document.getElementById('modal-delete-title').textContent = t.modal_delete_title;
  document.getElementById('delete-desc').textContent = t.delete_desc;
  document.getElementById('d-label-password').textContent = t.d_label_password;
  document.getElementById('btn-delete').textContent = t.btn_delete;
  document.getElementById('btn-cancel3').textContent = t.btn_cancel;
  
  document.getElementById('qr-title').textContent = t.qr_title;
  document.getElementById('qr-desc').textContent = t.qr_desc;
  document.getElementById('qr-download').textContent = t.qr_download;
  
  document.getElementById('current-theme-label').textContent = currentTheme === 'light' ? (currentLang === 'fa' ? 'روشن' : 'Light') : (currentLang === 'fa' ? 'تاریک' : 'Dark');
  document.getElementById('current-lang-label').textContent = currentLang === 'fa' ? 'فارسی' : 'English';
}

// ===== توابع عمومی =====
function toast(msg, type = '') {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show' + (type ? ' ' + type : '');
  setTimeout(() => t.classList.remove('show'), 2500);
}

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(1) + ' MB';
  if (b < 1024**4) return (b/1024**3).toFixed(2) + ' GB';
  return (b/1024**4).toFixed(2) + ' TB';
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }

// ===== احراز هویت =====
async function authF(url, opts = {}) {
  const r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

async function logout() {
  try { await fetch('/api/logout', { method: 'POST' }); } catch(e) {}
  location.href = '/login';
}

// ===== ناوبری =====
function navTo(name) {
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  document.querySelectorAll('.bottom-nav .nav-item').forEach(n => n.classList.toggle('active', n.dataset.pg === name));
  closeSb();
  const loaders = {
    dashboard: loadDashboard,
    users: loadUsers,
    inbound: loadInbound,
    connections: loadConnections,
    logs: loadLogs,
    settings: () => {}
  };
  if (loaders[name]) loaders[name]();
}

document.querySelectorAll('.nav-it, .bottom-nav .nav-item').forEach(el => {
  el.addEventListener('click', () => navTo(el.dataset.pg));
});

const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb() { sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb() { sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
overlay.addEventListener('click', closeSb);

// ===== نمودار مصرف =====
async function loadChart(period) {
  chartPeriod = period || '7d';
  document.querySelectorAll('#chart-7d, #chart-30d, #chart-90d').forEach(btn => {
    btn.className = 'btn btn-sm btn-o';
  });
  const btnMap = {'7d':'chart-7d','30d':'chart-30d','90d':'chart-90d'};
  if (btnMap[period]) {
    document.getElementById(btnMap[period]).className = 'btn btn-sm btn-pur';
  }
  
  try {
    const r = await authF('/api/stats');
    const data = await r.json();
    const hourly = data.hourly || {};
    
    const dailyData = {};
    let days = 7;
    if (period === '30d') days = 30;
    if (period === '90d') days = 90;
    
    for (const [hour, bytes] of Object.entries(hourly)) {
      const [h] = hour.split(':');
      const date = new Date();
      date.setHours(parseInt(h), 0, 0, 0);
      const key = date.toISOString().split('T')[0];
      if (!dailyData[key]) dailyData[key] = 0;
      dailyData[key] += bytes;
    }
    
    const sortedKeys = Object.keys(dailyData).sort();
    const lastDays = sortedKeys.slice(-days);
    
    const labels = [];
    const values = [];
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days + 1);
    startDate.setHours(0, 0, 0, 0);
    
    for (let i = 0; i < days; i++) {
      const d = new Date(startDate);
      d.setDate(d.getDate() + i);
      const key = d.toISOString().split('T')[0];
      labels.push(key);
      values.push(dailyData[key] || 0);
    }
    
    const mbValues = values.map(v => Number((v / (1024 * 1024)).toFixed(2)));
    
    const labelsFa = labels.map(d => {
      const date = new Date(d);
      return date.toLocaleDateString(currentLang === 'fa' ? 'fa-IR' : 'en-US', { weekday: 'short', day: 'numeric' });
    });
    
    if (trafficChart) { trafficChart.destroy(); }
    
    const ctx = document.getElementById('trafficChart').getContext('2d');
    trafficChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labelsFa,
        datasets: [{
          label: currentLang === 'fa' ? 'مصرف (MB)' : 'Usage (MB)',
          data: mbValues,
          borderColor: '#8B5CF6',
          backgroundColor: 'rgba(139, 92, 246, 0.12)',
          borderWidth: 2,
          fill: true,
          tension: 0.4,
          pointBackgroundColor: '#8B5CF6',
          pointBorderColor: '#0a0714',
          pointBorderWidth: 1,
          pointRadius: 2,
          pointHoverRadius: 5
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) { return context.parsed.y + ' MB'; }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: { color: '#69647F', font: { size: 8 }, callback: function(value) { return value + ' MB'; } },
            grid: { color: 'rgba(139, 92, 246, 0.08)' }
          },
          x: {
            ticks: { color: '#69647F', font: { size: 8 } },
            grid: { display: false }
          }
        },
        interaction: { intersect: false, mode: 'index' }
      }
    });
  } catch(e) { console.error(e); }
}

// ===== بارگذاری داشبورد =====
async function loadDashboard() {
  try {
    const r = await authF('/api/dashboard/stats');
    const data = await r.json();
    document.getElementById('stat-traffic').textContent = (data.traffic.total / (1024 * 1024)).toFixed(1);
    document.getElementById('stat-requests').textContent = data.requests || 0;
    document.getElementById('stat-uptime').textContent = data.uptime || '00:00:00';
    document.getElementById('stat-disk').textContent = data.disk.total_fmt || '0 GB';
    document.getElementById('stat-disk-used').textContent = (currentLang === 'fa' ? 'استفاده: ' : 'Used: ') + (data.disk.used_fmt || '0');
    document.getElementById('stat-speed').textContent = data.speed.download_fmt || '0 B/s';
    document.getElementById('stat-users').textContent = data.links_count || 0;
    document.getElementById('stat-users-active').textContent = (data.active_links || 0) + (currentLang === 'fa' ? ' فعال' : ' active');
    document.getElementById('online-badge').innerHTML = '<span class="dot dg"></span> ' + (data.connections || 0) + (currentLang === 'fa' ? ' آنلاین' : ' online');
    document.getElementById('last-update').textContent = (currentLang === 'fa' ? 'بروزرسانی: ' : 'Updated: ') + new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US');
    
    const usersR = await authF('/api/links');
    const usersData = await usersR.json();
    const links = usersData.links || [];
    const recent = links.slice(0, 4);
    const grid = document.getElementById('recent-users');
    if (!recent.length) {
      grid.innerHTML = '<div class="empty" style="padding:10px"><i class="ti ti-users"></i><p style="font-size:9px">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users') + '</p></div>';
    } else {
      grid.innerHTML = recent.map(l => `<div style="background:rgba(139,92,246,0.02);border-radius:4px;padding:4px 6px;display:flex;justify-content:space-between;align-items:center;transition:transform .3s"><div><div style="font-size:9px;font-weight:600;color:var(--t1)">${esc(l.label)}</div><div style="font-size:7px;color:var(--t3)">${l.active ? '🟢' : '🔴'}</div></div><div style="font-size:8px;color:var(--t2)">${fmtB(l.used_bytes||0)}</div></div>`).join('');
    }
    
    loadChart(chartPeriod);
  } catch(e) { console.error(e); }
}

// ===== بارگذاری اینباند =====
async function loadInbound() {
  try {
    const r = await authF('/api/inbound');
    const data = await r.json();
    document.getElementById('inbound-port').textContent = data.port || 443;
    document.getElementById('inbound-protocol').textContent = (data.protocol || 'vless-ws').toUpperCase();
    document.getElementById('inbound-host').textContent = data.host || '—';
  } catch(e) { console.error(e); }
}

// ===== بارگذاری کاربران =====
async function loadUsers() {
  try {
    const r = await authF('/api/links');
    const { links = [] } = await r.json();
    const tbody = document.getElementById('users-tbody');
    const total = links.length;
    const active = links.filter(l => l.active && !l.expired).length;
    const expired = links.filter(l => l.expired).length;
    const totalTraffic = links.reduce((sum, l) => sum + (l.used_bytes || 0), 0);
    
    document.getElementById('users-total').textContent = total;
    document.getElementById('users-active').textContent = active;
    document.getElementById('users-expired').textContent = expired;
    document.getElementById('users-traffic').textContent = fmtB(totalTraffic);
    document.getElementById('users-count-label').textContent = total + (currentLang === 'fa' ? ' کاربر' : ' users');
    
    if (!links.length) {
      tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users found') + '</td></tr>';
      return;
    }
    
    const fpEmoji = { chrome: '🌐', firefox: '🦊', safari: '🧭', edge: '🌊', ios: '📱', android: '🤖', safari_ios: '🍏', random: '🎲', none: '🚫' };
    const protocolIcons = { 'vless-ws':'🚀', 'vless-grpc':'⚡', 'vless-xhttp':'🛡️', 'vless-http2':'📶', 'trojan-ws':'🔒', 'shadowsocks':'🌊' };
    
    tbody.innerHTML = links.map(l => {
      const isActive = l.active && !l.expired;
      const statusClass = isActive ? 'active' : (l.expired ? 'expired' : 'disabled');
      const statusText = isActive ? (currentLang === 'fa' ? 'فعال' : 'Active') : (l.expired ? (currentLang === 'fa' ? 'منقضی' : 'Expired') : (currentLang === 'fa' ? 'غیرفعال' : 'Disabled'));
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      const usedFmt = fmtB(l.used_bytes || 0);
      const limitFmt = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
      const fp = l.fingerprint || 'chrome';
      const fpName = { chrome: 'Chrome', firefox: 'Firefox', safari: 'Safari', edge: 'Edge', ios: 'iOS', android: 'Android', safari_ios: 'Safari iOS', random: 'Random', none: 'None' }[fp] || fp;
      const protocol = l.protocol || 'vless-ws';
      const protoIcon = protocolIcons[protocol] || '🚀';
      const protoName = { 'vless-ws':'VLESS-WS', 'vless-grpc':'VLESS-gRPC', 'vless-xhttp':'VLESS-XHTTP', 'vless-http2':'VLESS-HTTP/2', 'trojan-ws':'Trojan-WS', 'shadowsocks':'Shadowsocks' }[protocol] || protocol;
      const httpVer = l.http_version || 'h2';
      const httpName = { 'h1':'HTTP/1.1', 'h2':'HTTP/2', 'h3':'HTTP/3', 'auto':'Auto' }[httpVer] || httpVer;
      let duration = '∞';
      let durationPct = 100;
      let durationClass = '';
      if (l.expires_at) {
        try {
          const exp = new Date(l.expires_at);
          const now = new Date();
          const days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
          duration = days > 0 ? days + (currentLang === 'fa' ? ' روز' : ' days') : (currentLang === 'fa' ? 'منقضی' : 'Expired');
          const created = l.created_at ? new Date(l.created_at) : null;
          const totalMs = created ? (exp - created) : null;
          if (totalMs && totalMs > 0) {
            durationPct = Math.max(0, Math.min(100, ((exp - now) / totalMs) * 100));
          } else {
            durationPct = days > 0 ? 100 : 0;
          }
          durationClass = durationPct <= 10 ? 'crit' : (durationPct <= 25 ? 'warn' : '');
        } catch(e) { duration = '—'; durationPct = 100; }
      }
      const avatarLetter = (l.label || 'U')[0].toUpperCase();
      return `<tr><td><div class="user-name-cell"><div class="avatar">${avatarLetter}</div><div><div class="name">${esc(l.label)}</div><div class="uuid-short">${l.uuid.slice(0,8)}… ${protoIcon} ${protoName}</div></div></div></td><td style="font-size:9px;color:var(--t2);">${fpEmoji[fp] || '🌐'} ${fpName}<br><span style="font-size:7px;color:var(--t3)">${httpName}</span></td><td><span class="status-badge ${statusClass}"><span class="status-dot"></span>${statusText}</span></td><td><div class="usage-bar"><span class="usage-text">${usedFmt} / ${limitFmt}</span><div class="bar"><div class="fill" style="width:${pct}%"></div></div></div></td><td><div class="duration-bar"><span class="duration-text ${durationClass}">${duration}</span><div class="bar"><div class="fill" style="width:${durationPct}%"></div></div></div></td><td><div class="action-btns"><button class="btn btn-pur btn-sm" onclick="showQR('${l.sub_url}')" title="QR Code"><i class="ti ti-qrcode"></i></button><button class="btn btn-pur btn-sm" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('${currentLang === 'fa' ? '✅ کپی ساب' : '✅ Copied'}','ok'))" title="${currentLang === 'fa' ? 'کپی ساب‌لینک' : 'Copy sub'}"><i class="ti ti-link"></i></button><button class="btn btn-amber btn-sm" onclick="resetUsage('${l.uuid}')" title="${currentLang === 'fa' ? 'ریست مصرف' : 'Reset usage'}"><i class="ti ti-rotate"></i></button><button class="btn btn-pur btn-sm" onclick="openEditModal('${l.uuid}')" title="${currentLang === 'fa' ? 'ویرایش' : 'Edit'}"><i class="ti ti-edit"></i></button><button class="btn btn-d btn-sm" onclick="openDeleteModal('${l.uuid}')" title="${currentLang === 'fa' ? 'حذف' : 'Delete'}"><i class="ti ti-trash"></i></button></div></td></tr>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== QR Code =====
function showQR(url) {
  const container = document.getElementById('qrcode-container');
  container.innerHTML = '';
  if (qrCodeInstance) { qrCodeInstance.clear(); qrCodeInstance = null; }
  qrCodeInstance = new QRCode(container, {
    text: url,
    width: 200,
    height: 200,
    colorDark: '#8B5CF6',
    colorLight: '#08080d',
    correctLevel: QRCode.CorrectLevel.H
  });
  openModal('modal-qr');
  container.dataset.url = url;
}

function downloadQR() {
  const canvas = document.querySelector('#qrcode-container canvas');
  if (!canvas) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); return; }
  const link = document.createElement('a');
  link.download = 'qrcode.png';
  link.href = canvas.toDataURL('image/png');
  link.click();
  toast('✅ ' + (currentLang === 'fa' ? 'QR دانلود شد' : 'QR downloaded'), 'ok');
}

// ===== مدیریت کاربران با تقویم =====
function initDatePickers() {
  // تقویم ساخت کاربر
  if (expiryPicker) {
    expiryPicker.destroy();
  }
  expiryPicker = flatpickr("#user-expiry-date", {
    locale: currentLang === 'fa' ? 'fa' : 'en',
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: true,
    placeholder: currentLang === 'fa' ? 'انتخاب تاریخ انقضا' : 'Select expiry date',
    allowInput: true,
    onChange: function(selectedDates, dateStr, instance) {
      if (dateStr) {
        document.getElementById('user-expiry-date').value = dateStr;
      }
    }
  });
  
  // تقویم ویرایش کاربر
  if (editExpiryPicker) {
    editExpiryPicker.destroy();
  }
  editExpiryPicker = flatpickr("#edit-expiry-date", {
    locale: currentLang === 'fa' ? 'fa' : 'en',
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: true,
    placeholder: currentLang === 'fa' ? 'انتخاب تاریخ انقضا' : 'Select expiry date',
    allowInput: true,
    onChange: function(selectedDates, dateStr, instance) {
      if (dateStr) {
        document.getElementById('edit-expiry-date').value = dateStr;
      }
    }
  });
}

async function saveUser() {
  const label = document.getElementById('user-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('user-quota').value) || 0;
  const expiryDate = document.getElementById('user-expiry-date').value;
  const devices = parseInt(document.getElementById('user-devices').value) || 0;
  const password = document.getElementById('user-password').value.trim();
  const fingerprint = document.getElementById('user-fingerprint').value || 'chrome';
  const protocol = document.getElementById('user-protocol').value || 'vless-ws';
  const http_version = document.getElementById('user-http').value || 'h2';
  
  // محاسبه روزهای باقیمانده از تاریخ
  let expires_days = 0;
  if (expiryDate) {
    const exp = new Date(expiryDate);
    const now = new Date();
    expires_days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
    if (expires_days < 0) expires_days = 0;
  }
  
  try {
    const r = await authF('/api/links', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ label, limit_value: quota, limit_unit: 'GB', expires_days, max_devices: devices, password, fingerprint, protocol, http_version })
    });
    if (!r.ok) throw new Error();
    document.getElementById('user-label').value = 'کاربر';
    document.getElementById('user-quota').value = '2';
    document.getElementById('user-expiry-date').value = '';
    document.getElementById('user-devices').value = '1';
    document.getElementById('user-password').value = '';
    document.getElementById('user-fingerprint').value = 'chrome';
    document.getElementById('user-protocol').value = 'vless-ws';
    document.getElementById('user-http').value = 'h2';
    closeModal('modal-user');
    toast('✅ ' + (currentLang === 'fa' ? 'کاربر ساخته شد' : 'User created'), 'ok');
    loadUsers();
    loadDashboard();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function openEditModal(uuid) {
  try {
    const r = await authF('/api/links');
    const { links = [] } = await r.json();
    const link = links.find(l => l.uuid === uuid);
    if (!link) { toast((currentLang === 'fa' ? 'کاربر یافت نشد' : 'User not found'), 'err'); return; }
    document.getElementById('edit-uuid').value = uuid;
    document.getElementById('edit-label').value = link.label || '';
    document.getElementById('edit-password').value = '';
    document.getElementById('edit-quota').value = link.limit_bytes === 0 ? '' : (link.limit_bytes / (1024 ** 3)).toFixed(1);
    
    // تنظیم تاریخ در تقویم
    if (link.expires_at) {
      const expDate = new Date(link.expires_at);
      const dateStr = expDate.toISOString().split('T')[0];
      document.getElementById('edit-expiry-date').value = dateStr;
      if (editExpiryPicker) {
        editExpiryPicker.setDate(dateStr);
      }
    } else {
      document.getElementById('edit-expiry-date').value = '';
      if (editExpiryPicker) {
        editExpiryPicker.clear();
      }
    }
    
    document.getElementById('edit-devices').value = link.max_devices || 0;
    document.getElementById('edit-status').value = link.active ? 'true' : 'false';
    document.getElementById('edit-fingerprint').value = link.fingerprint || 'chrome';
    document.getElementById('edit-protocol').value = link.protocol || 'vless-ws';
    document.getElementById('edit-http').value = link.http_version || 'h2';
    document.getElementById('edit-password-section').style.display = link.has_password ? 'block' : 'none';
    openModal('modal-edit');
  } catch(e) { toast((currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function saveEdit() {
  const uuid = document.getElementById('edit-uuid').value;
  const password = document.getElementById('edit-password').value.trim();
  const label = document.getElementById('edit-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('edit-quota').value) || 0;
  const expiryDate = document.getElementById('edit-expiry-date').value;
  const devices = parseInt(document.getElementById('edit-devices').value) || 0;
  const active = document.getElementById('edit-status').value === 'true';
  const fingerprint = document.getElementById('edit-fingerprint').value || 'chrome';
  const protocol = document.getElementById('edit-protocol').value || 'vless-ws';
  const http_version = document.getElementById('edit-http').value || 'h2';
  
  let expires_days = 0;
  if (expiryDate) {
    const exp = new Date(expiryDate);
    const now = new Date();
    expires_days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
    if (expires_days < 0) expires_days = 0;
  }
  
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ label, limit_value: quota, limit_unit: 'GB', expires_days, max_devices: devices, active, password, fingerprint, protocol, http_version })
    });
    if (!r.ok) {
      if (r.status === 403) { toast('❌ ' + (currentLang === 'fa' ? 'رمز اشتباه' : 'Wrong password'), 'err'); return; }
      throw new Error();
    }
    closeModal('modal-edit');
    toast('✅ ' + (currentLang === 'fa' ? 'ویرایش شد' : 'Saved'), 'ok');
    loadUsers();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

function openDeleteModal(uuid) {
  document.getElementById('delete-uuid').value = uuid;
  document.getElementById('delete-password').value = '';
  openModal('modal-delete');
}

async function confirmDelete() {
  const uuid = document.getElementById('delete-uuid').value;
  const password = document.getElementById('delete-password').value.trim();
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ password })
    });
    if (!r.ok) {
      if (r.status === 403) { toast('❌ ' + (currentLang === 'fa' ? 'رمز اشتباه' : 'Wrong password'), 'err'); return; }
      throw new Error();
    }
    closeModal('modal-delete');
    toast('✅ ' + (currentLang === 'fa' ? 'حذف شد' : 'Deleted'), 'ok');
    loadUsers();
    loadDashboard();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function resetUsage(uuid) {
  if (!confirm(currentLang === 'fa' ? 'ریست مصرف؟' : 'Reset usage?')) return;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reset_usage: true })
    });
    if (!r.ok) throw new Error();
    toast('✅ ' + (currentLang === 'fa' ? 'ریست شد' : 'Reset'), 'ok');
    loadUsers();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

// ===== بارگذاری اتصالات =====
async function loadConnections() {
  try {
    const r = await authF('/api/connections');
    const d = await r.json();
    const grid = document.getElementById('conns-grid');
    const count = d.count || 0;
    document.getElementById('conn-count').textContent = count + (currentLang === 'fa' ? ' اتصال' : ' connections');
    if (!count) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-plug-off"></i><p>' + (currentLang === 'fa' ? 'هیچ اتصالی وجود ندارد' : 'No connections') + '</p></div>';
      return;
    }
    grid.innerHTML = d.connections.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + 's' : secs < 3600 ? Math.floor(secs / 60) + 'm' : Math.floor(secs / 3600) + 'h';
      return `<div class="conn-card"><div class="ip"><span class="conn-status-dot"></span> ${esc(c.ip)}</div><div class="label">${esc(c.label || 'نامشخص')}</div><div class="conn-info"><span>📥 ${esc(c.bytes_fmt || '0 B')}</span><span>⏱ ${dur}</span></div></div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== بارگذاری لاگ‌ها =====
async function loadLogs() {
  try {
    const r = await authF('/api/activity');
    const data = await r.json();
    const logs = data.logs || [];
    document.getElementById('logs-count').textContent = logs.length + (currentLang === 'fa' ? ' لاگ' : ' logs');
    const container = document.getElementById('logs-container');
    if (!logs.length) {
      container.innerHTML = '<div class="empty"><i class="ti ti-notes"></i><p>' + (currentLang === 'fa' ? 'هیچ لاگی وجود ندارد' : 'No logs') + '</p></div>';
      return;
    }
    container.innerHTML = logs.map(log => {
      const time = log.time ? new Date(log.time).toLocaleString(currentLang === 'fa' ? 'fa-IR' : 'en-US') : '—';
      const color = log.level === 'err' ? '#F87171' : log.level === 'warn' ? '#FCD34D' : '#22D3EE';
      return `<div style="padding:3px 0;border-bottom:1px solid rgba(139,92,246,0.02);display:flex;gap:6px"><span style="color:${color};font-weight:700">[${(log.level || 'info').toUpperCase()}]</span><span style="color:var(--t3)">${time}</span><span>${esc(log.message)}</span></div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== RGB Mode =====
let rgbMode = false;
let rgbHue = 258;
let rgbTimer = null;

function rgbTick() {
  rgbHue = (rgbHue + 0.55) % 360;
  const root = document.documentElement.style;
  const h1 = rgbHue, h2 = (rgbHue + 65) % 360, h3 = (rgbHue + 300) % 360;
  root.setProperty('--accent', `hsl(${h1},88%,64%)`);
  root.setProperty('--accent2', `hsl(${h2},90%,62%)`);
  root.setProperty('--accent3', `hsl(${h3},75%,46%)`);
  root.setProperty('--card-b', `hsla(${h1},88%,64%,0.14)`);
  root.setProperty('--card-bh', `hsla(${h1},88%,64%,0.24)`);
  root.setProperty('--glow-1', `hsla(${h1},88%,60%,0.10)`);
  root.setProperty('--glow-2', `hsla(${h2},90%,60%,0.08)`);
}

function startRGBCycle() {
  document.body.classList.add('rgb-mode');
  if (rgbTimer) return;
  rgbTimer = setInterval(rgbTick, 35);
}

function stopRGBCycle() {
  document.body.classList.remove('rgb-mode');
  if (rgbTimer) { clearInterval(rgbTimer); rgbTimer = null; }
  const root = document.documentElement.style;
  ['--accent','--accent2','--accent3','--card-b','--card-bh','--glow-1','--glow-2'].forEach(v => root.removeProperty(v));
}

async function loadRGBStatus() {
  try {
    const r = await authF('/api/settings');
    const data = await r.json();
    rgbMode = data.rgb_mode || false;
    updateRGBUI();
  } catch(e) {}
}

function updateRGBUI() {
  const sw = document.getElementById('rgb-switch');
  if (rgbMode) { startRGBCycle(); sw.classList.add('on'); }
  else { stopRGBCycle(); sw.classList.remove('on'); }
}

async function toggleRGB() {
  const newState = !rgbMode;
  try {
    const r = await authF('/api/settings/rgb', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enabled: newState })
    });
    const data = await r.json();
    rgbMode = data.rgb_mode;
    updateRGBUI();
    toast(rgbMode ? '🌈 RGB ' + (currentLang === 'fa' ? 'فعال شد' : 'enabled') : '🌙 RGB ' + (currentLang === 'fa' ? 'غیرفعال شد' : 'disabled'), 'ok');
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

// ===== تغییر رمز عبور / نام کاربری =====
async function changeCredentials() {
  const btn = document.getElementById('cred-submit-btn');
  const currentPass = document.getElementById('cred-current-pass').value;
  const newUser = document.getElementById('cred-new-user').value.trim();
  const newPass = document.getElementById('cred-new-pass').value;
  const newPass2 = document.getElementById('cred-new-pass2').value;

  if (!currentPass) { toast('❌ رمز عبور فعلی را وارد کنید', 'err'); return; }
  if (!newUser && !newPass) { toast('⚠️ چیزی برای تغییر وارد نکردید', 'warn'); return; }
  if (newPass && newPass.length < 4) { toast('❌ رمز عبور جدید باید حداقل ۴ کاراکتر باشد', 'err'); return; }
  if (newPass !== newPass2) { toast('❌ تکرار رمز عبور مطابقت ندارد', 'err'); return; }

  btn.disabled = true;
  const originalHtml = btn.innerHTML;
  btn.innerHTML = '<i class="ti ti-loader-2"></i> در حال ذخیره...';
  try {
    const r = await authF('/api/settings/credentials', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ current_password: currentPass, new_username: newUser, new_password: newPass })
    });
    const data = await r.json();
    if (!r.ok) { throw new Error(data.detail || 'خطا'); }
    toast('✅ اطلاعات ورود با موفقیت تغییر کرد', 'ok');
    document.getElementById('cred-current-pass').value = '';
    document.getElementById('cred-new-user').value = '';
    document.getElementById('cred-new-pass').value = '';
    document.getElementById('cred-new-pass2').value = '';
  } catch(e) {
    toast('❌ ' + (e.message || 'خطا در تغییر اطلاعات'), 'err');
  } finally {
    btn.disabled = false;
    btn.innerHTML = originalHtml;
  }
}

// ===== بکاپ =====
async function createBackup() {
  try {
    const r = await authF('/api/backup');
    const data = await r.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `persepolis_backup_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    toast('✅ ' + (currentLang === 'fa' ? 'بکاپ دانلود شد' : 'Backup downloaded'), 'ok');
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function restoreBackup(event) {
  const file = event.target.files[0];
  if (!file) return;
  try {
    const text = await file.text();
    const data = JSON.parse(text);
    const r = await authF('/api/backup/restore', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!r.ok) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); return; }
    toast('✅ ' + (currentLang === 'fa' ? 'بکاپ بازیابی شد' : 'Backup restored'), 'ok');
    setTimeout(() => location.reload(), 1000);
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا: ' : 'Error: ') + e.message, 'err'); }
  event.target.value = '';
}

// ===== راه‌اندازی اولیه =====
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch(e) { location.href = '/login'; }
  
  await loadThemeFromServer();
  setLang(currentLang);
  await loadRGBStatus();
  initDatePickers();
  
  loadDashboard();
  loadInbound();
  loadUsers();
  loadConnections();
  loadLogs();
  
  setInterval(() => {
    if (document.getElementById('pg-dashboard').classList.contains('on')) loadDashboard();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConnections();
    if (document.getElementById('pg-users').classList.contains('on')) loadUsers();
  }, 10000);
});
</script>
</body></html>"""


# ===== تابع ساب‌لینک حرفه‌ای با طراحی کارتی =====
def get_sub_page_html(uuid: str, link: dict) -> str:
    """صفحه ساب‌لینک با طراحی کارتی و دکمه‌های اپلیکیشن"""
    from datetime import datetime
    
    used = link.get('used_bytes', 0)
    limit = link.get('limit_bytes', 0)
    active = link.get('active', True)
    expired = link.get('expired', False)
    label = link.get('label', 'کاربر')
    fingerprint = link.get('fingerprint', 'chrome')
    max_devices = link.get('max_devices', 0)
    protocol = link.get('protocol', 'vless-ws')
    http_version = link.get('http_version', 'h2')
    active_connections = link.get('active_connections', 0)
    sub_url = link.get('sub_url', '')
    used_val = link.get('used_val', '0')
    used_unit = link.get('used_unit', 'B')
    limit_val = link.get('limit_val', '∞')
    limit_unit = link.get('limit_unit', '')
    percent = link.get('percent', 0)
    days_left = link.get('days_left', 'نامحدود')
    vless_link = link.get('vless_link', '')
    protocol_name = link.get('protocol_name', 'VLESS-WS')
    protocol_icon = link.get('protocol_icon', '🚀')
    http_name = link.get('http_name', 'HTTP/2')
    
    is_allowed = active and not expired
    host = get_host() if 'get_host' in dir() else 'localhost'
    
    def fmt_bytes(b):
        if not b or b == 0:
            return '0 B'
        if b < 1024:
            return f'{b} B'
        if b < 1024**2:
            return f'{b/1024:.1f} KB'
        if b < 1024**3:
            return f'{b/1024**2:.2f} MB'
        return f'{b/1024**3:.2f} GB'
    
    used_fmt = fmt_bytes(used)
    limit_fmt = 'نامحدود' if limit == 0 else fmt_bytes(limit)
    
    # منوی تم‌ها
    theme_names = {
        'persepolis_gold':'🏛️ طلایی',
        'persepolis_dark':'🌙 شب',
        'persepolis_sun':'☀️ آفتاب',
        'persepolis_royal':'👑 سلطنتی',
        'persepolis_stone':'🗿 سنگی',
        'persepolis_light':'✨ روشن',
        'persepolis_warm':'🔥 گرم',
        'persepolis_cool':'❄️ خنک',
        'persepolis_ancient':'🏺 کهن',
        'persepolis_modern':'💎 مدرن'
    }
    theme_colors = {
        'persepolis_gold':'linear-gradient(135deg,#D9A03C,#F0C674)',
        'persepolis_dark':'linear-gradient(135deg,#9494A6,#C4C4D4)',
        'persepolis_sun':'linear-gradient(135deg,#FB923C,#FBBF24)',
        'persepolis_royal':'linear-gradient(135deg,#8B5CF6,#22D3EE)',
        'persepolis_stone':'linear-gradient(135deg,#A3A38A,#7A7A64)',
        'persepolis_light':'linear-gradient(135deg,#6366F1,#8B5CF6)',
        'persepolis_warm':'linear-gradient(135deg,#F43F5E,#FB7185)',
        'persepolis_cool':'linear-gradient(135deg,#0EA5E9,#22D3EE)',
        'persepolis_ancient':'linear-gradient(135deg,#A3946D,#7A6E4E)',
        'persepolis_modern':'linear-gradient(135deg,#8B5CF6,#22D3EE)'
    }
    
    menu_items = ""
    for t in ['persepolis_gold','persepolis_dark','persepolis_sun','persepolis_royal','persepolis_stone','persepolis_light','persepolis_warm','persepolis_cool','persepolis_ancient','persepolis_modern']:
        menu_items += f"""
        <div class="menu-item" data-theme="{t}" onclick="selectTheme('{t}')">
            <span class="dot" style="background:{theme_colors[t]}"></span>
            {theme_names[t]}
            <span class="check">✓</span>
        </div>
        """
    
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>🏛️ {label} · تخت جمشید</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{
  --bg:#08080d;--card:rgba(10,10,30,0.85);--card-border:rgba(139,92,246,0.08);
  --text:#EDEDF7;--text2:#B4AEDD;--text3:#69647F;
  --accent:#8B5CF6;--accent2:#22D3EE;--accent3:#6D28D9;
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-text:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.08);--red-text:#F87171;
  --shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(139,92,246,0.02);
  --transition:all 0.4s cubic-bezier(0.34,1.56,0.64,1);--radius:16px
}}
[data-theme="persepolis_gold"]{{--bg:#0d0a05;--card:rgba(20,15,8,0.85);--card-border:rgba(217,160,60,0.1);--accent:#D9A03C;--accent2:#F0C674;--text:#F5ECD7;--text2:#C9AD78;--text3:#8A7A4A}}
[data-theme="persepolis_dark"]{{--bg:#08080a;--card:rgba(14,14,17,0.85);--card-border:rgba(148,148,166,0.08);--accent:#9494A6;--accent2:#C4C4D4;--text:#EDEDF2;--text2:#A0A0B0;--text3:#68687A}}
[data-theme="persepolis_sun"]{{--bg:#120a05;--card:rgba(28,16,8,0.85);--card-border:rgba(251,146,60,0.1);--accent:#FB923C;--accent2:#FBBF24;--text:#FFF3E0;--text2:#E0A868;--text3:#8A6A3A}}
[data-theme="persepolis_royal"]{{--bg:#0a0714;--card:rgba(18,12,28,0.85);--card-border:rgba(139,92,246,0.1);--accent:#8B5CF6;--accent2:#22D3EE;--text:#EDEDF7;--text2:#B4AEDD;--text3:#69647F}}
[data-theme="persepolis_stone"]{{--bg:#0a0a0a;--card:rgba(18,18,18,0.85);--card-border:rgba(160,160,150,0.08);--accent:#A3A38A;--accent2:#7A7A64;--text:#E5E3DC;--text2:#A8A695;--text3:#6E6C5C}}
[data-theme="persepolis_light"]{{--bg:#F2F1FA;--card:rgba(255,255,255,0.85);--card-border:rgba(99,102,241,0.1);--accent:#6366F1;--accent2:#8B5CF6;--text:#15121F;--text2:#5A5670;--text3:#8A87A0}}
[data-theme="persepolis_warm"]{{--bg:#120608;--card:rgba(28,10,12,0.85);--card-border:rgba(244,63,94,0.1);--accent:#F43F5E;--accent2:#FB7185;--text:#FDECEE;--text2:#D88A96;--text3:#8A5A62}}
[data-theme="persepolis_cool"]{{--bg:#050a12;--card:rgba(8,18,28,0.85);--card-border:rgba(14,165,233,0.1);--accent:#0EA5E9;--accent2:#22D3EE;--text:#DFF3FC;--text2:#7FB8D4;--text3:#4A7A8A}}
[data-theme="persepolis_ancient"]{{--bg:#0a0805;--card:rgba(18,14,8,0.85);--card-border:rgba(163,148,109,0.08);--accent:#A3946D;--accent2:#7A6E4E;--text:#E8DDC8;--text2:#A89870;--text3:#6A5A3A}}
[data-theme="persepolis_modern"]{{--bg:#08080d;--card:rgba(10,10,25,0.85);--card-border:rgba(139,92,246,0.1);--accent:#8B5CF6;--accent2:#22D3EE;--text:#F0EEFF;--text2:#B4AEDD;--text3:#69647F}}

@keyframes twinkle{{0%,100%{{opacity:0.1}}50%{{opacity:0.5}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
@keyframes cardIn{{from{{opacity:0;transform:translateY(30px) scale(0.96)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes float{{0%,100%{{transform:translate(0,0) scale(1)}}50%{{transform:translate(20px,-20px) scale(1.03)}}}}

body{{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;background:var(--bg);color:var(--text);transition:var(--transition);position:relative;overflow-x:hidden}}
.stars-container{{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}}
.star{{position:absolute;border-radius:50%;background:var(--text);animation:twinkle 4s ease-in-out infinite}}
.glow-orb{{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:float 8s ease-in-out infinite}}
.glow-orb1{{width:400px;height:400px;background:rgba(139,92,246,0.04);top:-100px;right:-50px}}
.glow-orb2{{width:300px;height:300px;background:rgba(34,211,238,0.03);bottom:-50px;left:-30px;animation-delay:3s}}

.theme-dropdown{{position:fixed;top:20px;left:50%;transform:translateX(-50%);z-index:100}}
.theme-dropdown .toggle-btn{{background:var(--card);backdrop-filter:blur(40px) saturate(160%);border:1px solid var(--card-border);border-radius:14px;padding:10px 20px;color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:13px;font-weight:600;cursor:pointer;display:flex;align-items:center;gap:10px;transition:var(--transition);box-shadow:0 8px 40px rgba(0,0,0,0.3)}}
.theme-dropdown .toggle-btn:hover{{border-color:var(--accent);transform:scale(1.02)}}
.theme-dropdown .toggle-btn .arrow{{transition:transform .3s;font-size:12px}}
.theme-dropdown .toggle-btn .arrow.open{{transform:rotate(180deg)}}
.theme-dropdown .menu{{display:none;position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%);background:var(--card);backdrop-filter:blur(40px) saturate(160%);border:1px solid var(--card-border);border-radius:14px;padding:8px;min-width:200px;box-shadow:0 12px 50px rgba(0,0,0,0.4)}}
.theme-dropdown .menu.open{{display:block}}
.theme-dropdown .menu-item{{display:flex;align-items:center;gap:10px;padding:8px 14px;border-radius:10px;cursor:pointer;transition:var(--transition);color:var(--text2);font-size:13px;font-weight:500}}
.theme-dropdown .menu-item:hover{{background:rgba(139,92,246,0.06);color:var(--text)}}
.theme-dropdown .menu-item .dot{{display:inline-block;width:18px;height:18px;border-radius:5px;flex-shrink:0;border:1px solid rgba(255,255,255,0.1)}}
.theme-dropdown .menu-item .check{{margin-right:auto;opacity:0;transition:opacity .2s;color:var(--accent)}}
.theme-dropdown .menu-item.active .check{{opacity:1}}
.theme-dropdown .menu-item.active{{background:rgba(139,92,246,0.06);color:var(--text)}}

.card{{position:relative;z-index:10;background:var(--card);backdrop-filter:blur(40px) saturate(160%);border:1px solid var(--card-border);border-radius:var(--radius);padding:24px 20px 20px;max-width:480px;width:100%;box-shadow:var(--shadow);animation:cardIn 0.6s ease;transition:var(--transition);margin-top:60px}}

/* هدر کارت */
.card-header{{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--card-border)}}
.brand{{display:flex;align-items:center;gap:8px}}
.brand-icon{{width:32px;height:32px;border-radius:8px;background:linear-gradient(135deg,#8B5CF6,#6D28D9);display:flex;align-items:center;justify-content:center;font-size:16px;box-shadow:0 0 30px rgba(139,92,246,0.15)}}
.brand-text{{font-size:11px;font-weight:700;background:linear-gradient(135deg,#22D3EE,#8B5CF6);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.brand-sub{{font-size:6px;color:var(--text3)}}
.theme-toggle-btn{{background:rgba(139,92,246,0.05);border:1px solid var(--card-border);color:var(--text2);width:30px;height:30px;border-radius:6px;cursor:pointer;font-size:14px;transition:var(--transition)}}
.theme-toggle-btn:hover{{background:rgba(139,92,246,0.1);transform:rotate(20deg)}}

/* نام کاربر */
.user-name-row{{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}}
.user-name{{font-size:20px;font-weight:800;color:var(--text);display:flex;align-items:center;gap:6px}}
.user-name .proto-badge{{font-size:9px;font-weight:600;background:rgba(139,92,246,0.08);padding:2px 10px;border-radius:12px;color:var(--accent2);letter-spacing:0.3px}}
.status-badge{{display:inline-flex;align-items:center;gap:4px;padding:2px 12px;border-radius:12px;font-size:10px;font-weight:700}}
.status-badge.active{{background:var(--green-bg);color:var(--green-text);border:1px solid rgba(16,185,129,0.1)}}
.status-badge.inactive{{background:var(--red-bg);color:var(--red-text);border:1px solid rgba(239,68,68,0.1)}}
.status-dot{{width:6px;height:6px;border-radius:50%;display:inline-block;animation:pulse 1.5s infinite}}
.status-dot.green{{background:var(--green-text)}}
.status-dot.red{{background:var(--red-text)}}

/* UUID */
.uuid-box{{background:rgba(139,92,246,0.03);border:1px solid var(--card-border);border-radius:8px;padding:6px 10px;font-size:9px;font-family:monospace;color:var(--text3);word-break:break-all;cursor:pointer;transition:var(--transition);text-align:center;margin:6px 0 10px}}
.uuid-box:hover{{background:rgba(139,92,246,0.06);transform:scale(1.01)}}

/* آمار مصرف - کارت‌های اطلاعات */
.stats-card-grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:10px 0}}
.stat-info-card{{background:rgba(139,92,246,0.02);border:1px solid var(--card-border);border-radius:10px;padding:10px 12px;transition:var(--transition)}}
.stat-info-card:hover{{background:rgba(139,92,246,0.04);transform:translateY(-2px)}}
.stat-info-label{{font-size:7px;color:var(--text3);font-weight:600;text-transform:uppercase;letter-spacing:0.04em}}
.stat-info-value{{font-size:15px;font-weight:700;color:var(--text);margin-top:2px}}
.stat-info-value .unit{{font-size:9px;font-weight:400;color:var(--text2)}}
.stat-info-value.used{{color:var(--accent2)}}
.stat-info-value.limit{{color:var(--text2)}}

/* نوار پیشرفت */
.progress-section{{margin:8px 0}}
.progress-bar{{height:7px;border-radius:5px;background:rgba(139,92,246,0.06);overflow:hidden;box-shadow:inset 0 0 5px rgba(0,0,0,0.35)}}
.progress-fill{{height:100%;border-radius:5px;background:linear-gradient(90deg,#FF3CAC,#784BA0,#2B86C5,#22D3EE,#8B5CF6,#FF3CAC);background-size:300% 100%;animation:rgbBarFlow 5s linear infinite;box-shadow:0 0 10px rgba(139,92,246,.6);width:0%;transition:width 1.2s ease}}
@keyframes rgbBarFlow{{0%{{background-position:0% 50%}}100%{{background-position:300% 50%}}}}
.progress-text{{display:flex;justify-content:space-between;font-size:8px;color:var(--text3);margin-top:3px}}
.progress-text .pct{{font-weight:700;color:var(--text2)}}

/* لینک ساب‌اسکریپشن */
.sub-link-section{{background:rgba(139,92,246,0.02);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;margin:8px 0}}
.sub-link-label{{font-size:7px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:0.04em;display:flex;align-items:center;gap:4px;margin-bottom:3px}}
.sub-link-label i{{color:var(--accent);font-size:8px}}
.sub-link-url{{font-family:monospace;font-size:8px;color:var(--accent2);word-break:break-all;line-height:1.5;background:rgba(0,0,0,0.2);padding:4px 6px;border-radius:4px;border:1px solid var(--card-border)}}
.sub-link-actions{{display:flex;gap:4px;margin-top:4px;flex-wrap:wrap}}
.sub-link-actions .btn{{flex:1;font-size:8px;padding:4px 8px;justify-content:center}}

/* دکمه‌های اپلیکیشن */
.apps-section{{margin:10px 0}}
.apps-title{{font-size:9px;font-weight:700;color:var(--text3);margin-bottom:6px;display:flex;align-items:center;gap:4px}}
.apps-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}}
.app-btn{{background:rgba(139,92,246,0.02);border:1px solid var(--card-border);border-radius:8px;padding:6px 4px;text-align:center;cursor:pointer;transition:var(--transition);text-decoration:none;color:var(--text)}}
.app-btn:hover{{background:rgba(139,92,246,0.06);transform:translateY(-2px);border-color:var(--accent)}}
.app-btn .app-icon{{font-size:20px;display:block;margin-bottom:2px;transition:transform .3s}}
.app-btn:hover .app-icon{{animation:emojiBounce .6s ease-in-out infinite}}
@keyframes emojiBounce{{0%,100%{{transform:translateY(0) scale(1)}}50%{{transform:translateY(-4px) scale(1.15)}}}}
.app-btn .app-name{{font-size:6px;color:var(--text2);font-weight:600;display:block}}
.app-btn .app-action{{font-size:5px;color:var(--text3);display:block;margin-top:1px}}
.app-btn .app-action.copy{{color:var(--accent2)}}

/* کانفیگ‌ها */
.configs-section{{margin:10px 0}}
.config-item{{display:flex;align-items:center;justify-content:space-between;background:rgba(139,92,246,0.02);border:1px solid var(--card-border);border-radius:8px;padding:6px 10px;margin-bottom:3px;transition:var(--transition)}}
.config-item:hover{{background:rgba(139,92,246,0.04)}}
.config-item .config-name{{font-size:9px;font-weight:600;color:var(--text)}}
.config-item .config-type{{font-size:7px;color:var(--text3);background:rgba(139,92,246,0.04);padding:1px 6px;border-radius:4px}}
.config-item .config-action{{font-size:8px;color:var(--accent2);cursor:pointer;transition:var(--transition)}}
.config-item .config-action:hover{{color:var(--accent)}}

/* دکمه‌ها */
.btn{{font-family:inherit;font-size:9px;font-weight:600;border-radius:6px;padding:5px 10px;cursor:pointer;display:inline-flex;align-items:center;gap:3px;border:none;transition:var(--transition);white-space:nowrap;justify-content:center}}
.btn i{{font-size:10px}}
.btn-success{{background:var(--green-bg);border:1px solid rgba(16,185,129,0.08);color:var(--green-text)}}
.btn-success:hover{{background:rgba(16,185,129,0.12);transform:translateY(-2px)}}
.btn-success.copied{{background:#059669;color:#fff;transform:scale(0.95)}}
.btn-secondary{{background:rgba(139,92,246,0.03);border:1px solid var(--card-border);color:var(--text2)}}
.btn-secondary:hover{{background:rgba(139,92,246,0.06);color:var(--text);transform:translateY(-2px)}}
.btn-gold{{background:linear-gradient(135deg,#8B5CF6,#6D28D9);color:#0a0714}}
.btn-gold:hover{{transform:translateY(-2px);box-shadow:0 4px 20px rgba(139,92,246,0.2)}}

.footer{{margin-top:12px;padding-top:10px;border-top:1px solid var(--card-border);text-align:center;font-size:6px;color:var(--text3)}}
.footer .brand-name{{color:var(--accent);font-weight:700}}

.toast{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(28px) saturate(160%);border:1px solid var(--card-border);color:var(--text);border-radius:8px;padding:6px 14px;font-size:9px;opacity:0;transition:var(--transition);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:4px}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(16,185,129,0.15);color:var(--green-text)}}

@media(max-width:400px){{.card{{padding:16px 12px;margin-top:70px}}.user-name{{font-size:17px}}.stats-card-grid{{gap:4px}}.stat-info-value{{font-size:13px}}.apps-grid{{grid-template-columns:repeat(4,1fr)}}.app-btn .app-icon{{font-size:16px}}}}
</style>
</head>
<body>
<div class="stars-container">
    <div class="star" style="width:2px;height:2px;top:8%;left:6%;animation-delay:0s"></div>
    <div class="star" style="width:3px;height:3px;top:25%;left:35%;animation-delay:1.5s"></div>
    <div class="star" style="width:1px;height:1px;top:45%;left:65%;animation-delay:0.8s"></div>
    <div class="star" style="width:2px;height:2px;top:65%;left:15%;animation-delay:2.2s"></div>
    <div class="star" style="width:3px;height:3px;top:80%;left:75%;animation-delay:0.5s"></div>
    <div class="star" style="width:1px;height:1px;top:35%;left:85%;animation-delay:1.8s"></div>
    <div class="star" style="width:2px;height:2px;top:55%;left:45%;animation-delay:2.5s"></div>
</div>
<div class="glow-orb glow-orb1"></div>
<div class="glow-orb glow-orb2"></div>
<div class="toast" id="toast"></div>

<div class="theme-dropdown">
    <button class="toggle-btn" onclick="toggleThemeMenu()">
        <span>🎨</span>
        <span id="themeDisplay">انتخاب تم</span>
        <span class="arrow" id="themeArrow">▾</span>
    </button>
    <div class="menu" id="themeMenu">
        {menu_items}
    </div>
</div>

<div class="card" id="mainCard">
    <!-- هدر -->
    <div class="card-header">
        <div class="brand">
            <div class="brand-icon">🏛️</div>
            <div>
                <div class="brand-text">تخت جمشید</div>
                <div class="brand-sub">اشتراک ویژه</div>
            </div>
        </div>
        <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn">🌙</button>
    </div>

    <!-- نام کاربر و وضعیت -->
    <div class="user-name-row">
        <div class="user-name">
            {label}
            <span class="proto-badge">{protocol_icon} {protocol_name} · {http_name}</span>
        </div>
        <span class="status-badge {'active' if is_allowed else 'inactive'}">
            <span class="status-dot {'green' if is_allowed else 'red'}"></span>
            {'فعال' if is_allowed else 'غیرفعال'}
        </span>
    </div>

    <!-- UUID -->
    <div class="uuid-box" onclick="copyUUID()">🔑 {uuid}</div>

    <!-- آمار مصرف -->
    <div class="stats-card-grid">
        <div class="stat-info-card">
            <div class="stat-info-label">📊 مصرف</div>
            <div class="stat-info-value used">{used_val} <span class="unit">{used_unit}</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📦 سهمیه</div>
            <div class="stat-info-value limit">{limit_val} <span class="unit">{limit_unit}</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">⏳ زمان باقی</div>
            <div class="stat-info-value">{days_left}</div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📱 دستگاه‌ها</div>
            <div class="stat-info-value">{str(max_devices) if max_devices > 0 else '∞'}</div>
        </div>
    </div>

    <!-- نوار پیشرفت -->
    <div class="progress-section">
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="progress-text">
            <span>میزان مصرف</span>
            <span class="pct">{percent:.1f}%</span>
        </div>
    </div>

    <!-- لینک ساب‌اسکریپشن -->
    <div class="sub-link-section">
        <div class="sub-link-label"><i class="ti ti-link"></i> لینک اشتراک</div>
        <div class="sub-link-url" id="subLink">{sub_url}</div>
        <div class="sub-link-actions">
            <button class="btn btn-success" onclick="copySub()" id="copySubBtn"><i class="ti ti-copy"></i> کپی لینک</button>
            <button class="btn btn-gold" onclick="window.open('{sub_url}', '_blank')"><i class="ti ti-external-link"></i> باز کردن</button>
        </div>
    </div>

    <!-- اپلیکیشن‌ها -->
    <div class="apps-section">
        <div class="apps-title"><i class="ti ti-devices"></i> نصب روی دستگاه‌ها</div>
        <div class="apps-grid">
            <div class="app-btn" onclick="openApp('hiddify')">
                <span class="app-icon">📱</span>
                <span class="app-name">Hiddify</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2rayng')">
                <span class="app-icon">📲</span>
                <span class="app-name">V2rayNG</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2box')">
                <span class="app-icon">📱</span>
                <span class="app-name">V2Box</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="copySub()">
                <span class="app-icon">📋</span>
                <span class="app-name">نکست‌وی‌پی‌ان</span>
                <span class="app-action copy">کپی لینک</span>
            </div>
            <div class="app-btn" onclick="openApp('clash')">
                <span class="app-icon">⚔️</span>
                <span class="app-name">Clash Meta</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('windows')">
                <span class="app-icon">🪟</span>
                <span class="app-name">Windows</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('macos')">
                <span class="app-icon">🍎</span>
                <span class="app-name">macOS</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('linux')">
                <span class="app-icon">🐧</span>
                <span class="app-name">Linux</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
        </div>
    </div>

    <!-- کانفیگ‌ها -->
    <div class="configs-section">
        <div class="config-item">
            <span class="config-name">{label}-Default</span>
            <span class="config-type">{protocol_name} · {http_name}</span>
            <span class="config-action" onclick="copyConfig('{vless_link}')">📋</span>
        </div>
    </div>

    <div class="footer">
        <span class="brand-name">🏛️ تخت جمشید</span> · نسخه ۱۴ · {protocol_icon} {protocol_name}
    </div>
</div>

<script>
const subUrl = `{sub_url}`;
const uuid = `{uuid}`;
const vlessLink = `{vless_link}`;
const isExpired = {str(not is_allowed).lower()};

function toast(msg, type) {{
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.className = 'toast show' + (type ? ' ' + type : '');
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('show'), 2000);
}}

function copySub() {{
    const btn = document.getElementById('copySubBtn');
    navigator.clipboard.writeText(subUrl).then(() => {{
        toast('✅ ساب‌لینک کپی شد!', 'ok');
        btn.classList.add('copied');
        btn.innerHTML = '<i class="ti ti-check"></i> کپی شد!';
        setTimeout(() => {{
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="ti ti-copy"></i> کپی لینک';
        }}, 1500);
    }}).catch(() => toast('❌ خطا در کپی', 'err'));
}}

function copyUUID() {{
    navigator.clipboard.writeText(uuid).then(() => toast('✅ کپی شد', 'ok'));
}}

function copyConfig(link) {{
    navigator.clipboard.writeText(link).then(() => toast('✅ کانفیگ کپی شد!', 'ok'));
}}

function openApp(app) {{
    const apps = {{
        'hiddify': 'https://github.com/hiddify/hiddify-app/releases',
        'v2rayng': 'https://github.com/2dust/v2rayNG/releases',
        'v2box': 'https://apps.apple.com/app/v2box/id6446814670',
        'clash': 'https://github.com/MetaCubeX/ClashMetaForAndroid/releases',
        'windows': 'https://github.com/2dust/v2rayN/releases',
        'macos': 'https://github.com/ShadowLaunch/ShadowLaunch/releases',
        'linux': 'https://github.com/SagerNet/sing-box/releases'
    }};
    const url = apps[app];
    if (url) {{
        window.open(url, '_blank');
    }} else {{
        toast('📋 لینک در کلیپ‌بورد', 'ok');
        copySub();
    }}
}}

// ===== مدیریت تم =====
let currentTheme = localStorage.getItem('persepolis-sub-theme') || 'persepolis_gold';
const themeList = ['persepolis_gold','persepolis_dark','persepolis_sun','persepolis_royal','persepolis_stone','persepolis_light','persepolis_warm','persepolis_cool','persepolis_ancient','persepolis_modern'];
const themeNames = {{
    'persepolis_gold':'🏛️ طلایی',
    'persepolis_dark':'🌙 شب',
    'persepolis_sun':'☀️ آفتاب',
    'persepolis_royal':'👑 سلطنتی',
    'persepolis_stone':'🗿 سنگی',
    'persepolis_light':'✨ روشن',
    'persepolis_warm':'🔥 گرم',
    'persepolis_cool':'❄️ خنک',
    'persepolis_ancient':'🏺 کهن',
    'persepolis_modern':'💎 مدرن'
}};

function applyTheme(theme) {{
    currentTheme = theme;
    localStorage.setItem('persepolis-sub-theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.getElementById('themeDisplay').textContent = themeNames[theme] || 'انتخاب تم';
    document.querySelectorAll('.theme-dropdown .menu-item').forEach(el => {{
        el.classList.toggle('active', el.dataset.theme === theme);
    }});
    document.getElementById('themeMenu').classList.remove('open');
    document.getElementById('themeArrow').classList.remove('open');
    document.getElementById('themeBtn').textContent = theme.includes('light') ? '🌙' : '☀️';
}}

function toggleThemeMenu() {{
    const menu = document.getElementById('themeMenu');
    const arrow = document.getElementById('themeArrow');
    menu.classList.toggle('open');
    arrow.classList.toggle('open');
}}

function selectTheme(theme) {{
    applyTheme(theme);
    toast('✅ ' + themeNames[theme], 'ok');
}}

function toggleTheme() {{
    const current = currentTheme;
    const idx = themeList.indexOf(current);
    const next = themeList[(idx + 1) % themeList.length];
    selectTheme(next);
}}

document.addEventListener('click', function(e) {{
    const dropdown = document.querySelector('.theme-dropdown');
    if (dropdown && !dropdown.contains(e.target)) {{
        document.getElementById('themeMenu').classList.remove('open');
        document.getElementById('themeArrow').classList.remove('open');
    }}
}});

applyTheme(currentTheme);

// انیمیشن نوار پیشرفت
setTimeout(() => {{
    const fill = document.getElementById('progressFill');
    if (fill) fill.style.width = '{percent:.1f}%';
}}, 100);
</script>
</body></html>"""
