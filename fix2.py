with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── FIX 1: JS ID mismatches ──────────────────────────────────
content = content.replace(
    "const wrap = document.getElementById('field-btns');",
    "const wrap = document.getElementById('field-scroll');"
)
content = content.replace(
    "document.getElementById('field-content').innerHTML = `",
    "document.getElementById('phone-topics').innerHTML = `"
)

# ── FIX 2: Replace static calendar card with dynamic container ─
OLD_CAL = '''    <div class="card">
      <div style="font-size:13px;font-weight:800;color:#fff;margin-bottom:10px;">🗓 2026年5月</div>
      <div class="cal-grid">
        <div class="cal-hdr">日</div><div class="cal-hdr">一</div><div class="cal-hdr">二</div>
        <div class="cal-hdr wed">三🎓</div><div class="cal-hdr">四</div><div class="cal-hdr">五</div><div class="cal-hdr">六</div>
        <!-- Row 1 -->
        <div class="cal-cell"></div><div class="cal-cell"></div><div class="cal-cell"></div>
        <div class="cal-cell"></div><div class="cal-cell"></div>
        <div class="cal-cell"><span class="cal-num">1</span></div>
        <div class="cal-cell"><span class="cal-num">2</span></div>
        <!-- Row 2 -->
        <div class="cal-cell"><span class="cal-num">3</span></div><div class="cal-cell"><span class="cal-num">4</span></div>
        <div class="cal-cell"><span class="cal-num">5</span></div><div class="cal-cell wed-day"><span class="cal-num">6</span><div class="ev-dot wed"></div></div>
        <div class="cal-cell"><span class="cal-num">7</span></div>
        <div class="cal-cell has-ev"><span class="cal-num">8</span><div class="ev-dot"></div></div>
        <div class="cal-cell has-ev"><span class="cal-num">9</span><div class="ev-dot"></div></div>
        <!-- Row 3 -->
        <div class="cal-cell"><span class="cal-num">10</span></div><div class="cal-cell"><span class="cal-num">11</span></div>
        <div class="cal-cell"><span class="cal-num">12</span></div><div class="cal-cell wed-day"><span class="cal-num">13</span><div class="ev-dot wed"></div></div>
        <div class="cal-cell"><span class="cal-num">14</span></div>
        <div class="cal-cell"><span class="cal-num">15</span></div><div class="cal-cell"><span class="cal-num">16</span></div>
        <!-- Row 4 -->
        <div class="cal-cell"><span class="cal-num">17</span></div>
        <div class="cal-cell today"><span class="cal-num">18</span></div>
        <div class="cal-cell"><span class="cal-num">19</span></div>
        <div class="cal-cell wed-day"><span class="cal-num">20</span><div class="ev-dot wed"></div></div>
        <div class="cal-cell"><span class="cal-num">21</span></div>
        <div class="cal-cell"><span class="cal-num">22</span></div>
        <div class="cal-cell has-ev"><span class="cal-num">23</span><div class="ev-dot"></div></div>
        <!-- Row 5 -->
        <div class="cal-cell"><span class="cal-num">24</span></div>
        <div class="cal-cell"><span class="cal-num">25</span></div>
        <div class="cal-cell"><span class="cal-num">26</span></div>
        <div class="cal-cell wed-day"><span class="cal-num">27</span><div class="ev-dot wed"></div></div>
        <div class="cal-cell"><span class="cal-num">28</span></div>
        <div class="cal-cell"><span class="cal-num">29</span></div>
        <div class="cal-cell has-ev"><span class="cal-num">30</span><div class="ev-dot"></div></div>
        <!-- Row 6 -->
        <div class="cal-cell"><span class="cal-num">31</span></div>
      </div>
      <div style="display:flex;gap:12px;font-size:10px;color:#7070a0;margin-top:4px;">
        <span>🔴 周三 = 线上课</span><span>🔵 = 实体课程/活动</span><span>🟣 = 今天</span>
      </div>
    </div>'''

NEW_CAL = '    <div id="cal-container"></div>'

content = content.replace(OLD_CAL, NEW_CAL)

