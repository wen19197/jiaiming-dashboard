with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── FIX 1: Add .f-btn CSS (add after .field-btn lines) ────────
OLD_CSS = '.field-btn.active { color:#fff; transform:scale(1.04); }'
NEW_CSS = '''.field-btn.active { color:#fff; transform:scale(1.04); }
.f-btn { flex-shrink:0; border:2px solid transparent; border-radius:20px; padding:6px 14px; font-size:12px; font-weight:700; cursor:pointer; background:transparent; font-family:inherit; white-space:nowrap; transition:all .2s; }
.f-btn.active { transform:scale(1.04); }'''
content = content.replace(OLD_CSS, NEW_CSS)

# ── FIX 2: Add renderCalendar + CAL_MONTHS before DOMContentLoaded ──
CAL_CODE = """
// ===== DYNAMIC CALENDAR =====
var calIdx = 0;
var CAL_MONTHS = [
  { label:'2026年5月', startDay:5, days:31,
    events:{8:1,9:1,23:1,30:1}, wed:[6,13,20,27], ig:[4,18] },
  { label:'2026年6月', startDay:1, days:30,
    events:{6:1,21:1,27:1}, wed:[3,10,17,24], ig:[1,15,29] },
  { label:'2026年7月', startDay:3, days:31,
    events:{3:1,4:1,5:1,11:1,18:1,19:1,25:1}, wed:[1,8,15,22,29], ig:[13,27] }
];

function renderCalendar(){
  var wrap = document.getElementById('cal-container');
  if(!wrap) return;
  var m = CAL_MONTHS[calIdx];
  var today = new Date();
  var todayD = (today.getFullYear()===2026 && today.getMonth()===(4+calIdx)) ? today.getDate() : -1;
  var cells = '';
  for(var k=0;k<m.startDay;k++) cells += '<div class="cal-cell"></div>';
  for(var d=1;d<=m.days;d++){
    var dow = (m.startDay + d - 1) % 7;
    var isWed = m.wed.indexOf(d) >= 0;
    var hasEv = m.events[d];
    var isIg  = m.ig.indexOf(d) >= 0;
    var isToday = d === todayD;
    var cls = 'cal-cell' + (isWed?' wed-day':'') + (hasEv?' has-ev':'') + (isToday?' today':'');
    var dots = '';
    if(isWed) dots += '<div class="ev-dot wed"></div>';
    else if(hasEv) dots += '<div class="ev-dot"></div>';
    if(isIg) dots += '<div class="ev-dot ig"></div>';
    cells += '<div class="'+cls+'"><span class="cal-num">'+d+'</span>'+dots+'</div>';
  }
  var prevBtn = calIdx===0
    ? '<button style="background:rgba(255,255,255,0.05);border:none;border-radius:50%;width:34px;height:34px;color:rgba(255,255,255,0.2);font-size:18px;cursor:default;display:flex;align-items:center;justify-content:center;">‹</button>'
    : '<button onclick="calNav(-1)" style="background:rgba(255,255,255,0.12);border:none;border-radius:50%;width:34px;height:34px;color:#fff;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">‹</button>';
  var nextBtn = calIdx===CAL_MONTHS.length-1
    ? '<button style="background:rgba(255,255,255,0.05);border:none;border-radius:50%;width:34px;height:34px;color:rgba(255,255,255,0.2);font-size:18px;cursor:default;display:flex;align-items:center;justify-content:center;">›</button>'
    : '<button onclick="calNav(1)" style="background:rgba(255,255,255,0.12);border:none;border-radius:50%;width:34px;height:34px;color:#fff;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">›</button>';
  wrap.innerHTML =
    '<div class="card" style="padding:14px;">' +
      '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">' +
        prevBtn +
        '<div style="font-size:14px;font-weight:800;color:#fff;">🗓 '+m.label+'</div>' +
        nextBtn +
      '</div>' +
      '<div class="cal-grid">' +
        '<div class="cal-hdr">日</div><div class="cal-hdr">一</div><div class="cal-hdr">二</div>' +
        '<div class="cal-hdr wed">三🎓</div><div class="cal-hdr">四</div><div class="cal-hdr">五</div><div class="cal-hdr">六</div>' +
        cells +
      '</div>' +
      '<div style="display:flex;flex-wrap:wrap;gap:10px;font-size:10px;color:#7070a0;margin-top:8px;">' +
        '<span>🔴 周三线上课</span>' +
        '<span>🔵 实体活动</span>' +
        '<span style="color:#22d3ee;">🩵 IG数据上传</span>' +
        '<span>🟣 今天</span>' +
      '</div>' +
    '</div>';
}

function calNav(dir){
  var next = calIdx + dir;
  if(next < 0 || next >= CAL_MONTHS.length) return;
  calIdx = next;
  renderCalendar();
}

"""

content = content.replace(
    "\nwindow.addEventListener('DOMContentLoaded'",
    CAL_CODE + "\nwindow.addEventListener('DOMContentLoaded'"
)

with open('instagram_growth_mobile.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
import subprocess, re
with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    html = f.read()
m = re.search(r'<script>(.*)</script>', html, re.DOTALL)
with open('/tmp/chk.js','w') as f:
    f.write(m.group(1))
r = subprocess.run(['node','--check','/tmp/chk.js'], capture_output=True, text=True)
print('JS:', 'OK ✅' if r.returncode==0 else r.stderr[:400])

checks = ['function renderCalendar','CAL_MONTHS','\.f-btn {','calNav','</html>']
for c in checks:
    import re as re2
    found = len(re2.findall(c, html))
    print(f'  {c}: {found}')
print(f'Lines: {html.count(chr(10))}')
