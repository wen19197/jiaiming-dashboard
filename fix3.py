with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Replace renderContent (号码选题) with dark expandable cards ──
OLD_RC = """function renderContent(){
  const f = FIELDS[currentField];
  const items = f[currentMode];
  const colorMap = {'best':'#16a34a','worst':'#dc2626'};
  const col = colorMap[currentMode];
  document.getElementById('phone-topics').innerHTML = `
    <div style="display:flex;gap:8px;margin-bottom:12px;">
      <button id="btn-best" onclick="setMode('best')" style="flex:1;padding:8px;border:none;border-radius:10px;font-weight:700;font-size:14px;cursor:pointer;transition:.2s;background:${currentMode==='best'?'#22c55e':'#e8e8e8'};color:${currentMode==='best'?'#fff':'#555'}">✅ 吉星案例</button>
      <button id="btn-worst" onclick="setMode('worst')" style="flex:1;padding:8px;border:none;border-radius:10px;font-weight:700;font-size:14px;cursor:pointer;transition:.2s;background:${currentMode==='worst'?'#ef4444':'#e8e8e8'};color:${currentMode==='worst'?'#fff':'#555'}">⚠️ 凶星案例</button>
    </div>
    <div style="background:${f.color}18;border-left:4px solid ${f.color};border-radius:0 10px 10px 0;padding:10px 12px;margin-bottom:12px;">
      <div style="font-weight:700;color:${f.color};font-size:15px;">${f.name} — ${currentMode==='best'?'吉星开场':'凶星开场'}</div>
      <div style="font-size:12px;color:#666;margin-top:3px;">点击案例复制开场白</div>
    </div>
    ${items.map((item,i)=>`
      <div onclick="navigator.clipboard&&navigator.clipboard.writeText('我认识一个人：${item.replace(/'/g,"\\'")}').then(()=>alert('已复制！'))" style="background:#fff;border:1px solid ${col}33;border-radius:10px;padding:10px 12px;margin-bottom:8px;cursor:pointer;display:flex;align-items:flex-start;gap:8px;">
        <span style="color:${col};font-weight:700;min-width:22px;">${i+1}.</span>
        <span style="color:#333;font-size:14px;line-height:1.5;">${item}</span>
      </div>
    `).join('')}
  `;
}"""

NEW_RC = """function togglePhone(uid){
  const body = document.getElementById('pb-'+uid);
  if(!body) return;
  body.classList.toggle('open');
  const arr = document.getElementById('pa-'+uid);
  if(arr) arr.textContent = body.classList.contains('open') ? '▲' : '▼';
}

function renderContent(){
  const f = FIELDS[currentField];
  const items = f[currentMode];
  const isBest = currentMode === 'best';
  const col = isBest ? '#22c55e' : '#ef4444';
  const label = isBest ? '吉星开场' : '凶星开场';
  document.getElementById('phone-topics').innerHTML = `
    <div style="display:flex;gap:8px;margin-bottom:14px;">
      <button id="btn-best" onclick="setMode('best')" style="flex:1;padding:9px;border:none;border-radius:12px;font-weight:700;font-size:13px;cursor:pointer;transition:.2s;background:${isBest?'#22c55e':'rgba(255,255,255,0.08)'};color:${isBest?'#fff':'rgba(255,255,255,0.5)'}">✅ 吉星案例</button>
      <button id="btn-worst" onclick="setMode('worst')" style="flex:1;padding:9px;border:none;border-radius:12px;font-weight:700;font-size:13px;cursor:pointer;transition:.2s;background:${!isBest?'#ef4444':'rgba(255,255,255,0.08)'};color:${!isBest?'#fff':'rgba(255,255,255,0.5)'}">⚠️ 凶星案例</button>
    </div>
    <div style="background:${f.color}22;border-left:4px solid ${f.color};border-radius:0 12px 12px 0;padding:10px 14px;margin-bottom:14px;">
      <div style="font-weight:800;color:${f.color};font-size:15px;">${f.name} — ${label}</div>
      <div style="font-size:11px;color:rgba(255,255,255,0.4);margin-top:3px;">点击展开 · 复制开场白</div>
    </div>
    ${items.map((item,i)=>{
      const uid = 'ph_'+currentField+'_'+currentMode+'_'+i;
      const preview = item.length>22 ? item.slice(0,22)+'…' : item;
      return `
      <div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:14px;margin-bottom:10px;overflow:hidden;">
        <button onclick="togglePhone('${uid}')" style="display:flex;align-items:center;justify-content:space-between;width:100%;padding:14px;background:none;border:none;font-family:inherit;cursor:pointer;text-align:left;gap:8px;">
          <div style="flex:1;min-width:0;">
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
              <span style="background:${col};color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;flex-shrink:0;">${i+1}</span>
              <span style="font-size:12px;color:${col};font-weight:700;">${isBest?'✅ 吉星场景':'⚠️ 凶星场景'}</span>
            </div>
            <div style="font-size:13px;color:rgba(255,255,255,0.75);line-height:1.4;padding-left:30px;">${preview}</div>
          </div>
          <span id="pa-${uid}" style="color:${f.color};font-size:11px;flex-shrink:0;">▼</span>
        </button>
        <div id="pb-${uid}" class="boom-body">
          <div style="padding:0 14px 14px;padding-left:30px;">
            <div style="background:rgba(255,255,255,0.05);border-radius:10px;padding:12px;margin-bottom:10px;">
              <div style="font-size:13px;color:rgba(255,255,255,0.9);line-height:1.6;">${item}</div>
            </div>
            <div style="display:flex;gap:8px;margin-bottom:10px;">
              <button onclick="navigator.clipboard&&navigator.clipboard.writeText('${item.replace(/'/g,"\\'").replace(/`/g,'\\`')}').then(()=>alert('已复制！'))" style="flex:1;padding:8px;background:${f.color};border:none;border-radius:10px;color:#fff;font-size:12px;font-weight:700;cursor:pointer;">📋 复制开场白</button>
            </div>
            <div style="background:rgba(255,255,255,0.04);border-radius:8px;padding:8px 10px;">
              <div style="font-size:10px;color:rgba(255,255,255,0.4);font-weight:700;margin-bottom:4px;">📝 脚本结构</div>
              <div style="font-size:11px;color:rgba(255,255,255,0.5);line-height:1.6;">开场情景 → 引入${f.name}概念 → 数字解读 → 改运建议 → 互动钩子</div>
            </div>
          </div>
        </div>
      </div>`;
    }).join('')}
  `;
}"""