# ── FIX 3: Inject renderCalendar JS before DOMContentLoaded ──
CAL_JS = r"""
// ===== DYNAMIC CALENDAR =====
const CAL_MONTHS = [
  { year:2026, month:4, label:'2026年5月', startDay:5, days:31,  // May: starts Fri
    events:{8:'课',9:'课',23:'课',30:'课'},
    ig:[4,18]
  },
  { year:2026, month:5, label:'2026年6月', startDay:1, days:30,  // June: starts Mon
    events:{6:'慈',21:'课',27:'课'},
    ig:[1,15,29]
  },
  { year:2026, month:6, label:'2026年7月', startDay:3, days:31,  // July: starts Wed
    events:{3:'课',4:'课',5:'课',11:'课',18:'营',19:'营',25:'课'},
    ig:[13,27]
  }
];
let calIdx = 0;

function renderCalendar(){
  const m = CAL_MONTHS[calIdx];
  const today = new Date();
  const todayD = (today.getFullYear()===2026 && today.getMonth()===m.month) ? today.getDate() : -1;

  // Build day cells
  let cells = '';
  // empty leading cells
  for(let i=0;i<m.startDay;i++) cells += '<div class="cal-cell"></div>';
  for(let d=1;d<=m.days;d++){
    const dow = (m.startDay + d - 1) % 7; // 0=Sun,3=Wed
    const isWed = dow === 3;
    const hasEv = m.events[d];
    const isIg = m.ig.includes(d);
    const isToday = d === todayD;
    let cls = 'cal-cell';
    if(isWed) cls += ' wed-day';
    if(hasEv) cls += ' has-ev';
    if(isToday) cls += ' today';
    let dots = '';
    if(isWed) dots += '<div class="ev-dot wed"></div>';
    if(hasEv && !isWed) dots += '<div class="ev-dot"></div>';
    if(isIg) dots += '<div class="ev-dot ig"></div>';
    cells += `<div class="${cls}"><span class="cal-num">${d}</span>${dots}</div>`;
  }

  document.getElementById('cal-container').innerHTML = `
    <div class="card" style="padding:14px;">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">
        <button onclick="calNav(-1)" style="background:rgba(255,255,255,0.1);border:none;border-radius:50%;width:32px;height:32px;color:#fff;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">${calIdx===0?'<span style=opacity:.3>‹</span>':'‹'}</button>
        <div style="font-size:14px;font-weight:800;color:#fff;">🗓 ${m.label}</div>
        <button onclick="calNav(1)" style="background:rgba(255,255,255,0.1);border:none;border-radius:50%;width:32px;height:32px;color:#fff;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;">${calIdx===CAL_MONTHS.length-1?'<span style=opacity:.3>›</span>':'›'}</button>
      </div>
      <div class="cal-grid">
        <div class="cal-hdr">日</div><div class="cal-hdr">一</div><div class="cal-hdr">二</div>
        <div class="cal-hdr wed">三🎓</div><div class="cal-hdr">四</div><div class="cal-hdr">五</div><div class="cal-hdr">六</div>
        ${cells}
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:10px;font-size:10px;color:#7070a0;margin-top:8px;">
        <span>🔴 周三线上课</span>
        <span>🔵 实体活动</span>
        <span style="color:#22d3ee;">🔵 IG数据上传</span>
        <span>🟣 今天</span>
      </div>
    </div>`;
}

function calNav(dir){
  const next = calIdx + dir;
  if(next < 0 || next >= CAL_MONTHS.length) return;
  calIdx = next;
  renderCalendar();
}

"""

content = content.replace(
    "window.addEventListener('DOMContentLoaded', ()=>{",
    CAL_JS + "window.addEventListener('DOMContentLoaded', ()=>{"
)

# ── FIX 4: Add renderCalendar() to DOMContentLoaded ──────────
content = content.replace(
    "window.addEventListener('DOMContentLoaded', ()=>{\n  renderFieldButtons();\n  renderContent();\n  renderTopicCats();\n  renderTopics('plate');\n});",
    "window.addEventListener('DOMContentLoaded', ()=>{\n  renderFieldButtons();\n  renderContent();\n  renderTopicCats();\n  renderTopics('plate');\n  renderCalendar();\n});"
)

# ── FIX 5: Add .ev-dot.ig CSS (cyan) ─────────────────────────
content = content.replace(
    ".ev-dot.wed{background:#ff6496;}",
    ".ev-dot.wed{background:#ff6496;}\n.ev-dot.ig{width:4px;height:4px;border-radius:50%;background:#22d3ee;margin-top:1px;}"
)

with open('instagram_growth_mobile.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
# Verify
import subprocess
r1 = subprocess.run(['grep','-c','field-scroll','instagram_growth_mobile.html'],capture_output=True,text=True)
r2 = subprocess.run(['grep','-c','phone-topics','instagram_growth_mobile.html'],capture_output=True,text=True)
r3 = subprocess.run(['grep','-c','cal-container','instagram_growth_mobile.html'],capture_output=True,text=True)
r4 = subprocess.run(['grep','-c','renderCalendar','instagram_growth_mobile.html'],capture_output=True,text=True)
r5 = subprocess.run(['grep','-c','ev-dot.ig','instagram_growth_mobile.html'],capture_output=True,text=True)
print(f"field-scroll refs: {r1.stdout.strip()}")
print(f"phone-topics refs: {r2.stdout.strip()}")
print(f"cal-container refs: {r3.stdout.strip()}")
print(f"renderCalendar refs: {r4.stdout.strip()}")
print(f"ev-dot.ig refs: {r5.stdout.strip()}")
