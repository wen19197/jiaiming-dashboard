#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_v3.py
1. Remove 'balia'/'atas' from visible lang_nail tags
2. Add "+ 新增脚本" button at bottom of script tab
3. Replace TAB 6 (号码选题) with 数字能量 knowledge base
4. Update tab nav label
"""
import re

FILE = '/sessions/festive-determined-hawking/mnt/outputs/instagram_growth_mobile.html'

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# ──────────────────────────────────────────────
# 1. Remove balia / atas from t-lang tag spans
# ──────────────────────────────────────────────
for word in ['balia', 'atas']:
    html = re.sub(
        r'<span class="stag t-lang">💬 ' + word + r'</span>',
        '', html
    )

# ──────────────────────────────────────────────
# 2. Add "+ 新增脚本" button before </div> end of tab-posts
#    (inject just before <div class="page-bottom"></div> inside tab-posts)
# ──────────────────────────────────────────────
ADD_CARD_CSS = """
/* Add-card button */
.add-sc-btn{display:flex;align-items:center;justify-content:center;gap:8px;margin:12px 12px 4px;padding:14px;border-radius:14px;border:2px dashed rgba(96,165,250,0.35);background:rgba(96,165,250,0.05);color:#60a5fa;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;}
.add-sc-btn:active{background:rgba(96,165,250,0.12);}
.custom-sc{border-color:rgba(96,165,250,0.3);}
"""

ADD_CARD_JS = r"""
var _customCount = parseInt(localStorage.getItem('sc-custom-count')||'0');

function addCustomCard(){
  _customCount++;
  localStorage.setItem('sc-custom-count', _customCount);
  var id = 'c'+_customCount;
  var card = buildCustomCard(id, {});
  var btn = document.getElementById('add-sc-btn');
  btn.parentNode.insertBefore(card, btn);
  // auto-open
  toggleCustomSC(id);
}

function buildCustomCard(id, data){
  var fields = [
    ['type','🎬 拍摄类型',''],['dur','⏱ 预计时长',''],
    ['scene','🏠 场景/置景',''],['emo','🎭 IP情绪建议',''],
    ['field','✨ 磁场主题',''],['theme','📌 拍摄主题','电话号码'],
    ['curve','📈 情绪曲线',''],['hook','🎣 开篇钩子',''],
    ['script','📝 内容脚本',''],['ending','🏁 结尾/语言钉',''],
    ['cover','🖼️ 封面文字 L1',''],['cover2','🖼️ 封面文字 L2',''],
    ['ig','📱 IG配文','']
  ];
  var bodyHtml = fields.map(function(f){
    var key=id+'-'+f[0];
    var saved=localStorage.getItem('sc-edit-'+key)||data[f[0]]||'';
    return '<div class="sf-row"><span class="sf-label">'+f[1]+'</span>'+
      '<span class="sf-val" contenteditable="true" data-ekey="'+key+'" data-ph="点击输入..." '+
      'onblur="saveScEdit(this,this.dataset.ekey)">'+saved+'</span></div>';
  }).join('');

  var el=document.createElement('div');
  el.className='sc-card custom-sc'; el.id='sc-'+id;
  el.innerHTML=
    '<div class="sc-head" onclick="toggleCustomSC(\''+id+'\')">'+
    '<div class="sc-title-row">'+
    '<input type="checkbox" class="sc-check" id="chk-'+id+'" onclick="markCustomFilmed(event,\''+id+'\')">'+
    '<span class="sc-num">✏️</span>'+
    '<span class="sc-title" contenteditable="true" data-ekey="'+id+'-title" '+
    'onblur="saveScEdit(this,this.dataset.ekey)" onclick="event.stopPropagation()" '+
    'style="border-bottom:1px dashed rgba(96,165,250,0.3)">点击输入标题...</span>'+
    '<span class="sc-arrow" id="arr-'+id+'">▼</span></div></div>'+
    '<div class="sc-body" id="sb-'+id+'" style="display:none">'+bodyHtml+'</div>';
  return el;
}

function toggleCustomSC(id){
  var b=document.getElementById('sb-'+id);
  var a=document.getElementById('arr-'+id);
  if(!b)return;
  var open=b.style.display!=='none';
  b.style.display=open?'none':'block';
  a.classList.toggle('open',!open);
}

function markCustomFilmed(evt,id){
  evt.stopPropagation();
  var chk=document.getElementById('chk-'+id);
  var card=document.getElementById('sc-'+id);
  localStorage.setItem('sc-filmed-'+id,chk.checked?'1':'0');
  card.classList.toggle('filmed',chk.checked);
}

function restoreCustomCards(){
  var count=parseInt(localStorage.getItem('sc-custom-count')||'0');
  _customCount=count;
  var btn=document.getElementById('add-sc-btn');
  if(!btn)return;
  for(var i=1;i<=count;i++){
    var id='c'+i;
    var card=buildCustomCard(id,{});
    btn.parentNode.insertBefore(card,btn);
    // restore title
    var titleEl=card.querySelector('[data-ekey="'+id+'-title"]');
    var savedTitle=localStorage.getItem('sc-edit-'+id+'-title');
    if(savedTitle&&titleEl)titleEl.innerText=savedTitle;
    // restore filmed
    var chk=document.getElementById('chk-'+id);
    if(chk&&localStorage.getItem('sc-filmed-'+id)==='1'){
      chk.checked=true; card.classList.add('filmed');
    }
  }
}
"""

ADD_CARD_HTML = """    <div class="add-sc-btn" id="add-sc-btn" onclick="addCustomCard()">
      <span style="font-size:22px;">＋</span> 新增脚本
    </div>
"""

# Inject CSS
html = html.replace('</style>', ADD_CARD_CSS + '\n</style>', 1)
# Inject JS before the DOMContentLoaded block
html = html.replace(
    "window.addEventListener('DOMContentLoaded'",
    ADD_CARD_JS + "\nwindow.addEventListener('DOMContentLoaded'",
    1
)
# Add restoreCustomCards() call inside DOMContentLoaded
html = html.replace('restoreSC();', 'restoreSC();\n  restoreCustomCards();', 1)
# Inject the button HTML into tab-posts (before the last page-bottom inside it)
# We identify the page-bottom inside tab-posts by finding the block
html = html.replace(
    '    <div class="page-bottom"></div>\n  </div>\n</div>\n\n<!-- ========== TAB 3',
    ADD_CARD_HTML + '    <div class="page-bottom"></div>\n  </div>\n</div>\n\n<!-- ========== TAB 3',
    1
)

# ──────────────────────────────────────────────
# 3. Update tab nav label
# ──────────────────────────────────────────────
html = html.replace(
    '<div class="tab-icon">📱</div>号码选题',
    '<div class="tab-icon">🔮</div>数字能量',
    1
)

# ──────────────────────────────────────────────
# 4. Replace TAB 6 content with 数字能量 knowledge base
# ──────────────────────────────────────────────

DE_CSS = """
/* 数字能量 knowledge base */
.de-section{margin:8px 12px 0;}
.de-cat-head{display:flex;align-items:center;justify-content:space-between;padding:12px 14px;cursor:pointer;border-radius:12px;font-size:13px;font-weight:700;color:#e0e0f0;user-select:none;}
.de-cat-head .de-arr{font-size:11px;color:#7070a0;transition:transform .25s;}
.de-cat-head .de-arr.open{transform:rotate(180deg);}
.de-cat-body{padding:0 14px 14px;}
.de-field-card{margin-bottom:10px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);}
.de-field-head{display:flex;align-items:center;justify-content:space-between;padding:10px 14px;cursor:pointer;user-select:none;}
.de-field-title{font-size:13px;font-weight:800;}
.de-field-nums{font-size:11px;color:#a0a0c0;margin-top:2px;}
.de-field-body{padding:10px 14px 12px;border-top:1px solid rgba(255,255,255,0.06);}
.de-row{margin-bottom:8px;}
.de-row-label{font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.8px;color:#6060a0;margin-bottom:3px;}
.de-row-val{font-size:12px;color:#c8c8e8;line-height:1.6;}
.de-badge{display:inline-block;border-radius:5px;padding:2px 7px;font-size:10px;font-weight:700;margin:2px;}
.de-good{background:rgba(52,211,153,0.15);color:#6ee7b7;}
.de-bad{background:rgba(248,113,113,0.15);color:#fca5a5;}
.de-num{background:rgba(96,165,250,0.15);color:#93c5fd;font-weight:900;}
.de-star-table{width:100%;border-collapse:collapse;font-size:11px;margin-top:4px;}
.de-star-table th{padding:6px 8px;text-align:center;font-size:10px;color:#7070a0;border-bottom:1px solid rgba(255,255,255,0.08);}
.de-star-table td{padding:6px 8px;text-align:center;border-bottom:1px solid rgba(255,255,255,0.05);}
.de-star-table .star-name{text-align:left;font-weight:800;font-size:12px;}
.de-nums-row{display:flex;flex-wrap:wrap;gap:4px;margin:4px 0;}
.de-num-chip{background:rgba(167,139,250,0.2);color:#c4b5fd;border-radius:5px;padding:3px 8px;font-size:11px;font-weight:800;}
.de-combo-item{background:rgba(255,255,255,0.04);border-radius:8px;padding:8px 10px;margin-bottom:6px;font-size:12px;color:#c0c0e0;line-height:1.6;}
.de-combo-item strong{color:#fde68a;}
.de-danger-section{margin-bottom:10px;}
.de-danger-title{font-size:12px;font-weight:800;color:#fca5a5;margin-bottom:6px;}
.de-danger-nums{display:flex;flex-wrap:wrap;gap:5px;}
.de-danger-num{background:rgba(248,113,113,0.15);color:#fca5a5;border-radius:5px;padding:3px 8px;font-size:11px;font-weight:700;}
.de-letter-table{width:100%;border-collapse:collapse;font-size:12px;}
.de-letter-table td{padding:5px;text-align:center;border:1px solid rgba(255,255,255,0.07);}
.de-letter-table td:first-child{font-weight:800;color:#60a5fa;}
.de-search{width:100%;padding:10px 14px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:10px;color:#e0e0f0;font-size:13px;outline:none;box-sizing:border-box;}
.de-search::placeholder{color:#505070;}
.de-zero-card{background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:10px 12px;margin-bottom:8px;}
.de-zero-title{font-size:12px;font-weight:800;color:#fde68a;margin-bottom:4px;}
.de-zero-val{font-size:11px;color:#c0c0e0;line-height:1.65;}
"""

# Star data
STARS = [
    {
        'name':'天医', 'element':'土', 'type':'吉',
        'color':'rgba(251,191,36,0.15)','text':'#fbbf24',
        'nums':'13/31　68/86　49/94　27/72',
        'strength':'最强13/31　次强68/86　次弱49/94　最弱27/72',
        'core':'钱财、婚姻、业绩',
        'traits':'聪明、财富、业绩好、心胸开阔、善解人意',
        'weakness':'没主见、单纯容易被骗',
        'career':'钱财，工资，业绩，保险，金融，文艺，资金流',
        'money':'财源，财路，意外之财，富有',
        'love':'正桃花，婚姻，婚外情',
        'health':'血压，血液循环，眼耳鼻病',
        'study':'有天赋，宗教玄学',
        'before':'① 钱的来源和职业方向　② 对象特征和情况　③ 血液血压等疾病原因',
        'after':'① 钱的去向和工作情况　② 婚后状况和感情态度',
        'stack':'① 得财延续　② 稳定收入　③ 感情长期甜蜜　④ 血液疾病短时间难根治',
        'scatter':'① 好多段感情　② 财路多',
        'tail':'① 婚外情桃花多　② 财运旺机遇多　③ 血液疾病（老年更重）',
        'resolve':'一个天医可制服一个绝命',
    },
    {
        'name':'生气', 'element':'木', 'type':'吉',
        'color':'rgba(52,211,153,0.12)','text':'#34d399',
        'nums':'14/41　67/76　39/93　28/82',
        'strength':'最强14/41　次强67/76　次弱39/93　最弱28/82',
        'core':'贵人、亲戚、朋友、同事',
        'traits':'乐天派、有贵人帮、思维活跃、沟通能力强、好名声',
        'weakness':'企图心不强、懒散、没主见、无奈',
        'career':'服务业，意外之财，贵人送财，逢凶化吉',
        'money':'贵人带来财运，服务业得财',
        'love':'开心甜蜜，正桃花，好心情',
        'health':'肠胃，感情，身心开朗',
        'study':'全方位学习，接受新知识',
        'before':'① 贵人情况　② 对什么满足/看得开　③ 无奈或懒惰的原因　④ 肠胃疾病原因',
        'after':'① 贵人的作用好坏　② 贵人的表现',
        'stack':'贵人持续出现，长期得到帮助',
        'scatter':'各方来源的贵人支持',
        'tail':'贵人在最后出现，结果顺利',
        'resolve':'生气/生气+延年/生气+伏位相连，可化解一个祸害',
    },
    {
        'name':'延年', 'element':'金', 'type':'吉',
        'color':'rgba(247,151,30,0.12)','text':'#f7971e',
        'nums':'19/91　78/87　34/43　26/62',
        'strength':'最强19/91　次强78/87　次弱34/43　最弱26/62',
        'core':'工作、事业、专业能力、阳刚性',
        'traits':'自主性强、责任心强、判断力强、追求完美、不乱花钱',
        'weakness':'大男/女子主义、好面子、心软、劳碌、压力大',
        'career':'喜欢主导，专业能力强，奔波劳碌，善于经营',
        'money':'懂得守财，善于理财，铁公鸡',
        'love':'专一，不轻易劈腿，固执，霸道',
        'health':'压力病，劳累',
        'study':'能抓住重点，聪明',
        'before':'① 所从事行业性质　② 责任心放在什么上面　③ 善于经营什么　④ 对什么挑剔讲究　⑤ 压力来源',
        'after':'① 工作态度，感情状态　② 能力特长用到了哪里',
        'stack':'事业持续发展，能力不断加强',
        'scatter':'多方面能力展示',
        'tail':'事业成功，守业能力强',
        'resolve':'一个延年可压服一个六煞',
    },
    {
        'name':'伏位', 'element':'木', 'type':'吉',
        'color':'rgba(96,165,250,0.12)','text':'#60a5fa',
        'nums':'11/22　88/99　66/77　33/44',
        'strength':'最强11/22　次强99/88　次弱66/77　最弱33/44',
        'core':'蓄势待发、状况延续、潜龙在渊',
        'traits':'有耐心毅力、等待机会、一鸣惊人',
        'weakness':'不易变动、被动保守、不敢冒险、易有外债、内心矛盾',
        'career':'保守被动，等待时机，慢工细活，研究分析行业',
        'money':'稳定求财，保守求财',
        'love':'过于保守、胡思乱想、处理感情像含羞草',
        'health':'心脏、脑部、血稠、隐性疾病',
        'study':'坐得住，擅长思考分析，逻辑推理，灵感强',
        'before':'伏位在前：能量延续前面的磁场',
        'after':'伏位在后：能量延续并放大前面的磁场',
        'stack':'长期稳定，但停滞不前',
        'scatter':'伏位独立出现时保守性明显',
        'tail':'结果平稳，不大起大落',
        'resolve':'生气+伏位相连可化解一个祸害；延年+伏位相连可化解一个五鬼',
    },
    {
        'name':'六煞', 'element':'水', 'type':'凶',
        'color':'rgba(167,139,250,0.12)','text':'#a78bfa',
        'nums':'16/61　47/74　38/83　29/92',
        'strength':'最强16/61　次强47/74　次弱38/83　最弱29/92',
        'core':'偏桃花、女性化、家庭、房子、店铺、时尚',
        'traits':'美女帅哥、时尚、异性缘好、沟通力强、有魅力',
        'weakness':'犹豫不决、情绪化、感情用事、不开心、烦躁',
        'career':'服务业，女性行业，房产中介',
        'money':'人际关系得财，不易守财，因情损财',
        'love':'感情丰富，婚姻不顺，易有第三者，为情所困',
        'health':'失眠多梦，抑郁，皮肤，肠胃疾病',
        'study':'对美有鉴赏力，难以安静学习',
        'before':'① 魅力来源　② 女性/家/店面情况　③ 不开心原因　④ 肠胃皮肤病原因',
        'after':'① 肠胃皮肤病后果　② 身边女性的打算和行为',
        'stack':'感情问题反复出现，情绪长期起伏',
        'scatter':'多方感情线同时存在',
        'tail':'最终因情困扰或破财',
        'resolve':'一个延年可压服一个六煞',
    },
    {
        'name':'祸害', 'element':'土', 'type':'凶',
        'color':'rgba(248,113,113,0.12)','text':'#f87171',
        'nums':'17/71　89/98　46/64　23/32',
        'strength':'最强17/71　次强89/98　次弱46/64　最弱23/32',
        'core':'口舌是非、小人、病痛、意外伤灾',
        'traits':'口才好，能言善辩',
        'weakness':'花言巧语、脾气差、易激怒别人、爱面子、抱怨、小人',
        'career':'以口为业，老师，业务员，餐饮，娱乐',
        'money':'是非中损财，小人搞破坏',
        'love':'花言巧语说假话，易争吵，易分手',
        'health':'车祸，意外伤灾，咽喉/口腔/淋巴/肺气管/呼吸疾病',
        'study':'语言能力好',
        'before':'① 身体不好原因　② 小人特点　③ 意外伤害来源　④ 生气抱怨原因',
        'after':'是非的后果，病痛的结果',
        'stack':'是非口舌持续，病痛反复',
        'scatter':'多方小人同时存在',
        'tail':'结果因是非受损',
        'resolve':'生气/生气+延年/生气+伏位相连可化解一个祸害',
    },
    {
        'name':'五鬼', 'element':'火', 'type':'凶',
        'color':'rgba(251,146,60,0.12)','text':'#fb923c',
        'nums':'18/81　79/97　36/63　24/42',
        'strength':'最强18/81　次强79/97　次弱36/63　最弱24/42',
        'core':'变动改革、异地国外、血光、捉摸不定',
        'traits':'才华好，反应快，学习强，鬼点子多，易与玄学结缘',
        'weakness':'好幻想、反复无常、不稳定、缺安全感、疑心病重',
        'career':'宗教，企划，贸易公司，偏门生意，异地工作',
        'money':'红包，暗财，突然破财',
        'love':'不安分，三角恋外遇，离过婚；36/42异国恋多',
        'health':'心脏血液，女性妇科，男性肺部，老年脑部，中邪',
        'study':'有天赋，动脑，艺术类',
        'before':'① 变动原因　② 感情不稳定原因　③ 命理/宗教缘人特征　④ 后悔反悔的事',
        'after':'① 变动的情况　② 变动后带来的后果',
        'stack':'变动频繁，不稳定持续',
        'scatter':'多方变动因素',
        'tail':'结果变动，出乎意料',
        'resolve':'生气+天医+延年/延年+伏位相连可化解一个五鬼',
    },
    {
        'name':'绝命', 'element':'金', 'type':'凶',
        'color':'rgba(244,114,182,0.12)','text':'#f472b6',
        'nums':'12/21　69/96　48/84　37/73',
        'strength':'最强12/21　次强69/96　次弱48/84　最弱37/73',
        'core':'投资、开支、破财',
        'traits':'很会赚钱，意外之财，头脑反应快，企图心强，记忆力好',
        'weakness':'冲动暴躁、情绪不稳、好赌、易有官司',
        'career':'辛苦，独来独往，流动性职业，风险行业，敢冲敢做',
        'money':'不会守财，大起大落，投资风险高',
        'love':'难有结果，重视朋友，家庭协调差，易离婚',
        'health':'肝胆，肾，糖尿病，泌尿系统',
        'study':'头脑反应快，但冲动影响学习',
        'before':'① 破财花销原因　② 不适合做的事　③ 感情不稳定因素　④ 泌尿生殖系统疾病原因',
        'after':'① 钱的流向　② 思想状态　③ 变动后的情况',
        'stack':'破财持续，投资连续失败',
        'scatter':'多方破财线索',
        'tail':'结果破财，投资失败',
        'resolve':'一个天医可制服一个绝命',
    },
]

def de_section(title, body_html, open_=False):
    uid = title.replace(' ','').replace('/','')
    arr_cls = 'de-arr open' if open_ else 'de-arr'
    body_display = 'block' if open_ else 'none'
    return f'''<div class="de-section">
  <div style="border-radius:12px;overflow:hidden;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);margin-bottom:2px;">
    <div class="de-cat-head" onclick="toggleDE('{uid}')">
      <span>{title}</span>
      <span class="de-arr" id="de-arr-{uid}">▼</span>
    </div>
    <div id="de-{uid}" style="display:{body_display}">
      <div class="de-cat-body">{body_html}</div>
    </div>
  </div>
</div>'''

def star_card(s):
    uid = s['name']
    tc = s['text']
    bg = s['color']
    star_type_badge = f'<span class="de-badge {"de-good" if s["type"]=="吉" else "de-bad"}">{"✨ 四吉星" if s["type"]=="吉" else "⚠️ 四凶星"}</span>'
    nums_html = ''.join(f'<span class="de-num-chip">{n.strip()}</span>' for n in s['nums'].split('　') if n.strip())

    rows = [
        ('核心', s['core']),
        ('优点', s['traits']),
        ('缺点', s['weakness']),
        ('事业', s['career']),
        ('钱财', s['money']),
        ('感情', s['love']),
        ('健康', s['health']),
        ('学习', s['study']),
        ('在前（磁场前面）', s['before']),
        ('在后（磁场后面）', s['after']),
        ('叠加（连续出现）', s['stack']),
        ('分散', s['scatter']),
        ('尾号', s['tail']),
        ('化解关系', s['resolve']),
    ]
    rows_html = ''.join(
        f'<div class="de-row"><div class="de-row-label">{r[0]}</div><div class="de-row-val">{r[1]}</div></div>'
        for r in rows
    )

    return f'''<div class="de-field-card" id="de-star-{uid}" style="background:{bg};border-color:rgba(255,255,255,0.1);">
  <div class="de-field-head" onclick="toggleDECard('{uid}')">
    <div>
      <div class="de-field-title" style="color:{tc};">{s["name"]} ({s["element"]}) {star_type_badge}</div>
      <div class="de-field-nums">{s["nums"]}</div>
    </div>
    <span class="de-arr" id="de-arr-star-{uid}">▼</span>
  </div>
  <div id="de-body-{uid}" style="display:none">
    <div class="de-field-body">
      <div style="margin-bottom:10px;"><div class="de-row-label">数字组合强弱</div><div class="de-nums-row">{nums_html}</div><div class="de-row-val" style="font-size:11px;color:#7070a0;">{s["strength"]}</div></div>
      {rows_html}
    </div>
  </div>
</div>'''

# Build the 8 stars HTML
stars_good = [star_card(s) for s in STARS if s['type']=='吉']
stars_bad = [star_card(s) for s in STARS if s['type']=='凶']

# 0 & 5 rules
ZERO_RULES = [
    ('5 的含义（放大）', '5 出现在磁场中间 → 放大过程\n5 出现在磁场后面 → 放大结果'),
    ('0 的基础含义', '0 = 归零、隐藏、弱化、陷阱、被套、地下情\n2个0 = 官司、是非（像手铐）\n3个0 = 容易吸引肿瘤、癌症、重大疾病\n4个0 = 四大皆空（财运空、事业空、婚姻空、健康空）'),
    ('0 夹在各磁场中间的影响', '生气夹0 → 贵人不显，出家修行\n天医夹0 → 资金被套，借钱没收回来\n延年夹0 → 有能力却施展不出，卖房\n绝命夹0 → 未婚先孕，投资失败，破产\n六煞夹0 → 堕胎，流产\n五鬼夹0 → 隐藏性心脏病（医院查不出）\n祸害夹0 → 隐藏性疾病，小人暗藏'),
    ('特殊 0 组合', '301 = 婚姻波折，被冷落；资金被套\n104 = 贵人借不上力\n809 = 有苦难言\n906 = 投资被套\n108 = 埋没的人才\n601 = 隐性桃花或体内长东西\n0越多 = 表面越风光，内心越沧桑'),
    ('号码末尾的 0 含义', '末位(第1位)是0 → ① 结果等于0，一场空　② 克孩子（孩子运势健康财运不好）\n末位(第2位)是0 → 克另外一半（男克老婆，女克老公）\n末位(第3位)是0 → 克自己（事业健康财运不好）\n末位(第4位)是0 → ① 克兄弟姐妹　② 克男主人（赚钱最主要的人）\n末位(第5位)是0 → 克父母（女克爸，男克妈；65岁前早亡，65后重病）\n末位(第6位)是0 → 克自己的生意（中断后面的能量链接）'),
]

zero_html = ''.join(
    f'<div class="de-zero-card"><div class="de-zero-title">{z[0]}</div><div class="de-zero-val" style="white-space:pre-wrap">{z[1]}</div></div>'
    for z in ZERO_RULES
)

# Combinations
COMBOS_RESOLVE = [
    ('天医 化解 绝命', '一个天医可制服一个绝命'),
    ('延年 化解 六煞', '一个延年可压服一个六煞'),
    ('生气/生气+延年/生气+伏位 化解 祸害', '三组之一相连可化解一个祸害'),
    ('生气+天医+延年 / 延年+伏位 化解 五鬼', '两组之一相连可化解一个五鬼'),
]

COMBOS_EFFECT = [
    ('天医+延年+生气', '完整婚恋，婚后幸福'),
    ('天医+任意凶星', '感情破裂，分手'),
    ('延年+任意凶星', '工作不愉悦，跳槽'),
    ('六煞+绝命', '容易看破红尘'),
    ('绝命+五鬼 / 五鬼+绝命', '意外伤灾'),
    ('五鬼+六煞 / 六煞+五鬼', '抑郁，出轨'),
    ('生气+天医', '招正桃花'),
]

COMBOS_MONEY = [
    ('生气+天医', '贵人来财'),
    ('延年+天医', '专业技能来财'),
    ('绝命+天医', '白手起家，投资来财'),
    ('五鬼+天医', '投资来财，意外之财'),
    ('六煞+天医', '人脉来财'),
    ('祸害+天医', '口才来财'),
]

combo_html = (
    '<div class="de-row-label">化解关系</div>' +
    ''.join(f'<div class="de-combo-item"><strong>{c[0]}</strong><br>{c[1]}</div>' for c in COMBOS_RESOLVE) +
    '<div class="de-row-label" style="margin-top:10px;">星耀组合效果</div>' +
    ''.join(f'<div class="de-combo-item"><strong>{c[0]}</strong> → {c[1]}</div>' for c in COMBOS_EFFECT) +
    '<div class="de-row-label" style="margin-top:10px;">如何选择赚钱渠道（天医前面的星）</div>' +
    ''.join(f'<div class="de-combo-item"><strong>{c[0]}</strong> → {c[1]}</div>' for c in COMBOS_MONEY)
)

# 全阳号警告
FULL_YANG = '<div class="de-zero-card"><div class="de-zero-title" style="color:#f87171;">⚠️ 全阳号（早亡号）</div><div class="de-zero-val">如果号码全部都是吉星（四吉星），代表「全阳号」。能量全部倒转，4年内必定插水（极度不好）。\n\n好的号码必须：有吉有凶，能量由低走高，才能驾驭。</div></div>'

# Car & door energy
CAR_HTML = '''<div class="de-zero-val" style="white-space:pre-wrap;margin-bottom:10px;">英文字母也要看（对照表在下方）。车牌同样两个两个看。

<b style="color:#fbbf24;">天医</b> → 福气、来财
<b style="color:#34d399;">生气</b> → 带来贵人、开心
<b style="color:#f7971e;">延年</b> → 安全驾驶但压力大
<b style="color:#60a5fa;">伏位</b> → 有耐心
<b style="color:#a78bfa;">六煞</b> → 开车容易郁闷，被人剐蹭撞击，心情不好
<b style="color:#f87171;">祸害</b> → 容易吸引意外，路怒症，吵架，零件（冷气、水管、引擎）容易坏
<b style="color:#fb923c;">五鬼</b> → 胡思乱想造成车祸，血光，突然来的意外（108 一撞就byebye）
<b style="color:#f472b6;">绝命</b> 73/37 → 主动冲动超速踩快油，主动造成车祸

车牌能量越少越好（越简单越好）</div>'''

DOOR_HTML = '''<div class="de-zero-val" style="white-space:pre-wrap;">门牌也是两个两个看，影响住在里面的所有人。

<b style="color:#fbbf24;">天医</b> 13/31 → 旺最赚钱的人，吸财，佛缘
<b style="color:#34d399;">生气</b> → 开心乐观，时常有朋友来玩
<b style="color:#f7971e;">延年</b> → 睡不着，谈工作，压力（26比较容易休息）
<b style="color:#60a5fa;">伏位</b> → 无太多能量，看前面的磁场
<b style="color:#f472b6;">绝命</b> → 脾气臭（尤其女性）
<b style="color:#f87171;">祸害</b> → 很容易吵架，做事两头不到岸，呼吸系统出问题
<b style="color:#fb923c;">五鬼</b> → 灵异，噩梦，熬夜，忘东忘西，破财
<b style="color:#a78bfa;">六煞</b> → 内耗，焦虑，郁闷，皮肤敏感，总是出事，不断往外花钱</div>'''

# Dangerous numbers
DANGER_HTML = '''<div class="de-danger-section">
  <div class="de-danger-title">🩸 重大意外凶险血光号码</div>
  <div class="de-danger-nums">''' + ''.join(f'<span class="de-danger-num">{n}</span>' for n in ['818','851','158','810','180','118','811','181','816','817']) + '''</div>
</div>
<div class="de-danger-section">
  <div class="de-danger-title">☠️ 往生号码</div>
  <div class="de-danger-nums">''' + ''.join(f'<span class="de-danger-num">{n}</span>' for n in ['108','801','1058','1508','8501','8051','709','907','7509','7059','9057','9507']) + '''</div>
</div>
<div class="de-danger-section">
  <div class="de-danger-title">🏥 重大疾病号码</div>
  <div class="de-danger-nums">''' + ''.join(f'<span class="de-danger-num">{n}</span>' for n in ['812','218','212','121','102','201','716','618','8012','8102','8512','8152','152','251','617','718','2018','2518','2108','2158','217','712','171','711','817','612','216','816','157','751','107','701','1507','1057','7501','7051','8559','9558','8509','8059','9508','9805']) + '''</div>
</div>'''

# Letter table
LETTERS_A = list('ABCDEFGHIJKLM')
LETTERS_N = list('NOPQRSTUVWXYZ')
NUMS_A = list(range(1, 14))
NUMS_N = list(range(14, 27))
letter_rows = (
    '<table class="de-letter-table">' +
    '<tr>' + ''.join(f'<td>{l}</td>' for l in LETTERS_A) + '</tr>' +
    '<tr>' + ''.join(f'<td style="color:#c4b5fd;">{n}</td>' for n in NUMS_A) + '</tr>' +
    '<tr>' + ''.join(f'<td>{l}</td>' for l in LETTERS_N) + '</tr>' +
    '<tr>' + ''.join(f'<td style="color:#c4b5fd;">{n}</td>' for n in NUMS_N) + '</tr>' +
    '</table>' +
    '<div style="font-size:11px;color:#7070a0;margin-top:6px;">车牌英文字母先转换成数字，再与车牌号码一起两个两个看。</div>'
)

# 八星速查表
QUICK_TABLE = '''<div style="overflow-x:auto;"><table class="de-star-table">
<tr><th>八星</th><th>特质</th><th>最强</th><th>次强</th><th>次弱</th><th>最弱</th></tr>''' + ''.join(
    f'<tr><td class="star-name" style="color:{s["text"]};">{s["name"]}({s["element"]})</td><td style="font-size:10px;color:#a0a0c0;">{s["core"]}</td>'
    + ''.join(f'<td><span class="de-num-chip" style="font-size:10px;">{n}</span></td>' for n in [p.strip() for p in s["strength"].replace("最强","").replace("次强","").replace("次弱","").replace("最弱","").split("　") if p.strip()])
    + '</tr>'
    for s in STARS
) + '</table></div>'''

# General rules
GENERAL_HTML = '''<div class="de-zero-card">
  <div class="de-zero-title">✅ 好号码的标准</div>
  <div class="de-zero-val">1. 号码磁场能量必须由低走高（才能驾驭）
2. 手机号中能量最强的星耀决定号主的主要性格
3. 吉凶搭配 70% 吉星 + 30% 凶星 最为平衡
4. 全阳号（全吉星）= 早亡号，4年内必插水</div>
</div>''' + FULL_YANG

# Build sections
SECTION_05 = de_section('🔢 0 与 5 的特殊含义（必看）', zero_html, open_=True)
SECTION_TABLE = de_section('📊 八星速查表', QUICK_TABLE)
SECTION_RULES = de_section('📐 好号码标准 & 全阳号警告', GENERAL_HTML)
SECTION_GOOD = de_section('✨ 四吉星详解', '\n'.join(stars_good))
SECTION_BAD = de_section('⚠️ 四凶星详解', '\n'.join(stars_bad))
SECTION_COMBO = de_section('🔗 磁场组合 & 化解关系', combo_html)
SECTION_CAR = de_section('🚗 车牌能量', CAR_HTML)
SECTION_DOOR = de_section('🏠 门牌能量', DOOR_HTML)
SECTION_DANGER = de_section('🚨 危险号码参考', DANGER_HTML)
SECTION_LETTER = de_section('🔤 英文字母对照表（车牌用）', letter_rows)

DE_JS = """
function toggleDE(id){
  var el=document.getElementById('de-'+id);
  var arr=document.getElementById('de-arr-'+id);
  if(!el)return;
  var open=el.style.display!=='none';
  el.style.display=open?'none':'block';
  arr.classList.toggle('open',!open);
}
function toggleDECard(id){
  var el=document.getElementById('de-body-'+id);
  var arr=document.getElementById('de-arr-star-'+id);
  if(!el)return;
  var open=el.style.display!=='none';
  el.style.display=open?'none':'block';
  arr.classList.toggle('open',!open);
}
"""

NEW_TAB6 = f"""<!-- ========== TAB 6: DIGITAL ENERGY ========== -->
<div id="tab-phone" class="section">
  <div class="page-top">
    <div class="sec-lbl">🔮 数字能量资料库</div>
    <div style="padding:0 12px 8px;">
      <input class="de-search" type="search" placeholder="🔍 搜索磁场名称、号码组合..." oninput="deSearch(this.value)">
    </div>
    {SECTION_05}
    {SECTION_TABLE}
    {SECTION_RULES}
    {SECTION_GOOD}
    {SECTION_BAD}
    {SECTION_COMBO}
    {SECTION_CAR}
    {SECTION_DOOR}
    {SECTION_DANGER}
    {SECTION_LETTER}
    <div class="page-bottom"></div>
  </div>
</div>

"""

DE_SEARCH_JS = """
function deSearch(q){
  q=q.trim().toLowerCase();
  if(!q){
    document.querySelectorAll('.de-field-card,.de-section').forEach(function(el){el.style.display='';});
    return;
  }
  document.querySelectorAll('.de-field-card').forEach(function(card){
    var txt=card.innerText.toLowerCase();
    card.style.display=txt.includes(q)?'':'none';
  });
}
"""

# Inject DE CSS and JS
html = html.replace('</style>', DE_CSS + '\n</style>', 1)
html = html.replace(
    "window.addEventListener('DOMContentLoaded'",
    DE_JS + DE_SEARCH_JS + "\nwindow.addEventListener('DOMContentLoaded'",
    1
)

# Replace TAB 6 block
tab6_pattern = re.compile(
    r'<!-- ={5,} TAB 6: PHONE TOPICS ={5,} -->.*?</div>\s*\n(?=\s*</div><!-- end main)',
    re.DOTALL
)
html, n = tab6_pattern.subn(NEW_TAB6, html)
if n == 0:
    # Fallback
    s6 = html.find('<!-- ========== TAB 6: PHONE TOPICS ========== -->')
    e6 = html.find('</div><!-- end main -->')
    if s6 >= 0 and e6 >= 0:
        html = html[:s6] + NEW_TAB6 + '\n' + html[e6:]
        print('Fallback replacement OK for TAB 6')
    else:
        print('ERROR: Could not find TAB 6')
else:
    print(f'TAB 6 replaced (regex, {n} match)')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done. Chars: {len(html)}, Lines: {html.count(chr(10))}')