content = content.replace(OLD_RC, NEW_RC)

# ── Replace renderTopicCats: dark theme for inactive buttons ──
OLD_CATS = """function renderTopicCats(){
  const bar = document.getElementById('cat-filter-bar');
  if(!bar) return;
  bar.innerHTML = TOPIC_CATS.map(c=>`
    <button class="cat-f-btn${c.id===currentCat?' active':''}"
      style="background:${c.id===currentCat?c.color:'#f0f0f0'};color:${c.id===currentCat?'#fff':'#555'};border:none;border-radius:10px;padding:6px 14px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;"
      onclick="switchCat('${c.id}')">${c.name}</button>
  `).join('');
}"""

NEW_CATS = """function renderTopicCats(){
  const bar = document.getElementById('cat-filter-bar');
  if(!bar) return;
  bar.innerHTML = TOPIC_CATS.map(c=>`
    <button class="cat-f-btn${c.id===currentCat?' active':''}"
      style="background:${c.id===currentCat?c.color:'rgba(255,255,255,0.1)'};color:${c.id===currentCat?'#fff':'rgba(255,255,255,0.6)'};border:1px solid ${c.id===currentCat?c.color:'rgba(255,255,255,0.15)'};border-radius:20px;padding:7px 16px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;transition:.2s;"
      onclick="switchCat('${c.id}')">${c.name}</button>
  `).join('');
}"""

content = content.replace(OLD_CATS, NEW_CATS)

