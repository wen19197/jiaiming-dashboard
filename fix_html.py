import sys

# Read existing lines, keep 1-1195
with open('instagram_growth_mobile.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

kept = lines[:1195]  # lines 1-1195 (0-indexed: 0-1194)

# Verify last kept line
print("Last kept line:", repr(kept[-1].rstrip()))

MISSING = r"""      '我朋友40岁中风，因为一直在为别人的事情操心，自己的事情一个都没做',
    ],
  },
  // 伏位星 (field index 3)
  {
    id:'fuwei', name:'伏位星 ☯️', color:'#8b5cf6',
    best:[
      '我认识一个人，做同一件事做了20年，现在是这个行业里最被人尊重的专家',
      '我朋友很稳定，没有大起大落，但每年都在进步，10年后大家才发现他有多厉害',
      '我有一个前辈，不喜欢出风头，但每一次开会他说的话，所有人都会听',
      '我认识的人做事很细心，不快但是每次都做对，从来不需要返工',
      '我朋友用15年做一件事，现在别人要花3倍价钱来请他',
      '我老板很低调，但公司每年都在稳定增长，从不靠运气',
      '我认识的人不急不忙，但10年前买的房子现在涨了三倍',
      '我前辈说，他的成功秘诀就是把一件事做到别人追不上',
      '我朋友从不跟人争，但每次机会来，都是找他的',
    ],
    worst:[
      '我认识的人太保守，机会来了也不敢动，最后被别人抢先',
      '我朋友很稳定，但从来不愿意改变，结果被时代淘汰了',
      '我老板太谨慎，什么事都要想很久，公司机会一个个溜走',
      '我认识的人做事没有进展，每年都一样，原地踏步了10年',
      '我朋友太过坚持，但坚持的方向是错的，坚持越久损失越大',
      '我同事不喜欢冒险，结果一辈子都在等待，等来了退休',
      '我认识的人太执着，放不下一段关系，浪费了5年青春',
      '我朋友太过保守，拒绝了所有新事物，现在后悔莫及',
      '我老板不敢创新，结果竞争对手超越了，市场份额越来越小',
    ],
  },
  // 绝命星 (field index 4)
  {
    id:'jueming', name:'绝命星 ⚡', color:'#ef4444',
    best:[
      '我认识的人胆子很大，别人不敢做的他第一个冲，结果成了行业第一',
      '我朋友在最低潮的时候做了一个大决定，现在是我们圈子里最成功的',
      '我老板每次危机都当机会，公司越打越强',
      '我认识的人不怕失败，一次次跌倒一次次站起来，现在没有人敢小看他',
      '我朋友说他最感谢的是那些逼他的人，因为没有压力他不会成长',
      '我认识一个创业者，连续失败三次，第四次成功了，现在身价过亿',
      '我前辈说，越是危险的事，回报越高，关键是你有没有勇气',
      '我认识的人在行业最黑暗的时候进场，现在收益是别人的十倍',
      '我朋友说，每一次的绝境都是上天给的机会，你只需要抓住',
    ],
    worst:[
      '我认识的人做事太冲动，没有计划就进场，结果损失惨重',
      '我朋友太好胜，什么都要争第一，结果得罪了很多人，最后孤立无援',
      '我认识的人承受不了压力，一遇到困难就放弃，从来没有完成过一件事',
      '我老板太激进，公司扩张太快，资金断链，差点倒闭',
      '我朋友什么都敢说，结果说错话，丢失了一个大客户',
      '我认识的人太冒险，把所有鸡蛋放在一个篮子里，最后全部输光',
      '我同事脾气太大，一发怒就控制不了，结果和老板大吵，被炒了',
      '我朋友太好强，明明做不到还要撑面子，结果越陷越深',
      '我认识的人做事太随意，没有后路就往前冲，结果走投无路',
    ],
  },
  // 五鬼星 (field index 5)
  {
    id:'wugui', name:'五鬼星 👻', color:'#f97316',
    best:[
      '我认识的人很聪明，能看见别人看不见的机会，总是快人一步',
      '我朋友有一种直觉，每次都能在问题变大之前解决掉',
      '我老板的思维很不一样，别人觉得是问题的，他都能找到出路',
      '我认识的人很善于读人心，知道客户在想什么，成交率特别高',
      '我朋友有创意，能把简单的事情做出不一样的感觉，让人印象深刻',
      '我认识的人总是能找到捷径，同样的目标他用一半的时间达到',
      '我前辈能感知趋势，在大多数人还没意识到的时候已经布局好了',
      '我朋友善于变通，遇到问题不会死磕，总能找到另一条路',
      '我认识的人思维灵活，能把危机变成转机，每次都化险为夷',
    ],
    worst:[
      '我认识的人太聪明，喜欢走捷径，结果被人发现，信用全毁',
      '我朋友太有创意，但从不落实，想法一堆，成果是零',
      '我老板思维跳跃，但员工跟不上，团队一盘散沙',
      '我认识的人太爱耍小聪明，结果被合伙人坑了，损失了所有积蓄',
      '我朋友有点投机取巧，走了很多弯路，最后还是回到原点',
      '我认识的人太会算计，结果人家都不想跟他合作，越来越孤立',
      '我同事喜欢钻漏洞，被发现后名声扫地，再也没有人信任他',
      '我朋友太善变，今天这样明天那样，让人不知道该怎么和他合作',
      '我认识的人太有心机，把聪明用错地方，结果伤了很多人，也伤了自己',
    ],
  },
  // 六煞星 (field index 6)
  {
    id:'liusha', name:'六煞星 🌊', color:'#06b6d4',
    best:[
      '我认识的人人缘很好，走到哪里都有人帮，从不缺少机会',
      '我朋友很会说话，跟任何人都能聊得来，客户都变成了朋友',
      '我老板很懂得维系关系，20年前的客户到现在还在合作',
      '我认识的人善于建立信任，客户愿意把最重要的事交给他',
      '我朋友有一种魅力，能让人感觉被重视，所以大家都喜欢靠近他',
      '我认识的人很会处理冲突，每次都能让两边都满意',
      '我前辈说，人脉不是认识多少人，是多少人愿意在你困难的时候帮你',
      '我朋友的成功，60%来自人脉，因为他对每个人都真诚',
      '我认识的人会用情感连接客户，不是卖产品，是卖信任',
    ],
    worst:[
      '我认识的人太依赖关系，一旦关系断了，什么都没有了',
      '我朋友太好说话，什么都答应，结果被人占便宜，累死自己',
      '我认识的人喜欢讨好所有人，结果没有人真正尊重他',
      '我老板太重感情，明明知道合伙人不对，还是不忍心说，最后吃了大亏',
      '我朋友太念旧，明明关系已经不好了，还是不肯放手，消耗了很多精力',
      '我认识的人做事太讲人情，结果原则一再妥协，工作越来越难做',
      '我同事太依赖朋友介绍生意，一旦朋友的资源用完，就不知道怎么办',
      '我朋友太感性，做决定都靠感觉，结果错误的人际关系影响了事业',
      '我认识的人把生意和感情混在一起，最后生意做砸，朋友也没了',
    ],
  },
  // 祸害星 (field index 7)
  {
    id:'huohai', name:'祸害星 🔥', color:'#dc2626',
    best:[
      '我认识的人经历了很多挫折，但每一次都让他更清楚自己要什么',
      '我朋友被最信任的人背叛，反而让他学会了辨别人，现在眼光特别准',
      '我老板说，他最感谢的是那些让他受苦的人，因为那些苦造就了今天的他',
      '我认识的人经历了破产，重新站起来的他，比以前更有智慧',
      '我朋友经历了一段很痛的感情，反而让他更珍惜现在的关系',
      '我认识的人每次遇到障碍，都把它当成修炼，现在他的承受力是常人的三倍',
      '我前辈说，没有经历过真正的苦难，就不知道自己有多强',
      '我朋友经历了最黑暗的时期，反而激发了他从未有过的潜能',
      '我认识的人受过很多委屈，但他把每一个委屈都变成了前进的燃料',
    ],
    worst:[
      '我认识的人总是遇到烂人，感情、事业都被拖累，好像有人专门来消耗他',
      '我朋友很努力，但运气一直不好，每次快成功就会出现意外',
      '我认识的人做了很多好事，但生活一直不顺，总是有意外出现',
      '我老板遇到一个合伙人专门来破坏，结果公司差点关门',
      '我朋友遇人不淑，被骗了钱，还被泼脏水，名声受损',
      '我认识的人总是遇到是非，明明没有做错，但总是被卷进麻烦',
      '我同事很善良，但偏偏遇到最会利用善良的人，一次又一次受伤',
      '我朋友说，他这辈子最大的问题不是能力，是身边总有人拖他的后腿',
      '我认识的人努力了十年，但每次接近目标就会出现一个问题，让他前功尽弃',
    ],
  },
];

let currentField = 0;
let currentMode = 'best';

function renderFieldButtons(){
  const wrap = document.getElementById('field-btns');
  if(!wrap) return;
  wrap.innerHTML = FIELDS.map((f,i)=>`
    <button class="f-btn${i===currentField?' active':''}"
      style="${i===currentField?'background:'+f.color+';color:#fff;border-color:'+f.color:'border-color:'+f.color+';color:'+f.color}"
      onclick="selectField(${i})">${f.name}</button>
  `).join('');
}

function selectField(idx){
  currentField = idx;
  renderFieldButtons();
  renderContent();
}

function setMode(mode){
  currentMode = mode;
  document.getElementById('btn-best').style.background = mode==='best'?'#22c55e':'#e8e8e8';
  document.getElementById('btn-best').style.color = mode==='best'?'#fff':'#555';
  document.getElementById('btn-worst').style.background = mode==='worst'?'#ef4444':'#e8e8e8';
  document.getElementById('btn-worst').style.color = mode==='worst'?'#fff':'#555';
  renderContent();
}

function renderContent(){
  const f = FIELDS[currentField];
  const items = f[currentMode];
  const colorMap = {'best':'#16a34a','worst':'#dc2626'};
  const col = colorMap[currentMode];
  document.getElementById('field-content').innerHTML = `
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
}

// ── TOPIC SECTION ──────────────────────────────────────────────
const TOPIC_CATS = [
  {id:'plate',  name:'🚗 车牌',   color:'#ff6496'},
  {id:'phone',  name:'📱 手机号', color:'#a855f7'},
  {id:'house',  name:'🏠 门牌/楼层', color:'#f59e0b'},
  {id:'birth',  name:'🎂 生日',   color:'#06b6d4'},
  {id:'general',name:'💡 通用',   color:'#22c55e'},
];

const TOPIC_DATA = [
  // 车牌
  {cat:'plate', title:'你的车牌号藏着你的人生密码', hooks:[
    {elem:'警示恐惧', text:'很多人开了十年的车，但从来不知道自己的车牌在影响他们的财运'},
    {elem:'揭秘悬念', text:'为什么同样努力，有些人的事业一直卡住？答案可能就在你每天看的车牌号'},
    {elem:'情感共鸣', text:'我也曾经觉得数字只是数字，直到我换了车牌，生意才开始顺了'},
    {elem:'身份认同', text:'马来西亚做生意的你，一定要了解这件事，因为它和你的财富直接挂钩'},
    {elem:'对比反差', text:'同一个路段，两辆车，一个越来越顺，一个越来越堵，区别只有这个'},
    {elem:'互动参与', text:'把你的车牌号码打在评论区，我来帮你解读你的能量磁场'},
    {elem:'实用价值', text:'教你用三秒钟判断你的车牌号是在帮你还是在拖累你'},
    {elem:'争议话题', text:'有人说车牌只是号码，但这些年我见过太多人因为换了车牌，命运真的改变了'},
  ]},
  {cat:'plate', title:'为什么老板都在选这几个车牌数字', hooks:[
    {elem:'警示恐惧', text:'如果你的车牌有这个组合，小心它正在悄悄影响你的贵人运'},
    {elem:'揭秘悬念', text:'马来西亚顶级富商最爱的车牌号码，背后有一个共同规律'},
    {elem:'情感共鸣', text:'我帮一个朋友分析车牌，他第一反应是不信，后来他说"怎么这么准"'},
    {elem:'身份认同', text:'做生意的人，你的车牌就是你的移动名片，它在说什么？'},
    {elem:'对比反差', text:'有些车牌吸财，有些车牌漏财，同样的努力，结果却差十万八千里'},
    {elem:'互动参与', text:'你觉得车牌号码会影响运气吗？评论区说说你的看法'},
    {elem:'实用价值', text:'三个步骤，自己在家就能判断车牌号码的能量属性'},
    {elem:'争议话题', text:'很多人觉得这是迷信，但科学无法解释的事，不代表它不存在'},
  ]},
  // 手机号
  {cat:'phone', title:'你的手机号码泄露了你的性格密码', hooks:[
    {elem:'警示恐惧', text:'你现在用的手机号，可能正在影响你接到的贵人和机会'},
    {elem:'揭秘悬念', text:'为什么有些人手机一响就是好消息，有些人每次接电话都是麻烦？'},
    {elem:'情感共鸣', text:'我换手机号那一年，接到的机会和以前完全不一样，我才开始认真研究这个'},
    {elem:'身份认同', text:'如果你是做销售、做生意的，这条视频你一定要看完'},
    {elem:'对比反差', text:'同一个业务团队，有人电话响不停，有人等了一整天没有一个客户来电'},
    {elem:'互动参与', text:'把你的手机尾四位打在评论区，我来帮你看看你的人际磁场'},
    {elem:'实用价值', text:'教你看手机号的三个关键位置，判断你的财运和贵人运'},
    {elem:'争议话题', text:'你相信手机号码会影响你接到的机会吗？很多人不信，但结果让他们改变了想法'},
  ]},
  {cat:'phone', title:'换了手机号之后，我的生意真的变了', hooks:[
    {elem:'警示恐惧', text:'如果你的手机号里有这个数字组合，你的财运可能一直被拦截着'},
    {elem:'揭秘悬念', text:'同样的产品，同样的价格，为什么有些销售接单接到手软，有些一单都难？'},
    {elem:'情感共鸣', text:'我的学员换了手机号三个月后跟我说，感觉整个人的状态都不一样了'},
    {elem:'身份认同', text:'马来西亚做业务的朋友，你的手机号码正在帮你还是在拖你？'},
    {elem:'对比反差', text:'一个号码帮你吸引贵人，一个号码让你总是遇到麻烦客户，差别就在这里'},
    {elem:'互动参与', text:'你有没有因为号码问题而烦恼过？评论区分享你的故事'},
    {elem:'实用价值', text:'五分钟内，教你自己判断手机号码的吉凶能量'},
    {elem:'争议话题', text:'有人说换手机号太麻烦，但如果现在的号一直让你走霉运，你还会说麻烦吗？'},
  ]},
  // 门牌/楼层
  {cat:'house', title:'你住的楼层正在影响你的健康和财运', hooks:[
    {elem:'警示恐惧', text:'有些楼层住进去就开始漏财，有些楼层越住越旺，你知道自己住的是哪种吗？'},
    {elem:'揭秘悬念', text:'为什么同一栋楼，有些人越住越顺，有些人越住越难？答案就在楼层数字'},
    {elem:'情感共鸣', text:'我有个学员搬到新楼层半年，感情、事业、健康同时改善，她说她都不敢相信'},
    {elem:'身份认同', text:'正在考虑买房或换房的你，这条信息可能帮你省下几十万的错误决定'},
    {elem:'对比反差', text:'同一个小区，一楼层的人生意越做越大，另一楼层的人连续换了三份工作'},
    {elem:'互动参与', text:'你现在住几楼？评论区告诉我，我来帮你分析这个楼层的能量'},
    {elem:'实用价值', text:'教你用数字能量学，在五分钟内判断一个楼层是否适合你'},
    {elem:'争议话题', text:'楼层影响运势？很多人第一反应是不信，但我帮上千人分析后发现规律很明显'},
  ]},
  // 生日
  {cat:'birth', title:'你的生日数字决定了你最适合做什么生意', hooks:[
    {elem:'警示恐惧', text:'很多人一生努力，却做了不适合自己天赋的事，原因可能就在生日数字里'},
    {elem:'揭秘悬念', text:'为什么有些人天生就适合做销售，有些人适合做管理？生日数字有答案'},
    {elem:'情感共鸣', text:'我分析自己生日那天，才终于明白为什么有些事我怎么做都很吃力'},
    {elem:'身份认同', text:'正在创业或考虑转行的你，这条视频可能帮你找到最适合的方向'},
    {elem:'对比反差', text:'同样努力，有人越做越顺，有人越做越累，不是能力问题，是方向问题'},
    {elem:'互动参与', text:'把你的生日（月份+日期）打在评论区，我来帮你看看你的天赋磁场'},
    {elem:'实用价值', text:'三个步骤，用生日数字找出你最强的能量磁场和最适合的事业方向'},
    {elem:'争议话题', text:'用生日判断天赋？听起来像命理，但背后的数字逻辑让很多理性的人也改变了看法'},
  ]},
  // 通用
  {cat:'general', title:'为什么有些人天生就比较旺？', hooks:[
    {elem:'警示恐惧', text:'如果你总是感觉努力但事倍功半，问题可能不在你的行动，而在你的能量磁场'},
    {elem:'揭秘悬念', text:'易经数字能量学到底是什么？为什么全球华人圈里越来越多成功人士在研究这个？'},
    {elem:'情感共鸣', text:'我以前觉得这种东西是老一辈的迷信，直到有一天我亲眼看到它改变了一个朋友的人生'},
    {elem:'身份认同', text:'如果你相信数字背后有规律，相信每个人都有属于自己的能量密码，这条视频是为你拍的'},
    {elem:'对比反差', text:'同样的起点，有些人越走越宽，有些人越走越窄，差别不只是努力，还有方向'},
    {elem:'互动参与', text:'你相信数字能量会影响人的运势吗？评论区告诉我你的想法'},
    {elem:'实用价值', text:'今天教你用一个简单的方法，在三分钟内了解自己的基本能量磁场'},
    {elem:'争议话题', text:'有人说这是迷信，有人说这是科学，但不管你信什么，数字背后的规律真实存在'},
  ]},
  {cat:'general', title:'改变这一件事，我的人生开始不一样了', hooks:[
    {elem:'警示恐惧', text:'你身边那些一直卡住的人，很可能都在用和自己能量相冲的数字'},
    {elem:'揭秘悬念', text:'易经数字能量学里有一个概念，叫做"磁场共振"，懂了这个，你会看世界的眼光都不同'},
    {elem:'情感共鸣', text:'学了数字能量学之后，我开始看懂一些以前不明白的事，包括为什么某些人总是吸引麻烦'},
    {elem:'身份认同', text:'给所有想要突破现状、活得更清醒的人——这是一套值得花时间了解的系统'},
    {elem:'对比反差', text:'同样的号码，用对了是助力，用错了是阻力，关键在于你有没有意识到这件事'},
    {elem:'互动参与', text:'如果你想了解自己的数字能量，评论区留下你的出生年月日，我会一一回复'},
    {elem:'实用价值', text:'今天分享数字能量学入门最重要的三个概念，学完你就能自己开始分析'},
    {elem:'争议话题', text:'很多人问我，学这个有什么用？我的答案是：当你开始看懂数字背后的语言，决策会变得清晰很多'},
  ]},
];

let currentCat = 'plate';

function renderTopicCats(){
  const bar = document.getElementById('cat-filter-bar');
  if(!bar) return;
  bar.innerHTML = TOPIC_CATS.map(c=>`
    <button class="cat-f-btn${c.id===currentCat?' active':''}"
      style="background:${c.id===currentCat?c.color:'#f0f0f0'};color:${c.id===currentCat?'#fff':'#555'};border:none;border-radius:10px;padding:6px 14px;font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;"
      onclick="switchCat('${c.id}')">${c.name}</button>
  `).join('');
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
}

window.addEventListener('DOMContentLoaded', ()=>{
  renderFieldButtons();
  renderContent();
  renderTopicCats();
  renderTopics('plate');
});
</script>
</body>
</html>
"""

with open('instagram_growth_mobile.html', 'w', encoding='utf-8') as f:
    f.writelines(kept)
    f.write(MISSING)

print("Done! Total lines:", sum(1 for _ in open('instagram_growth_mobile.html', encoding='utf-8')))

# Verify closing tags
import subprocess
result = subprocess.run(['grep', '-c', '</html>', 'instagram_growth_mobile.html'], capture_output=True, text=True)
print("</html> count:", result.stdout.strip())
result2 = subprocess.run(['grep', '-c', '</script>', 'instagram_growth_mobile.html'], capture_output=True, text=True)
print("</script> count:", result2.stdout.strip())
