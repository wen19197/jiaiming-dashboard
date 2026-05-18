with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# togglePhone starts at line 1317 (1-indexed) = index 1316
# renderContent starts at line 1325 (1-indexed) = index 1324
# let currentCat starts at line 1371 (1-indexed) = index 1370
# Replace lines 1316 to 1369 (inclusive) with clean version

BEFORE = lines[:1316]
AFTER  = lines[1370:]   # from "let currentCat = 'plate';" onwards

NEW_FUNCS = """\
function togglePhone(uid){
  var body = document.getElementById('pb-'+uid);
  if(!body) return;
  body.classList.toggle('open');
  var arr = document.getElementById('pa-'+uid);
  if(arr) arr.textContent = body.classList.contains('open') ? '▲' : '▼';
}

function renderContent(){
  var f = FIELDS[currentField];
  var items = f[currentMode];
  var isBest = currentMode === 'best';
  var col = isBest ? '#22c55e' : '#ef4444';
  var label = isBest ? '吉星开场' : '凶星开场';
  var bestBg  = isBest  ? '#22c55e' : 'rgba(255,255,255,0.08)';
  var worstBg = !isBest ? '#ef4444' : 'rgba(255,255,255,0.08)';
  var bestCl  = isBest  ? '#fff' : 'rgba(255,255,255,0.5)';
  var worstCl = !isBest ? '#fff' : 'rgba(255,255,255,0.5)';
  var html = '';
  html += '<div style="display:flex;gap:8px;margin-bottom:14px;">';
  html += '<button data-m="best" class="rc-toggle" style="flex:1;padding:9px;border:none;border-radius:12px;font-weight:700;font-size:13px;cursor:pointer;background:'+bestBg+';color:'+bestCl+'">✅ 吉星案例</button>';
  html += '<button data-m="worst" class="rc-toggle" style="flex:1;padding:9px;border:none;border-radius:12px;font-weight:700;font-size:13px;cursor:pointer;background:'+worstBg+';color:'+worstCl+'">⚠️ 凶星案例</button>';
  html += '</div>';
  html += '<div style="background:'+f.color+'22;border-left:4px solid '+f.color+';border-radius:0 12px 12px 0;padding:10px 14px;margin-bottom:14px;">';
  html += '<div style="font-weight:800;color:'+f.color+';font-size:15px;">'+f.name+' — '+label+'</div>';
  html += '<div style="font-size:11px;color:rgba(255,255,255,0.4);margin-top:3px;">点击展开 · 复制开场白</div>';
  html += '</div>';
  for(var i=0;i<items.length;i++){
    var item = items[i];
    var uid = 'ph_'+currentField+'_'+currentMode+'_'+i;
    var preview = item.length>22 ? item.slice(0,22)+'…' : item;
    html += '<div style="background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:14px;margin-bottom:10px;overflow:hidden;">';
    html += '<button data-uid="'+uid+'" class="ph-expand" style="display:flex;align-items:center;justify-content:space-between;width:100%;padding:14px;background:none;border:none;font-family:inherit;cursor:pointer;text-align:left;gap:8px;">';
    html += '<div style="flex:1;min-width:0;">';
    html += '<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">';
    html += '<span style="background:'+col+';color:#fff;border-radius:50%;width:22px;height:22px;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;flex-shrink:0;">'+(i+1)+'</span>';
    html += '<span style="font-size:12px;color:'+col+';font-weight:700;">'+(isBest?'✅ 吉星场景':'⚠️ 凶星场景')+'</span>';
    html += '</div>';
    html += '<div style="font-size:13px;color:rgba(255,255,255,0.75);line-height:1.4;padding-left:30px;">'+preview+'</div>';
    html += '</div>';
    html += '<span id="pa-'+uid+'" style="color:'+f.color+';font-size:11px;flex-shrink:0;">▼</span>';
    html += '</button>';
    html += '<div id="pb-'+uid+'" class="boom-body">';
    html += '<div style="padding:0 14px 14px 14px;">';
    html += '<div style="background:rgba(255,255,255,0.05);border-radius:10px;padding:12px;margin-bottom:10px;">';
    html += '<div style="font-size:13px;color:rgba(255,255,255,0.9);line-height:1.6;">'+item+'</div>';
    html += '</div>';
    html += '<button data-copy="'+i+'" class="ph-copy" style="width:100%;padding:9px;background:'+f.color+';border:none;border-radius:10px;color:#fff;font-size:13px;font-weight:700;cursor:pointer;margin-bottom:10px;">📋 复制开场白</button>';
    html += '<div style="background:rgba(255,255,255,0.04);border-radius:8px;padding:8px 10px;">';
    html += '<div style="font-size:10px;color:rgba(255,255,255,0.4);font-weight:700;margin-bottom:4px;">📝 脚本结构</div>';
    html += '<div style="font-size:11px;color:rgba(255,255,255,0.45);line-height:1.6;">开场情景 → 引入'+f.name+'概念 → 数字解读 → 改运建议 → 互动钩子</div>';
    html += '</div></div></div></div>';
  }
  var wrap = document.getElementById('phone-topics');
  wrap.innerHTML = html;
  // Attach event listeners (no inline onclick = no quote issues)
  wrap.querySelectorAll('.rc-toggle').forEach(function(btn){
    btn.addEventListener('click', function(){ setMode(this.dataset.m); });
  });
  wrap.querySelectorAll('.ph-expand').forEach(function(btn){
    btn.addEventListener('click', function(){ togglePhone(this.dataset.uid); });
  });
  wrap.querySelectorAll('.ph-copy').forEach(function(btn){
    btn.addEventListener('click', function(){
      var txt = items[parseInt(this.dataset.copy)];
      if(navigator.clipboard){ navigator.clipboard.writeText(txt).then(function(){ alert('已复制！'); }); }
    });
  });
}

"""

with open('instagram_growth_mobile.html', 'w', encoding='utf-8') as f:
    f.writelines(BEFORE)
    f.write(NEW_FUNCS)
    f.writelines(AFTER)

print("Written. Checking syntax...")
import subprocess, re

# Extract JS and check
with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    html = f.read()
match = re.search(r'<script>(.*)</script>', html, re.DOTALL)
if match:
    with open('/tmp/check.js', 'w') as f:
        f.write(match.group(1))
r = subprocess.run(['node','--check','/tmp/check.js'], capture_output=True, text=True)
if r.returncode == 0:
    print("✅ JS syntax OK!")
else:
    print("❌ Syntax error:")
    print(r.stderr[:500])

total = sum(1 for _ in open('instagram_growth_mobile.html'))
print(f"Total lines: {total}")