# ── Replace renderTopics: full dark theme ──────────────────────
OLD_TOPICS = """function renderTopics(catId){
  const sec = document.getElementById('topic-sections');
  if(!sec) return;
  const items = TOPIC_DATA.filter(t=>t.cat===catId);
  const cat = TOPIC_CATS.find(c=>c.id===catId)||{color:'#ff6496'};
  if(!items.length){ sec.innerHTML='<p style="text-align:center;color:#aaa;padding:20px;">暂无选题</p>'; return; }
  sec.innerHTML = items.map((t,i)=>{
    const uid = catId+'_'+i;
    return `
    <div style="background:#fff;border-radius:14px;box-shadow:0 2px 10px rgba(0,0,0,.07);margin-bottom:12px;overflow:hidden;">
      <button class="boom-toggle" onclick="toggleBoom('${uid}')" style="display:flex;align-items:center;justify-content:space-between;width:100%;padding:14px;background:none;border:none;font-family:inherit;cursor:pointer;text-align:left;">
        <div>
          <div style="font-weight:700;color:#1a1a1a;font-size:14px;">${t.title}</div>
          <div style="font-size:11px;color:#999;margin-top:3px;">展开查看 8 种爆款开场白</div>
        </div>
        <span id="arr-${uid}" style="color:${cat.color};font-size:12px;margin-left:8px;">▼</span>
      </button>
      <div id="boom-${uid}" class="boom-body">
        <div style="padding:0 14px 14px;">
          ${t.hooks.map(h=>`
            <div class="boom-row" style="display:flex;gap:8px;padding:8px;background:#f8f8f8;border-radius:8px;margin-bottom:6px;cursor:pointer;" 
              onclick="navigator.clipboard&&navigator.clipboard.writeText('${h.text.replace(/'/g,"\\'")}').then(()=>alert('已复制！'))">
              <span style="background:${cat.color};color:#fff;border-radius:6px;padding:2px 7px;font-size:11px;font-weight:700;white-space:nowrap;flex-shrink:0;">${h.elem}</span>
              <span style="font-size:13px;color:#333;line-height:1.5;">${h.text}</span>
            </div>
          `).join('')}
        </div>
      </div>
    </div>`;
  }).join('');
}"""

NEW_TOPICS = """function renderTopics(catId){
  const sec = document.getElementById('topic-sections');
  if(!sec) return;
  const items = TOPIC_DATA.filter(t=>t.cat===catId);
  const cat = TOPIC_CATS.find(c=>c.id===catId)||{color:'#ff6496'};
  if(!items.length){ sec.innerHTML='<p style="text-align:center;color:rgba(255,255,255,0.3);padding:20px;">暂无选题</p>'; return; }
  sec.innerHTML = items.map((t,i)=>{
    const uid = catId+'_'+i;
    return `
    <div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:16px;margin-bottom:12px;overflow:hidden;">
      <button class="boom-toggle" onclick="toggleBoom('${uid}')" style="display:flex;align-items:center;justify-content:space-between;width:100%;padding:16px;background:none;border:none;font-family:inherit;cursor:pointer;text-align:left;gap:10px;">
        <div style="flex:1;min-width:0;">
          <div style="font-weight:700;color:#fff;font-size:14px;line-height:1.4;">${t.title}</div>
          <div style="font-size:11px;color:rgba(255,255,255,0.35);margin-top:4px;">展开查看 8 种爆款开场白 · 点击直接复制</div>
        </div>
        <span id="arr-${uid}" style="color:${cat.color};font-size:13px;flex-shrink:0;background:${cat.color}22;border-radius:50%;width:24px;height:24px;display:flex;align-items:center;justify-content:center;">▼</span>
      </button>
      <div id="boom-${uid}" class="boom-body">
        <div style="padding:0 14px 14px;">
          <div style="height:1px;background:rgba(255,255,255,0.08);margin-bottom:12px;"></div>
          ${t.hooks.map(h=>`
            <div style="display:flex;gap:8px;padding:10px;background:rgba(255,255,255,0.04);border-radius:10px;margin-bottom:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);transition:.15s;"
              onclick="navigator.clipboard&&navigator.clipboard.writeText('${h.text.replace(/'/g,"\\'")}').then(()=>alert('已复制！'))">
              <span style="background:${cat.color};color:#fff;border-radius:8px;padding:3px 8px;font-size:10px;font-weight:800;white-space:nowrap;flex-shrink:0;height:fit-content;">${h.elem}</span>
              <span style="font-size:13px;color:rgba(255,255,255,0.8);line-height:1.55;">${h.text}</span>
            </div>
          `).join('')}
        </div>
      </div>
    </div>`;
  }).join('');
}"""

content = content.replace(OLD_TOPICS, NEW_TOPICS)

with open('instagram_growth_mobile.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify all replacements worked
import subprocess
checks = [
    ('renderTopics replaced', 'rgba(255,255,255,0.06).*border-radius:16px', True),
    ('renderContent replaced', 'togglePhone', True),
    ('renderTopicCats dark', 'rgba(255,255,255,0.1)', True),
    ('old white card gone', "background:#fff;border-radius:14px;box-shadow", False),
]
for name, pat, should_exist in checks:
    r = subprocess.run(['grep','-c', pat, 'instagram_growth_mobile.html'], capture_output=True, text=True)
    count = int(r.stdout.strip() or 0)
    ok = (count > 0) == should_exist
    print(f"{'✅' if ok else '❌'} {name}: count={count}")

print(f"\nTotal lines: {sum(1 for _ in open('instagram_growth_mobile.html'))}")
