with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# renderContent: lines 1317-1438 (0-indexed: 1316-1437)
# renderTopicCats: lines 1439-1454 (0-indexed: 1438-1453)
# toggleBoom: lines 1455-1462 (0-indexed: 1454-1461)
# renderTopics: lines 1463-1566 (0-indexed: 1462-1565)
# DOMContentLoaded: line 1567+

BEFORE_RC   = lines[:1316]   # everything before renderContent
AFTER_TOPICS = lines[1565:]   # everything from window.addEventListener onwards

NEW_FUNCTIONS = """\
function togglePhone(uid){
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
  document.getElementById('phone-topics').innerHTML =
    '<div style="display:flex;gap:8px;margin-bottom:14px;">' +
      '<button id="btn-best" onclick="setMode(\'best\')" style="flex:1;padding:9px;border:none;border-radius:12px;font-weight:700;font-size:13px;cursor:pointer;background:' + (isBest?'#22c55e':'rgba(255,255,255,0.08)') + ';color:' + (isBest?'#fff':'rgba(255,255,255,0.5)') + '">✅ 吉星案例</button>' +
      '<button id="btn-worst" onclick="setMode(\'worst\')" style="flex:1;padding:9px;border:none;border-radius:12px;font-weight:700;font-size:13px;cursor:pointer;background:' + (!isBest?'#ef4444':'rgba(255,255,255,0.08)') + ';color:' + (!isBest?'#fff':'rgba(255,255,255,0.5)') + '">⚠️ 凶星案例</button>' +
    '</div>' +
    '<div style="background:' + f.color + '22;border-left:4px solid ' + f.color + ';border-radius:0 12px 12px 0;padding:10px 14px;margin-bottom:14px;">' +
      '<div style="font-weight:800;color:' + f.color + ';font-size:15px;">' + f.name + ' — ' + label + '</div>' +
      '<div style="font-size:11px;color:rgba(255,255,255,0.4);margin-top:3px;">点击展开 · 复制开场白</div>' +
    '</div>' +
    items.map(function(item,i){
      var uid = 'ph_' + currentField + '_' + currentMode + '_' + i;
      var preview = item.length > 22 ? item.slice(0,22) + '…' : item;
      return '<div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:14px;margin-bottom:10px;overflow:hidden;">' +
        '<button onclick="togglePhone(' + "'" + uid + "'" + ')" style="display:flex;align-items:center;justify-content:space-between;width:100%;padding:14px;background:none;border:none;font-family:inherit;cursor:pointer;text-align:left;gap:8px;">' +
          '<div style="flex:1;min-width:0;">' +
            '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">' +
              '<span style="background:' + col + ';color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;flex-shrink:0;">' + (i+1) + '</span>' +
              '<span style="font-size:12px;color:' + col + ';font-weight:700;">' + (isBest ? '✅ 吉星场景' : '⚠️ 凶星场景') + '</span>' +
            '</div>' +
            '<div style="font-size:13px;color:rgba(255,255,255,0.75);line-height:1.4;padding-left:30px;">' + preview + '</div>' +
          '</div>' +
          '<span id="pa-' + uid + '" style="color:' + f.color + ';font-size:11px;flex-shrink:0;">▼</span>' +
        '</button>' +
        '<div id="pb-' + uid + '" class="boom-body">' +
          '<div style="padding:0 14px 14px 14px;">' +
            '<div style="background:rgba(255,255,255,0.05);border-radius:10px;padding:12px;margin-bottom:10px;">' +
              '<div style="font-size:13px;color:rgba(255,255,255,0.9);line-height:1.6;">' + item + '</div>' +
            '</div>' +
            '<button onclick="navigator.clipboard&&navigator.clipboard.writeText(' + "'" + item.replace(/'/g,"\\'") + "'" + ').then(function(){alert(' + "'已复制！'" + ')})" style="width:100%;padding:9px;background:' + f.color + ';border:none;border-radius:10px;color:#fff;font-size:13px;font-weight:700;cursor:pointer;margin-bottom:10px;">📋 复制开场白</button>' +
            '<div style="background:rgba(255,255,255,0.04);border-radius:8px;padding:8px 10px;">' +
              '<div style="font-size:10px;color:rgba(255,255,255,0.4);font-weight:700;margin-bottom:4px;">📝 脚本结构</div>' +
              '<div style="font-size:11px;color:rgba(255,255,255,0.45);line-height:1.6;">开场情景 → 引入' + f.name + '概念 → 数字解读 → 改运建议 → 互动钩子</div>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</div>';
    }).join('');
}

function renderTopicCats(){
  const bar = document.getElementById('cat-filter-bar');
  if(!bar) return;
  bar.innerHTML = TOPIC_CATS.map(function(c){
    var active = c.id === currentCat;
    return '<button class="cat-f-btn' + (active?' active':'') + '"' +
      ' style="background:' + (active?c.color:'rgba(255,255,255,0.1)') + ';color:' + (active?'#fff':'rgba(255,255,255,0.6)') + ';border:1px solid ' + (active?c.color:'rgba(255,255,255,0.15)') + ';border-radius:20px;padding:7px 16px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;transition:.2s;"' +
      ' onclick="switchCat(' + "'" + c.id + "'" + ')">' + c.name + '</button>';
  }).join('');
}

function switchCat(catId){
  currentCat = catId;
  renderTopicCats();
  renderTopics(catId);
}

function toggleBoom(id){
  const body = document.getElementById('boom-'+id);
  if(!body) return;
  body.classList.toggle('open');
  const arrow = document.getElementById('arr-'+id);
  if(arrow) arrow.textContent = body.classList.contains('open') ? '▲' : '▼';
}

function renderTopics(catId){
  const sec = document.getElementById('topic-sections');
  if(!sec) return;
  const items = TOPIC_DATA.filter(function(t){ return t.cat===catId; });
  const cat = TOPIC_CATS.find(function(c){ return c.id===catId; })||{color:'#ff6496'};
  if(!items.length){ sec.innerHTML='<p style="text-align:center;color:rgba(255,255,255,0.3);padding:20px;">暂无选题</p>'; return; }
  sec.innerHTML = items.map(function(t,i){
    const uid = catId+'_'+i;
    return '<div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:16px;margin-bottom:12px;overflow:hidden;">' +
      '<button class="boom-toggle" onclick="toggleBoom(' + "'" + uid + "'" + ')" style="display:flex;align-items:center;justify-content:space-between;width:100%;padding:16px;background:none;border:none;font-family:inherit;cursor:pointer;text-align:left;gap:10px;">' +
        '<div style="flex:1;min-width:0;">' +
          '<div style="font-weight:700;color:#fff;font-size:14px;line-height:1.4;">' + t.title + '</div>' +
          '<div style="font-size:11px;color:rgba(255,255,255,0.35);margin-top:4px;">展开查看 8 种爆款开场白 · 点击直接复制</div>' +
        '</div>' +
        '<span id="arr-' + uid + '" style="color:' + cat.color + ';font-size:12px;flex-shrink:0;background:' + cat.color + '22;border-radius:50%;width:26px;height:26px;display:flex;align-items:center;justify-content:center;">▼</span>' +
      '</button>' +
      '<div id="boom-' + uid + '" class="boom-body">' +
        '<div style="padding:0 14px 14px;">' +
          '<div style="height:1px;background:rgba(255,255,255,0.08);margin-bottom:12px;"></div>' +
          t.hooks.map(function(h){
            return '<div style="display:flex;gap:8px;padding:10px;background:rgba(255,255,255,0.04);border-radius:10px;margin-bottom:8px;cursor:pointer;border:1px solid rgba(255,255,255,0.06);"' +
              ' onclick="navigator.clipboard&&navigator.clipboard.writeText(' + "'" + h.text.replace(/'/g,"\\'") + "'" + ').then(function(){alert(' + "'已复制！'" + ')})">' +
              '<span style="background:' + cat.color + ';color:#fff;border-radius:8px;padding:3px 8px;font-size:10px;font-weight:800;white-space:nowrap;flex-shrink:0;align-self:flex-start;">' + h.elem + '</span>' +
              '<span style="font-size:13px;color:rgba(255,255,255,0.8);line-height:1.55;">' + h.text + '</span>' +
            '</div>';
          }).join('') +
        '</div>' +
      '</div>' +
    '</div>';
  }).join('');
}

"""

with open('instagram_growth_mobile.html', 'w', encoding='utf-8') as f:
    f.writelines(BEFORE_RC)
    f.write(NEW_FUNCTIONS)
    f.writelines(AFTER_TOPICS)

total = sum(1 for _ in open('instagram_growth_mobile.html'))
print(f"Done! Lines: {total}")

import subprocess
c1 = subprocess.run(['grep','-c','togglePhone','instagram_growth_mobile.html'],capture_output=True,text=True).stdout.strip()
c2 = subprocess.run(['grep','-c','rgba(255,255,255,0.06)','instagram_growth_mobile.html'],capture_output=True,text=True).stdout.strip()
c3 = subprocess.run(['grep','-c','</html>','instagram_growth_mobile.html'],capture_output=True,text=True).stdout.strip()
print(f"togglePhone refs: {c1}")
print(f"dark card style refs: {c2}")
print(f"</html> count: {c3}")
