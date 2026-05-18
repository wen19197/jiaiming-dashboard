#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html as he, re

FILE = '/sessions/festive-determined-hawking/mnt/outputs/instagram_growth_mobile.html'
def e(s): return he.escape(str(s))

SCRIPTS = [
{
'id':1,'title':'专业的事情交给专业的人做',
'type_tags':['对话','晒过程'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['professional','pattern'],
'shoot_type':'对话 · 晒过程',
'duration':'60–90 秒',
'scene':'工作室桌面，IP 与 A 自然坐谈，桌上摆满各款磁场号码牌（自制道具）。镜头给到牌子特写再切人脸。',
'emotion':'B（IP）扮演被调侃的大哥，宠溺无奈，最终反将一军。内心独白：「我就是这种风格，你别逼我装正经。」',
'field_topic':'延年磁场（道具展示）',
'shoot_topic':'电话号码',
'curve':'😄 好奇开场 → 😂 搞笑展示道具 → 😤 被要求"正经" → 😅 拒绝抵抗 → 😎 反将一军',
'hook':'【反差】玄学老师在做手工牌子？/ 【揭秘悬念】这些牌子到底是用来做什么的？',
'script':'''A：给你做这么多牌做什么呢？这些牌是拿来做什么的？

B：哦，这些啊，我拿来拍视频用的啦。怕有时候他们看不懂嘛，他们听不懂什么是数字能量嘛。我把那个号码全部拼出来，这样子他们不是懂了咯。

A：哦，是哦，我都忘记我们是教育频道了，我们是教那种正能量的。这样子哦，你拿那个牌，你就讲。大家好，这个是延年磁场。延年磁场号码是 1991。

B：我没有这样子的啦。我都不是这样的人，直接没有那个感觉了。

A：你是玄学老师，你一定要正经，要端庄，要专业。

B：我是很专业，可是我不是一个正经的人。我是那种搞笑的人来的，你要这样子我怎样哦？

A：你就装啊，你就装那种正经的风水老师。

B：不可以不可以，做不到啊！

A：又不可以，一点点都不可以。

B：这样子你来拍比较快啦。你来，camera 让我帮你拿，你来讲。

A：这样子不可以，我看起来像风水老师咩？我头发黄黄这样，头发又没有梳高高，穿得拉里，邋遢这样。专业的事情交给专业的人做。''',
'ending':'「专业的事情交给专业的人做」—— 语言钉【professional】全场记住这句话。',
'cover_l1':'我很搞笑','cover_l2':'专业我也在行',
'ig_caption':'你叫我装正经？装不了的。但教你数字能量，这个我绝对在行 😏 #数字能量 #电话号码风水',
},
{
'id':2,'title':'生气磁场：听起来很好，用了躺平',
'type_tags':['对话','聊观点'],'field_tags':['生气磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['balia','settle'],
'shoot_type':'对话 · 聊观点',
'duration':'60–90 秒',
'scene':'两人坐谈，自然随意，可在咖啡厅或工作室。B 像在讲身边真实故事。',
'emotion':'B（IP）是见多识广的顾问，半认真半搞笑。把自己当做在吐槽朋友故事的大哥，但引出的结论是真知识。',
'field_topic':'生气磁场 14/41 67/76 93/39 28/82',
'shoot_topic':'电话号码',
'curve':'😏 吐槽朋友开场 → 😂 笑点堆叠（友族/5个孩子） → 🎯 引入号码 → 😮 揭示"生气"名字误解 → 💡 真相揭示',
'hook':'【人群】你有没有认识那种，每天嘻嘻哈哈但就是没有上进心的人？/ 【奇葩猎奇】30岁5个孩子月收2千',
'script':'''A：欸，我有一个朋友哦，他每个月赚两千块，每天在家里嘻嘻哈哈的。

B：赚钱，开心不就好咯。

A：他都三十岁了咯。他还在做服务员呢。

B：服务员有什么不好咩，怎么你歧视服务员？

A：我不是歧视，30岁要5个小孩养，2000哪里够哦。

B：等下，30岁5个小孩？他是…友族同胞还是…？

A：华人嘞，30岁才生5个，少了咯。

B：这样是他家里有钱？爸爸是ZUS Coffee的CEO，妈妈是99 Speedmart的股东？

A：他爸爸妈妈都退休了咯，每个月拿养老金来养孩子。

B：有一种号码哦，听起来是很好，但是用了哦，反而会让一个人没有动力。

A：什么号码？

B：14/41、67/76、93/39、28/82，这个叫生气磁场。

A：等下你有搞错吗，你不是讲听起来很好，生气磁场，听起来一点都不好嘞。

B：生气磁场最差，会让一个人只懂享受当下，没有进取心，安逸到balia都不知道。今天做到哪里就到哪里，settle了。''',
'ending':'生气磁场最差：不是发脾气，是没有动力。你认识这样的人吗？',
'cover_l1':'每天嘻嘻哈哈','cover_l2':'月底钱不见了',
'ig_caption':'有些号码，听起来很励志，用了反而让你躺平。这就是生气磁场最差的秘密 😶 #数字能量',
},
{
'id':3,'title':'五鬼磁场最好：做Marketing的人适合什么号？',
'type_tags':['对话','教知识'],'field_tags':['五鬼磁场'],'theme_tags':['电话号码'],
'priority':'📈 涨粉利器','lang_nail':['PRO','聪明'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A像是帮自己问问题的朋友，B解答中夹带笑点。',
'emotion':'B（IP）假装被问到很基础的问题，表情和语气带点无奈，但讲到知识点时变得专业。',
'field_topic':'五鬼磁场（聪明创意）',
'shoot_topic':'电话号码',
'curve':'😅 大型误解开场（电话 vs 电话号码） → 😂 来回绕圈笑点 → 🎯 引入五鬼磁场优势 → ⚠️ 搭配警告',
'hook':'【奇葩猎奇】电话问题引发大型误会 / 我以为他要问我买什么牌手机',
'script':'''A：像我这样做 Marketing 的人适合用什么电话好呢？

B：你应该用 iPhone 咯，比较顺嘛。

A：你有听错我的问题吗？我是讲电话哦。

B：电话啦，iPhone 不是电话？

A：电话啊，电话号码。

B：你刚才不是问电话？

A：在我们那边，电话就是电话号码来的。

B：这样子，电话是什么？

A：手机。

B：……

B：好啦，做 Marketing 最需要的是聪明的 Idea，创意，跳出框框的思维，这种人适合有五鬼磁场的号码。五鬼磁场让你思维灵活，鬼主意多，很 PRO。

A：哇，那我要用！

B：但是要看搭配，如果五鬼磁场搭配到绝命磁场，你的鬼主意就全部用在错误的地方了。''',
'ending':'五鬼磁场：聪明归聪明，但搭配很重要，搭错了就变鬼主意用错地方。',
'cover_l1':'做Marketing的','cover_l2':'聪明要用对地方',
'ig_caption':'电话跟电话号码不一样，这你们知道吗？哈哈 第一次被这样误解 😂 #五鬼磁场 #数字能量',
},
{
'id':4,'title':'五鬼磁场最差：那种做夜场的号码特征',
'type_tags':['对话','聊观点'],'field_tags':['五鬼磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['pattern'],
'shoot_type':'对话 · 聊观点',
'duration':'45–60 秒',
'scene':'两人坐谈，轻松氛围，A像在出搞笑题目考 B。',
'emotion':'B（IP）扮演被纠正问题的专家，假装委屈，讲完反而引出真知识。',
'field_topic':'五鬼磁场（夜猫子能量）',
'shoot_topic':'电话号码',
'curve':'😂 搞笑描述夜场特征（答非所问） → 😤 被纠正 → 🎯 引入号码的夜场 pattern',
'hook':'【人群】那种经常去夜场的人，你知道他们有什么共同 pattern 吗？',
'script':'''A：那种经常做夜场的人都有什么特征嘞？

B：第一：黑眼圈重；第二：身上喜欢喷香水；第三：晚睡咯。

A：我的问题都不是这个。

B：你刚刚问什么？

A：你听多一次啊，那种每天去夜场的人哦，他都是用什么样的号码？

B：你刚刚都不是这样问？

A：是你听错了。

B：哎，不过我们讲一下，有什么样的号码容易让一个人喜欢夜生活。五鬼磁场如果搭配不好，会让一个人喜欢黑夜，逃避白天的责任，什么计划都要到晚上才有精神。这就是 pattern 了。''',
'ending':'五鬼磁场最差：不是坏人，是号码让你成为夜猫子，白天的机会都错过了。',
'cover_l1':'天黑才有精神','cover_l2':'太阳出来就睡觉',
'ig_caption':'不是说做夜场不好，是有些号码真的特别容易吸引这种夜猫子的 pattern 😴 #五鬼磁场',
},
{
'id':5,'title':'行业观点：号码全放吉星是误解',
'type_tags':['对话','聊观点'],'field_tags':['多磁场'],'theme_tags':['电话号码'],
'priority':'⚡ 热点话题','lang_nail':['professional','PRO'],
'shoot_type':'对话 · 聊观点（行业观点）',
'duration':'60–90 秒',
'scene':'两人正面坐谈，A 像在替其他老师「挑战」B，B 专业反驳但不失礼。',
'emotion':'B（IP）扮演被挑战的专家，冷静、自信，用道理说服对方。内心是：「这个误解我解释了很多次，没关系，再解释一次。」',
'field_topic':'生气磁场 + 天医磁场（双面性）',
'shoot_topic':'电话号码',
'curve':'😤 挑衅开场 → 🛡️ 防御 → 💡 解释号码双面性 → 😮 具体举例颠覆认知',
'hook':'【争议话题】有老师说你讲的是错的！号码只可以放吉星！',
'script':'''A：你对数字的讲法是不是有什么误解？

B：怎么勒？

A：我听其他的老师讲了哦，号码只可以放吉星，不可以放凶星的嘞。你跟我讲什么五鬼六煞，呸，都骗人。

B：号码不是讲全部放好的就是好，号码都是有好有坏的。

A：怎样讲？

B：比如讲，生气磁场虽然很好，天医磁场虽然很好，但是他们用多了，会导致一些副作用。生气磁场太多会让你没有安全感，停不下来；天医磁场太多会让你善良心软，容易被人骗。

A：哦……所以不是全部放好星就最好？

B：对，号码的平衡才是关键。一个 professional 的看法是：70% 吉星，30% 凶星，这样才是最完整的能量搭配。''',
'ending':'号码有好有坏，关键是平衡，不是全放吉星。这才是 professional 的思维。',
'cover_l1':'全部放好星','cover_l2':'反而没有一样好',
'ig_caption':'有没有人也这样跟你讲，号码只能放吉星，放凶星是骗人的？我来帮你破解这个误解 👇 #数字能量',
},
{
'id':6,'title':'六煞磁场最好：帅哥美女的号码',
'type_tags':['对话','教知识'],'field_tags':['六煞磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['atas','形象'],
'shoot_type':'对话 · 教知识',
'duration':'45–60 秒',
'scene':'两人对谈，A 从外表切入，话题自然过渡到号码。IP 可以穿搭整洁上镜。',
'emotion':'B（IP）假装被嘲外表，但从容带过，自信引出号码知识。语气轻松 atas。',
'field_topic':'六煞磁场 16/61、38/83',
'shoot_topic':'电话号码',
'curve':'🧐 外貌切入 → 😂 穿搭 vs 中装笑点 → 🎯 穿搭与号码的关系 → 💡 六煞磁场揭示',
'hook':'【反差】风水老师穿 T-shirt 不穿中装？/ 【荷尔蒙】帅哥美女的号码都有这个',
'script':'''A：数字能量老师都是穿到这样的咩？

B：OK嘛这样，长裤，T-shirt。

A：数字能量不是风水来的？

B：是啊，算是电话号码的风水咯。

A：风水老师不是应该穿中装，然后留个胡子，手上带一个佛珠？

B：没有啦，我只是讲究形象嘛，穿到整齐点，得体就 OK 了咯。

A：这样穿搭跟号码有关系的吗？

B：肯定有。

A：什么关系勒？号码哦。

B：是啦，像我这样的帅哥，或者是美女，他们的号码里面通常有 16、61 这样的数字。这个叫六煞磁场，最好的时候，会让一个人很注重形象，很 atas，很有魅力，自然就容易吸引到好的人和机会。''',
'ending':'六煞磁场最好：形象感强，有魅力，atas。帅哥美女的号码通常都有这个。',
'cover_l1':'有不有钱不重要','cover_l2':'你帅就完事了',
'ig_caption':'帅哥美女的号码里通常都有这个磁场，你有吗？😏 #六煞磁场 #数字能量',
},
{
'id':7,'title':'数字4到底好不好？天医 vs 绝命',
'type_tags':['对话','教知识'],'field_tags':['天医磁场','绝命磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['PRO','pattern'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 像个死板的普通人带着迷信问题来问，B 耐心纠正。',
'emotion':'B（IP）被反复绕圈，表情逐渐从无奈到认真，最后专业解释，有点像在教小朋友。',
'field_topic':'天医磁场 49/94，绝命磁场 48/84',
'shoot_topic':'电话号码',
'curve':'😵 简单问题绕圈圈 → 😤 揭示迷信误解 → 💡 两个两个看的规则 → 😮 49天医 vs 48绝命的反转',
'hook':'【争议话题】4号到底好不好？很多人问这个 / 【揭秘悬念】你爸爸说的不一定对',
'script':'''A：数字4好吗？

B：什么意思数字4？

A：4咯，就4号这个号码OK吗？

B：怎样讲OK不OK勒？

A：我就想知道4号好不好罢了。

B：4号……ok啊，没有怎样啊。

A：你不是讲数字能量的，4号没有讲好不好的咩？

B：数字能量号码是两个两个看的嘞，大哥。

A：因为我听我爸爸讲哦，4号不好哦。

B：怎么又不好？

A：4号嘛……（空中用手指画出一个「死」字）

B：没有这样讲的啦，号码是要两个两个看的。比如4接去9，等于49，这个是天医磁场，代表财富，代表贵人，代表健康。但是如果4接去8，反而等于48，这个是绝命磁场，代表破财，代表意外。所以不是4不好，是要看他接去哪里，这才是 PRO 的看法。''',
'ending':'数字4要看搭配。49天医，代表财富；48绝命，代表破财。不是4不好，是你没有两个两个看。',
'cover_l1':'4号到底好不好','cover_l2':'你爸爸说的不算',
'ig_caption':'你妈妈叫你不要用4，我来告诉你为什么这是一个误解 😅 #天医磁场 #绝命磁场 #数字能量',
},
{
'id':8,'title':'天医磁场最好：他们说换了号码不一样了',
'type_tags':['对话','晒过程'],'field_tags':['天医磁场'],'theme_tags':['电话号码'],
'priority':'📈 涨粉利器','lang_nail':['PRO','atas'],
'shoot_type':'对话 · 晒过程',
'duration':'60–75 秒',
'scene':'两人坐谈，B 展示换号码后的真实反馈（截图/案例），A 半信半疑不断追问。',
'emotion':'B（IP）从容自信，被质疑时不急不躁，用事实说话。一种「你信不信都是真的」的笃定。',
'field_topic':'天医磁场 13/31 68/86 49/94 27/72',
'shoot_topic':'电话号码',
'curve':'😤 被质疑开场 → 🎯 展示成功案例 → 😂 好奇追问 → 💰 笑点结尾（5000块散钱）',
'hook':'【最好案例】换了号码之后他们都说不一样了 / 【反差】5000块叫散钱？',
'script':'''A：呐，抓到，换号码都可以中马票，还讲不可以。

B：这个不一样，这个是他们自己经常都有在买马票的。

A：这些是什么？

B：有些是做网店的爆单，有些是事业有上升咯。

A：这个嘞（指中TT的）。

B：如果你也常买就可以啦。

A：我每次都有买的，每次都是买5边，24打。

B：买多少？

A：比5。

B：5块？

A：5000。散钱。''',
'ending':'天医磁场带来财运机会，但你自己要有行动。不行动，号码也帮不了你。',
'cover_l1':'换了号码之后','cover_l2':'他们都说不一样了',
'ig_caption':'5000块，他说是散钱 😂 不管你信不信，这些都是真实发生的事 #天医磁场 #数字能量',
},
{
'id':9,'title':'稳定破财：收入稳定但永远没有钱存',
'type_tags':['对话','教知识'],'field_tags':['天医磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['terbalik','settle'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 一脸困惑，B 像在帮他诊断问题的顾问。',
'emotion':'B（IP）扮演见多识广的大哥，听完 A 的情况点了点头说「这个我见过」，专业但有趣。',
'field_topic':'天医磁场 13/31 68/86 49/94 27/72（不足时的反效果）',
'shoot_topic':'电话号码',
'curve':'😕 矛盾开场（稳定但没钱） → 😂 terbalik 笑点 → 🎯 引入天医磁场不足的诊断 → 💡 解决方向',
'hook':'【人群】那种收入很稳定但永远存不到钱的，你认识吗？/ 【反差】稳定没有钱，terbalik',
'script':'''A：我现在的收入已经很稳定了。

B：哦？这样你找我有什么事吗？

A：找你来改善一下我的钱财。

B：你不是……收入很稳定了还来找我？

A：我现在是稳定没有钱。

B：你这个叫稳定破财，不是收入稳定，terbalik 倒反料。

A：所以我才要找你帮忙嘛，有钱我都不用找你了。

B：一般上如果一个人赚钱辛苦，或是赚没有什么钱，一般上是他的号码里面没有太多天医的磁场，也就是我们讲的 13/31、68/86、49/94、27/72。这种号码的人，财富能量不足，所以钱就像会自动走掉一样，settle 不下来。''',
'ending':'稳定破财 = 号码里天医磁场不足。你的钱不是赚不到，是留不住。',
'cover_l1':'收入很稳定','cover_l2':'永远没有钱存',
'ig_caption':'稳定没有钱，不是赚不够，是号码让你留不住钱。这个叫稳定破财 😶 #天医磁场 #数字能量',
},
{
'id':10,'title':'最贵的号码不是你想的那样',
'type_tags':['对话','聊观点'],'field_tags':['多磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['atas','professional'],
'shoot_type':'对话 · 聊观点',
'duration':'45–60 秒',
'scene':'两人对谈，A 像是带着外行人认知来问，B 纠正认知。',
'emotion':'B（IP）淡定反问，像在纠正客户对行业的误解，语气温和但清晰。',
'field_topic':'多磁场能量搭配',
'shoot_topic':'电话号码',
'curve':'😕 误解开场（靓号 vs 能量号） → 😂 笑点澄清 → 💡 解释数字能量的真正价值',
'hook':'【争议话题】你不是在卖靓号吗？/ 【揭秘悬念】最贵的号码不是168888',
'script':'''A：你这边最贵的号码多少？

B：什么意思是最贵的号码？

A：你不是数字能量老师。

B：是啊。

A：你没有卖那种，美美的，然后很有 yeng 的电话号码 meh？

B：什么，什么是美美的号码，那种 168888 啊还是 8886888 啊？

A：对对对，就是那种。

B：没有啦，我不是卖号码的。数字能量不是靓号生意，是号码的能量搭配。168888 好不好听是一件事，但他的能量组合适不适合你，是另一件事。一个 professional 的人，选号码是看能量，不是看好不好听。''',
'ending':'数字能量不是卖靓号，是帮你找到适合你的能量组合。atas 的人，选的是能量，不是外表。',
'cover_l1':'最贵的号码','cover_l2':'不是你想的那样',
'ig_caption':'你以为数字能量老师是在卖靓号？我们不是那样运作的 😌 #数字能量 #电话号码',
},
{
'id':11,'title':'来换号码，顺便被卖了保险',
'type_tags':['对话','晒过程'],'field_tags':['天医磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['PRO','大儿子'],
'shoot_type':'对话 · 晒过程',
'duration':'75–90 秒',
'scene':'两人坐谈，A 扮演自称是保险 agent 的客户，不断转移话题推销保险，B 温和反将回主题。',
'emotion':'B（IP）扮演冷静被推销的大哥，幽默应对，但引出天医磁场的两面性时变认真。',
'field_topic':'天医磁场 13/31 68/86 49/94 27/72',
'shoot_topic':'电话号码',
'curve':'😊 朋友推荐开场 → 😂 被推销保险笑点 → 🎯 转回正题 → ⚠️ 天医太多副作用（做别人大儿子）',
'hook':'【奇葩猎奇】来换号码被反推销保险 / 【揭秘悬念】天医磁场太多也有问题',
'script':'''A：我朋友介绍我来换号码。

B：哦？朋友介绍来的，哪一个朋友？

A：你不用管，他说换了之后每个月都多赚一个2到3千哦，有没有淋哦。

B：有没有淋是看你做什么的嘛，可能他做 sales 的，换了号码赚多个2到3千，甚至10多千都有可能。如果你做 admin，你怎样换就是那个上线，我怎样回答你嘞。

A：这个你不用怕，我是做保险的，但是我看你脸色不太好这样嘞。

B：OK 啊，正常啊这样。

A：不是，你要小心嘞，现在哦，很多人都突然生病啊什么的，你最好要有医药卡啊，保险啊，关键时刻，省你一笔钱啊。

B：你是来……换号码还是？

A：来换号码，想了解一下先。我听他们讲号码用像 13、31 这样的天医就可以了是吗？

B：也不是这样讲，13/31 虽然是属于财富的号码，但不是每个人都担得起这个财。而且如果你号码里 13/31、68/86、49/94、27/72 这样的天医磁场太多，你就容易做别人大儿子，容易被骗咯。

A：哦……现在医院很贵啊，如果你没有保险很危险，支持一下咯。''',
'ending':'天医磁场太多副作用：善良心软，做别人大儿子，容易被骗。平衡才是关键。',
'cover_l1':'来换号码的','cover_l2':'顺便卖我保险',
'ig_caption':'来找我换号码，结果被他反推销。这个世界太有趣了哈哈 😂 #天医磁场 #数字能量',
},
{
'id':12,'title':'天医磁场两面性：老婆号码揭秘',
'type_tags':['对话','教知识'],'field_tags':['天医磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['pattern','balia'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 偷偷问老婆号码，整个对话像在替自己"挖坑"，B 最后揭示天医两面性。',
'emotion':'B（IP）像在帮人诊断感情问题的顾问，听完「追老婆经历」假装没事，然后认真揭示号码的心软副作用。',
'field_topic':'天医磁场 49/94（心软、善良的副作用）',
'shoot_topic':'电话号码',
'curve':'😏 偷偷问老婆号码 → 😂 搞笑追老婆经历 → 🎯 揭示天医磁场心软副作用 → 😅 被骗逻辑揭示',
'hook':'【人群】有没有人用数字能量分析过另一半的号码？/ 【奇葩猎奇】早安晚安就追到人',
'script':'''A：你帮人看号码的是吗？

B：是啊。

A：我老婆的号码可以帮我看吗？

B：这样你老婆嘞？

A：你看这边有吗？

B：没有啊，你都一个人罢了。

A：那不是没有在咯，我偷偷问下嘛。

B：这个号码，太多 49/94 了。你看，0149，后面又是 954，这种号码哦就是容易善良心软。这个自己换的还是怎样？

A：自己换的啦，不然怎样 kao 到她嘞。看准了的，起来先发早安，晚上再发一句晚安，偶尔爽爽问下吃饱了吗，就仙到了。

B：很多人会以为 49 这样的号码是天医很好，但号码是有两面性的。通常天医磁场像 13/31、68/86、49/94、27/72 太多，很容易善良心软，不懂得拒绝的，所以就很容易被像你这样 balia 的人骗咯。''',
'ending':'天医磁场太多：善良心软，pattern 就是被人骗。你身边有这样的人吗？',
'cover_l1':'你的善良','cover_l2':'是他的武器',
'ig_caption':'号码里天医磁场太多，容易善良心软，不懂拒绝。你身边有这样的人吗？😶 #天医磁场',
},
{
'id':13,'title':'换号码的条件，刁钻到换不到',
'type_tags':['对话','聊观点'],'field_tags':['多磁场'],'theme_tags':['电话号码'],
'priority':'😂 搞笑内容','lang_nail':['PROMAX','balia'],
'shoot_type':'对话 · 聊观点',
'duration':'45–60 秒',
'scene':'两人坐谈，A 像个刁钻客户，越讲条件越荒唐，B 越来越无语。',
'emotion':'B（IP）从耐心解释到无奈，逐渐失去表情，最后反将。语气是忍耐极限的可爱无奈。',
'field_topic':'多磁场（号码选择的原则）',
'shoot_topic':'电话号码',
'curve':'😊 正常开场 → 😅 第一个条件 → 😐 第二个条件 → 😶 第三个条件（全是8） → 😂 反将揭示矛盾',
'hook':'【奇葩猎奇】换号码还有这么多条件？/ 【反差】你的条件比找对象还多',
'script':'''A：我想换一个财运好的号码，但我有几个条件。

B：你讲。

A：第一：号码里面不可以有4，因为4不好听。

B：OK……

A：第二：倒数第三个号码决定不可以有9，因为我不喜欢。

B：……好。

A：第三：最好全部都是8。

B：……

B：你的条件比找另一半还多。不可以有4，不可以有9，全部是8……这样的号码，宇宙间不一定存在。而且就算存在，全是8的号码是伏位磁场，能量是「稳定不动」，你说的财运好，真的不是全部都是8。选号码是配合你的需求，不是满足你的偏好。这个叫 PROMAX 误解。''',
'ending':'换号码是配合你的人生目标，不是满足你的数字偏好。条件越多，越难找到真正适合你的。',
'cover_l1':'换号码有条件','cover_l2':'条件多到换不到',
'ig_caption':'不能有4，不能有9，最好全是8... 这样的号码，你觉得存在吗？😂 #数字能量 #电话号码',
},
{
'id':14,'title':'延年磁场最好：有事业心，但要配合实力',
'type_tags':['对话','聊观点'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['atas','balia'],
'shoot_type':'对话 · 聊观点',
'duration':'60–75 秒',
'scene':'两人坐谈，A 提出荒唐问题，B 无奈分析，引出延年磁场的特质。',
'emotion':'B（IP）被荒唐问题惊到，但很快冷静分析，语气是「你有雄心壮志，但先面对现实」。',
'field_topic':'延年磁场 19/91 78/87 43/34',
'shoot_topic':'电话号码',
'curve':'😲 荒唐问题开场 → 😂 月供分析笑点 → 💡 延年磁场的事业特质 → ⚡ 有雄心但配合实力',
'hook':'【反差】3000预算要选C300？/ 【奇葩猎奇】这种叫有事业，要最好的',
'script':'''A：3000预算你觉得我应该去买Civic还是C300嘞？

B：这个你要去问卖车的嘛，我哪里懂。可是你是要买来怎样？

A：我要买来创业，我今年35岁，敢创业的没有几个啊。

B：哦创业，做什么哦？

A：做Grab。

B：创业做Grab啊，驾很好一下哦，供一辆Bezza都嘛刚了咯。

A：我这种叫有事业，要最好的。

B：你这种就是没有事业心。延年磁场 19/91、78/87、43/34 给一个人的是事业的雄心和规划能力，但雄心要配合实力。3000预算讲Civic和C300，这个不是事业心，这个叫做……balia 的事业心。''',
'ending':'延年磁场给你事业雄心，但雄心要配合你现在的实力。想要 atas，先做到 atas 的事。',
'cover_l1':'3千预算','cover_l2':'你想要C300',
'ig_caption':'有事业心很好，但要配合你现在的实力。延年磁场就是给你这种冲劲 ⚡ #延年磁场 #数字能量',
},
{
'id':15,'title':'延年磁场：300块也要创业',
'type_tags':['对话','聊观点'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'😂 搞笑内容','lang_nail':['settle','存钱先'],
'shoot_type':'对话 · 聊观点',
'duration':'60–75 秒',
'scene':'两人坐谈，A 认真分享"创业计划"，B 越问越崩溃，最后建议先存钱配合好号码。',
'emotion':'B（IP）从认真听到逐渐崩溃，用无奈的关心来收尾，是那种「我是你大哥，我要说实话」的语气。',
'field_topic':'延年磁场 19/91 78/87 43/34（守财守业）',
'shoot_topic':'电话号码',
'curve':'😊 创业话题开场 → 😮 300块揭示 → 😂 逐渐崩溃笑点 → 💡 先 settle，配合延年磁场',
'hook':'【反差】300块要创业？/ 【奇葩猎奇】一个月commitment不到100块',
'script':'''A：我现在有300个，你觉得我创业做什么好勒？

B：300个是？300万？

A：300。

B：300千？

A：300块。

B：300块创什么业？300块拿去打油都不够啊。

A：所以现在300块是不可以创业的？

B：300创业你要怎样创勒？你自己都吃不饱还要创业。

A：我每个月commitment不到100块。

B：这样平常是吃什么？

A：我平常是吃家里住家里的。偶尔去打油一下就100块这样咯。

B：这样200块你要怎样创业勒？你就该好好去做一份工，先存钱先。再来你要用有像 19/91、78/87、43/34 这样的号码，因为这样的号码代表事业，也代表你的守财能力。先把自己 settle 好，号码配合你，才是完整的。''',
'ending':'延年磁场适合守财守业，但你要先把基础做好。先 settle，再谈创业。',
'cover_l1':'300块','cover_l2':'也要来创业',
'ig_caption':'300块创什么业？先存钱先，先把基础打好，号码配合你，才有用 💪 #延年磁场 #数字能量',
},
{
'id':16,'title':'延年磁场最差：McDonald\'s求婚的大方男',
'type_tags':['对话','聊观点'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['cheap','niaoji'],
'shoot_type':'对话 · 聊观点',
'duration':'60–75 秒',
'scene':'两人坐谈，A 很认真分享求婚计划，B 无奈到笑不出来，最后引出延年磁场的小气特质。',
'emotion':'B（IP）是被震惊到的大哥，心里觉得「这样求婚你女朋友不跑才怪」，但还是用理解的语气说出来。',
'field_topic':'延年磁场 19/91 78/87（守财守过头→小气）',
'shoot_topic':'电话号码',
'curve':'😊 结婚话题开场 → 😂 McDonald\'s求婚震惊 → 😤 进一步「排场」分析 → 💡 延年磁场小气特质',
'hook':'【反差】包场McDonald\'s求婚，他觉得这是高规格 / 【人群】那种大方说起来很大方，但花钱时就不见了',
'script':'''A：Bro你结婚了吗？

B：还没有啊。

A：你没有考虑结婚的咩？

B：有啊，还在计划着。

A：我预计下个月我要跟我女朋友求婚了。

B：哦？在哪里求婚嘞？

A：我想好了，McDonald\'s，办最大的那一种。

B：……你求婚，在McDonald\'s求？

A：是啦，包场，RM500 deposit给下去，随便吃随便喝。

B：也是啦，你看你就是McDonald\'s的 spec来的。你觉得你的女朋友同意吗？

A：包同意的嘛，不是什么人都可以随随便便包场的你知道吗。

A：我跟我好brother讲，他讲我niaoji哦，我就来问看你咯。

B：求婚是人生大事，一个女人可能就只有这一次而已。你随随便便在McDonald\'s求婚，我是你女朋友的话我一看到一定包走的。通常像你这样 cheap 的人啊，号码里面一定有 19 跟 91，或者 78/87 这样的。延年磁场守财守过头了，就是小气。''',
'ending':'延年磁场最差：守财守过头就是 cheap。求婚在McDonald\'s包场，你女朋友跑了不要怪号码。',
'cover_l1':'做人讲到很大方','cover_l2':'买单立刻装很忙',
'ig_caption':'求婚在McDonald\'s包场，他觉得这是排场。我是他女朋友一定包走的 😂 #延年磁场 #数字能量',
},
{
'id':17,'title':'延年磁场最差：5块是一天的饭钱上限',
'type_tags':['对话','教知识'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'😂 搞笑内容','lang_nail':['cheap','守财'],
'shoot_type':'对话 · 教知识',
'duration':'45–60 秒',
'scene':'两人坐谈，从点餐话题切入，A 越讲越省，B 自然过渡到号码话题。',
'emotion':'B（IP）被 A 的极度省钱震到，但不批评，只是自然引出号码特质，像是「我理解这种人，这是号码的问题」。',
'field_topic':'延年磁场 19/91（守财→小气）',
'shoot_topic':'电话号码',
'curve':'😊 点餐开场 → 😂 5块上限笑点 → 😮 越来越省 → 💡 19/91的守财特质揭示',
'hook':'【奇葩猎奇】一天饭钱上限5块，在JB怎么活？/ 【反差】守财守到自己也舍不得花',
'script':'''A：我叫Bak Kut Teh，你要什么吗？

B：30块？你赚很多是吗？

A：Bak Kut Teh不是这样子的价钱咯？

B：多料咯，我平常吃饭是不可以超过5块的，5块是我的maximum了咯。

A：5块在JB你可以吃什么？Kopitiam叫一set烤面包都要3、4块了咯。

B：够料咯，2片面包可以顶一天了。

A：来，你给我你的电话号码。

B：怎么的？

A：给就对了。

B：012-1901。

A：19这样的号码勒，就是代表守财，也代表小气。延年磁场最差的地方，就是守财守到连自己都舍不得花，这个就不叫守财，这个叫……cheap。''',
'ending':'延年磁场 19/91：守财能力强，但守过头就是 cheap。连自己都舍不得，不是美德是负担。',
'cover_l1':'守财是美德','cover_l2':'守过头就是小气',
'ig_caption':'19/91这样的号码守财能力很强，但守到连自己都舍不得花，就是另一回事了 😅 #延年磁场',
},
{
'id':18,'title':'延年最差：顶配猪肉粉约会',
'type_tags':['对话','聊观点'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'😂 搞笑内容','lang_nail':['cheap','balia'],
'shoot_type':'对话 · 聊观点',
'duration':'45–60 秒',
'scene':'两人坐谈，A 认真描述自己约会的「高规格消费」，B 无奈配合，最后引出号码分析。',
'emotion':'B（IP）是被荒唐笑死但不表现出来的顾问，表情管理，最后以号码事实收尾。',
'field_topic':'延年磁场（小气、守财过度影响感情）',
'shoot_topic':'电话号码',
'curve':'😤 追女难抱怨开场 → 😂 Kopitiam约会 + 顶配猪肉粉笑点 → 😏 老婆很听话引出 → 💡 延年磁场影响感情',
'hook':'【奇葩猎奇】约会去Kopitiam点顶配猪肉粉，这叫高消费 / 【反差】老婆很听话但原因不太对',
'script':'''A：现在追女孩子很难的啦，一下子就不开心。

B：怎么这样讲嘞？

A：我昨天去追一个，我又带他吃饭又带他玩，喝奶茶什么的，一整天不开心，想到干Dulan。

B：去哪里吃饭哦？

A：去Kopitiam哦。

B：约会去Kopitiam？

A：叫2份Bak Kut Teh，加Daoki，加花肉，加排骨，顶配。没有人敢像我这样消费啊。

B：你女朋友没有干你都不错了咯。

A：没有，我女朋友很听话的，我讲1他不敢讲2的，永远都是我讲的算。

B：……通常延年磁场守财特质太重的人，感情里也容易 cheap，觉得自己「已经很大方了」，但对方感受完全不同。号码里 19/91 太多，就是这种 pattern。''',
'ending':'延年磁场最差影响感情：你觉得顶配猪肉粉是大方，对方觉得你 cheap。号码让你看不见这个差距。',
'cover_l1':'顶配猪肉粉','cover_l2':'这叫高规格约会',
'ig_caption':'他说顶配猪肉粉是约会高消费。他女朋友没有跑已经很有情操了 😂 #延年磁场 #数字能量',
},
{
'id':19,'title':'延年最差（女生）：老婆赚两万老公赚二十',
'type_tags':['对话','聊观点'],'field_tags':['延年磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['terbalik','balia'],
'shoot_type':'对话 · 聊观点',
'duration':'60–75 秒',
'scene':'两人坐谈，A 先分享老婆赚很多，然后一步步揭示自己的情况，越揭示越崩溃。B 最后以号码收尾。',
'emotion':'B（IP）假装没有在评判，但逐渐被真相震惊。语气是「我不评论你的选择，我只说号码的事」。',
'field_topic':'延年磁场 19/91 78/87（女生用→强势、大女人主义）',
'shoot_topic':'电话号码',
'curve':'😊 老婆很厉害开场 → 😮 老公赚多少逐步揭示 → 😂 一天跑一两单笑点 → 💡 女生用延年磁场→强势',
'hook':'【反差】老婆赚2万，老公赚20 / 【人群】那种家里女强男弱的pattern',
'script':'''A：有什么赚钱康头吗？

B：怎么勒？赚没有吃？

A：我的老婆哦，一个月赚20多千，我是干压力，他叫我趴着我是不敢站起来的。

B：这样你自己赚多少？

A：我跑Grab的咯，赚一点散钱。

B：这样一点是多少？

A：比2。

B：200也不错啊，一个月休4天，都可以有5000多。

A：20。

B：……

A：我开车20分钟要休息1个小时，不然我会睡着，所以我平均一天跑一两单。

B：这样你有没有考虑换工作勒？

A：做到好好琢磨换？

B：我是不是有讲了，电话号码，女生不能用 19/91、78/87 这样的号码，容易强势，大女人主义。如果是像你这样啊，赚的又没有对方多，能力又没有对方大，你这种是一定打包的。terbalik 了。

A：我也是很上进一下，每天跑Grab没有休息的。

B：然后一天赚20？''',
'ending':'女生用延年磁场太重：强势、大女人主义。家里谁赚多，号码影响谁说了算。',
'cover_l1':'老婆赚两万','cover_l2':'老公赚二十',
'ig_caption':'女生号码里延年磁场太重，容易大女人主义。家里谁赚多，谁说了算 😂 #延年磁场 #数字能量',
},
{
'id':20,'title':'行业观点：我为什么不卖号码',
'type_tags':['口播','聊观点'],'field_tags':['无'],'theme_tags':['电话号码','品牌建立'],
'priority':'⚡ 热点话题','lang_nail':['professional','pattern'],
'shoot_type':'口播 · 聊观点',
'duration':'60–90 秒',
'scene':'IP 直接对镜头说，背景简洁，语气真诚但坚定。可以有一点辩解感。',
'emotion':'B（IP）是有原则的生意人，被质疑时不生气，只是冷静说出自己的想法。语气是「我想清楚了，我就是这样选择的」。',
'field_topic':'无（品牌建立、行业原则）',
'shoot_topic':'电话号码',
'curve':'🤔 朋友建议引出 → 💰 承认可以赚 → 🛡️ 但我选择不赚 → ❤️ 真正目标是帮助人',
'hook':'【争议话题】放着钱不赚，别人说我傻 / 【情感共鸣】做生意不只是为了钱',
'script':'''最近我有朋友问我，你教这个数字能量这么累干嘛，要学员自己去找号码，几浪费时间。你找一个电信公司合作，他们跟你换了号码，你直接从电信公司拿一个号码给他们。

你讲这个钱我赚得到吗？

赚得到啊。

我肯定赚得到，但是我不要去赚这个钱罢了。

因为你们来找我换号码已经是一笔费用了，今天你去外面找号码，才十多块而已。你何必要多给我这钱来买号码，我何必要多赚你这个钱。

有人说，做生意多赚一笔，没有什么的嘛。

因为我也有公司，有员工要养，我也有爸爸妈妈，我自己也要吃饭，我家里养的鱼也要吃饲料。但是更多的是，我想要通过这个电话号码，去帮助那些生活过到不顺，财运卡住，事业有问题的人。

我有课程，有学员，每个月都有线下场，我现在做的已经很知足了，我不需要靠多卖一个号码来多加我的收入，我需要的是继续做好我在做的事。

赚得到，只是我要不要罢了。这就是我的 professional 原则。''',
'ending':'赚得到，只是我要不要罢了。——这就是 professional 的选择。',
'cover_l1':'赚得到','cover_l2':'只是我不要',
'ig_caption':'有人说我傻，放着钱不赚。但我做这个行业，不只是为了那笔钱 💪 #数字能量 #真心话',
},
{
'id':21,'title':'花钱换号码是人傻钱多？',
'type_tags':['口播','聊观点'],'field_tags':['无'],'theme_tags':['电话号码','观念升级'],
'priority':'📈 涨粉利器','lang_nail':['PRO','PROMAX'],
'shoot_type':'口播 · 聊观点',
'duration':'90–120 秒',
'scene':'IP 直接对镜头，情感递进，像在说服一个犹豫的朋友。语速适中，有停顿感。',
'emotion':'B（IP）是用心为对方着想的导师，不是在推销，是在帮对方看清楚一个问题。语气是真诚的，有点急切但不强迫。',
'field_topic':'无（观念升级）',
'shoot_topic':'电话号码',
'curve':'🤔 反问引出 → 🍔 维度升级（好吃的类比） → 👁️ 不同视角（10年决定） → ⚖️ 权衡利弊 → 💡 情感收尾',
'hook':'【争议话题】有人说换号码是人傻钱多 / 【成本维度】你的10年值多少钱？',
'script':'''花钱去换号码，就是人傻钱多，做自己麻烦？

这样如果我跟你讲，换了号码，你接下来的几个月到未来10年会过得更顺，你觉得你的10年值多少钱？

为什么今天会有人愿意花钱去吃一些很贵的东西呢？

维度升级：你今天花钱买一个好吃的东西，虽然他可能比较贵，但是你吃了会开心，你花钱，你觉得你自己值得吃好一点。那你觉得你未来的10年时间，值得你去投资吗？你觉得你的10年，值多少钱？

不同视角：今天你做出改变，你是想要你未来的5到10年过得好一点，想要自己事业好一点，想让自己赚多一点钱，不要像现在那么辛苦。这些东西只有你自己知道罢了。

很多人会想，我去问我爸爸妈妈意见，问我朋友意见，问另外一半意见。但是你问的这些所有人，都不能帮你的未来做决定。他们爱你，他们担心你被骗，他们担心你做错决定，但他不能替你的未来负责。

权衡利弊：
▸ 不花：省了这笔钱，但你继续在同一个处境里等，没有方向的等它自己变好咯。
▸ 花了：你做了一个主动的选择，你告诉自己：我不想再等了，我的未来值得我为它做点什么。
▸ 两个选择都是你的权利，但10年后回头看，你会庆幸你动了，还是庆幸你省了那笔钱？

人傻钱多，是那些不敢为自己做选择的人，给你贴的标签。''',
'ending':'10年后你会庆幸你动了，还是庆幸你省了那笔钱？—— 这是一个 PROMAX 的人生问题。',
'cover_l1':'你的10年','cover_l2':'值多少钱',
'ig_caption':'花钱换号码是人傻钱多？10年后你会庆幸你动了，还是庆幸你省了那笔钱？🤔 #数字能量 #观念升级',
},
{
'id':22,'title':'祸害磁场最差：什么事都发生在他身上',
'type_tags':['对话','聊观点'],'field_tags':['祸害磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['pattern'],
'shoot_type':'对话 · 聊观点',
'duration':'60–75 秒',
'scene':'两人坐谈，A 吐槽朋友的倒霉经历，B 从号码角度分析。',
'emotion':'B（IP）像是见多识广的朋友，被问到后认真分析但不失幽默，语气是「这个我见过，很多人这样」。',
'field_topic':'祸害磁场 02/20 57/75 69/96',
'shoot_topic':'电话号码',
'curve':'😕 吐槽倒霉朋友 → 🎯 引入祸害磁场 → ⚠️ 口舌是非、招小人的具体影响 → 💡 解决方向',
'hook':'【人群】你有没有认识那种，什么事都偏偏发生在他身上的人？/ 【揭秘悬念】这是 pattern，不是运气',
'script':'''A：你有没有认识那种特别倒霉的人？

B：什么叫特别倒霉？

A：就是那种，今天走路滑倒，明天钱包不见，后天被老板骂，每件事都轮到他。

B：哦，那种叫做倒霉 pattern 了。

A：有没有号码是特别容易这样的？

B：有，这个叫祸害磁场。号码里有 02/20、57/75、69/96 这样的组合，就容易有这种倒霉 pattern。

A：那这样的人，换了号码就好了咯？

B：祸害磁场最差的影响是：口舌是非多，容易招小人，做事经常出乱子，钱也容易因为是非而损失。这不是要吓你，是这种号码的人要更加小心，不要随便得罪人，言多必失。

A：哦……那换了号码就减少这些？

B：换了号码是减少这个能量的影响。但自己的行为习惯也要一起改。''',
'ending':'祸害磁场：口舌是非多、招小人。这不是运气差，是有 pattern 的，可以改变。',
'cover_l1':'什么事都发生','cover_l2':'就是偏偏选上他',
'ig_caption':'运气差不是天生的，有时候是号码在配合你倒霉。你的号码有没有祸害磁场？😶 #祸害磁场',
},
{
'id':23,'title':'绝命磁场最差：赚到钱就会有事要用',
'type_tags':['对话','教知识'],'field_tags':['绝命磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['pattern'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 描述朋友的漏财现象，B 从号码诊断，像顾问给建议。',
'emotion':'B（IP）像个专业的财务顾问，认真帮对方找原因，语气是「这个我见过很多次，让我帮你诊断」。',
'field_topic':'绝命磁场 48/84 36/63（漏财、破财、意外）',
'shoot_topic':'电话号码',
'curve':'😕 朋友漏财现象描述 → 😮 钱会自己走？ → 🎯 号码诊断（绝命磁场） → ⚠️ 破财意外健康的影响 → 💡 解决',
'hook':'【人群】那种努力存钱但每次都有突发事情花掉的人 / 【揭秘悬念】不是你不努力，是号码有漏财开关',
'script':'''A：我有一个朋友，他说他的钱就像有脚一样，一直走掉。

B：怎样的走法？

A：就是放在银行里，突然有事要用，然后就没有了。

B：那不是钱会走，是他总是有事要花。

A：但他没有乱花啊，就是每次有计划存钱，结果都有突发的事情出现。

B：你把他的号码给我看。

A：（念号码给B听）

B：他号码里有 48/84 和 36/63，这两组都是绝命磁场。

A：绝命听起来很恐怖哦。

B：绝命磁场最差的是：破财、意外、健康容易出问题。他不是不努力，是号码里有一个"漏财"的开关，一直没关上。

A：这样换了号码就会好？

B：换了是减少这个能量的影响，但存钱的习惯也要一起改，不然就算换了也很快又有突发情况。''',
'ending':'绝命磁场：破财、意外、健康风险。你的号码有没有 48/84 或 36/63？',
'cover_l1':'赚到钱','cover_l2':'就会有事要用',
'ig_caption':'不是你不努力，是你的号码里有一个「漏财」的开关，一直没关上 😶 #绝命磁场 #数字能量',
},
{
'id':24,'title':'伏位磁场：做了十年还在同一个位置',
'type_tags':['对话','教知识'],'field_tags':['伏位磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['pattern','settle'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 描述朋友的"卡住"现象，B 以伏位磁场分析，像做职业诊断。',
'emotion':'B（IP）是理解这种人的过来人语气，不批评不评判，只是帮对方找原因，有一种「原来如此」的顿悟感。',
'field_topic':'伏位磁场 55/22/99/33/44（重复数字→稳定但原地踏步）',
'shoot_topic':'电话号码',
'curve':'😕 朋友职场卡住现象 → 🤔 能力问题还是意愿问题？ → 💡 伏位磁场的稳定特质 → ⚠️ 舒适区出不去的副作用',
'hook':'【人群】那种做了十年同一份工作，能力很好但就是升不上去的 / 【揭秘悬念】不是没有能力，是号码让他太安逸',
'script':'''A：那种做了十年同一份工作，升不上去的，是什么问题？

B：能力问题？

A：不是，他很能干的，就是跑不出去。

B：是跑不出去，还是不想跑出去？

A：我问他，他说想升，但每次机会来了又觉得算了。

B：哦，这种是伏位磁场太重的表现。

A：伏位是什么？

B：伏位磁场的好处是稳定、忠心、不容易出乱子。55、22、99、33、44这样的重复数字就是伏位。

A：那坏处呢？

B：坏处就是太习惯待在原地，comfort zone 出不去。不是没有能力，是号码让他太安逸，懒得改变，settle 得太早了。

A：那他应该换号码？

B：换号码是其中一个方法，同时他自己也要知道这个 pattern，才可以主动去打破它。''',
'ending':'伏位磁场：稳定但原地踏步。不是没有能力，是号码让你太舒服，舒服到不想动。',
'cover_l1':'做了十年','cover_l2':'还在同一个位置',
'ig_caption':'有些人不是没有能力，是号码让他太舒服，舒服到不想动。你有没有伏位磁场？😶 #伏位磁场',
},
{
'id':25,'title':'车牌也有磁场：你检查过你的车牌吗？',
'type_tags':['对话','教知识'],'field_tags':['延年磁场','天医磁场'],'theme_tags':['车牌'],
'priority':'⚡ 热点话题','lang_nail':['PRO','pattern'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 完全不知道车牌也有磁场，B 耐心解释，可以拿出车牌号码示范。',
'emotion':'B（IP）是在分享新知识的专家，语气轻松，像在教一个完全零基础的朋友。',
'field_topic':'延年磁场 19/91、天医磁场 13/31（车牌应用）',
'shoot_topic':'车牌',
'curve':'😮 车牌也有磁场的惊讶 → 💡 两个两个看的原则（跟电话号码一样） → 📊 具体车牌示范 → ⚠️ 哪些车牌要注意',
'hook':'【揭秘悬念】你的车牌，你有没有检查过？/ 【实用价值】原来车牌跟电话号码一样这样看',
'script':'''A：车牌也有磁场的吗？

B：有啊，车牌跟电话号码是一样的原理，两个两个看的。

A：哦，我以为只有电话号码才有。

B：不是，你的车牌号码，你每天开车都在接收那个能量。

A：那好的车牌是怎样的？

B：比如你的车牌是 WXX 1934，你看，19是延年磁场，34也是延年，93是生气磁场。

A：这样三个全部都是吉星？

B：也不能说全好，要看整体搭配。但这三组组合来说，事业运和冲劲都不错，很 PRO 的搭配。

A：那什么样的车牌是不好的？

B：如果你的车牌有很多 02/20、48/84 这种组合，就要注意了，这些是祸害和绝命磁场。

A：哇，我要去查一下我的车牌了。

B：去查吧，但记得不要只看一对，要整体看，这才是正确的 pattern。''',
'ending':'车牌磁场 = 你每天开车接收的能量。检查你的车牌，看看里面有什么磁场。',
'cover_l1':'车牌不只是号码','cover_l2':'每天都在影响你',
'ig_caption':'你的车牌，你有没有检查过？原来车牌跟电话号码一样，是两个两个看的 😮 #车牌磁场 #数字能量',
},
{
'id':26,'title':'门牌祸害磁场：换家之后变了一个人',
'type_tags':['对话','教知识'],'field_tags':['祸害磁场'],'theme_tags':['门牌'],
'priority':'⚡ 热点话题','lang_nail':['pattern'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 描述朋友搬家后性格变化，B 通过门牌号码分析原因。',
'emotion':'B（IP）像是帮人做能量诊断的专业顾问，认真分析，不夸张不恐吓，让人觉得「原来如此」。',
'field_topic':'祸害磁场 12/21（门牌应用）',
'shoot_topic':'门牌',
'curve':'😕 朋友搬家后变化描述 → 😮 门牌也可以这样分析？ → 💡 长期住在祸害磁场门牌的影响 → 🛡️ 化解建议',
'hook':'【揭秘悬念】换了新家之后开始变得不对劲 / 【人群】你身边有没有搬家后性格大变的人？',
'script':'''A：我有一个朋友，换了新家之后开始变得不对劲。

B：怎样不对劲？

A：以前很开朗的，换了新家之后开始不出门，不社交，整个人很低落。

B：换了多久了？

A：差不多半年。

B：你把他的门牌号码告诉我。

A：B-12-3A。

B：12，21，23这样看。12是祸害磁场，21也是，23就不是最好。

A：门牌也可以这样分析？

B：门牌是你每天回家第一个看到的号码，住在里面的人长期接收这个能量。祸害磁场的门牌，长期住容易情绪不稳定、多疑、人际关系容易出问题，慢慢就不想出门，不想社交。

A：那他要怎样？

B：换一个家是最直接的，或者请人做一些化解的布置。长期住在这种门牌，这个 pattern 会越来越明显的。''',
'ending':'门牌磁场 = 你每天回家接收的能量。12/21 这样的祸害磁场，长期住容易情绪不稳定。',
'cover_l1':'住了新家','cover_l2':'开始变得不对劲',
'ig_caption':'换了新家之后开始变得沉默忧郁？有可能是门牌的问题 😶 #门牌磁场 #祸害磁场 #数字能量',
},
{
'id':27,'title':'换了号码不等于发财：好剑也要会用',
'type_tags':['对话','聊观点'],'field_tags':['天医磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['PRO','professional'],
'shoot_type':'对话 · 聊观点',
'duration':'60–75 秒',
'scene':'两人坐谈，A 质疑换号码的效果，B 用「剑的比喻」解释号码是工具不是magic。',
'emotion':'B（IP）被质疑时不急不辩，冷静用比喻说话，语气是「我理解你的疑问，但答案比你想的更简单」。',
'field_topic':'天医磁场（工具论）',
'shoot_topic':'电话号码',
'curve':'😤 质疑开场 → 🛡️ 冷静应对 → ⚔️ 剑的比喻 → 💡 行动是关键 → 😮 豁然开朗',
'hook':'【争议话题】有朋友说换了号码什么都没改变 / 【实用价值】号码是工具，不是magic',
'script':'''A：我有一个朋友说他换了号码，什么都没有改变。

B：换了之后他有做什么吗？

A：没有，就换了号码，然后等好事发生。

B：就等咯？

A：对。

B：那当然没有什么改变啦。

A：你不是说天医磁场会带来财运吗？

B：会，但是号码是工具，不是magic。

A：什么意思？

B：我讲个例子，一把很好的剑，放在家里不拿出来，敌人来了你还是会输。但是一把好的剑，配合一个训练好的人，才可以赢。号码帮你打开能量的门，但你自己要走进去。这才是 professional 的理解。

A：哦，所以换了好号码，还是要有行动。

B：对，号码是配合你的行动，不是替代你的行动。''',
'ending':'号码是工具，不是magic。好号码 + 你的行动，才是完整的公式。',
'cover_l1':'有好剑','cover_l2':'也要会用剑',
'ig_caption':'号码是工具，不是magic。换了好号码，还是要自己有行动 💪 #数字能量 #天医磁场',
},
{
'id':28,'title':'六煞最差：一有男朋友就乱花钱',
'type_tags':['对话','教知识'],'field_tags':['六煞磁场'],'theme_tags':['电话号码'],
'priority':'🔥 热门主题','lang_nail':['pattern'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 描述朋友的感情花钱 pattern，B 通过号码分析。',
'emotion':'B（IP）像是帮人做感情+财务双诊断的专家，理解这种 pattern 但不评判，只分析原因。',
'field_topic':'六煞磁场 16/61 38/83（感情花钱、判断力下降）',
'shoot_topic':'电话号码',
'curve':'😕 感情花钱 pattern 描述 → 🤔 本性还是号码？ → 🎯 六煞磁场最差特质 → ⚠️ 保护自己的建议',
'hook':'【人群】那种没有男朋友很省，一有男朋友就全部花出去的 / 【揭秘悬念】这不是本性，是号码在影响',
'script':'''A：有那种女生，平时很省的，一有男朋友就开始乱花钱，这样是号码的问题吗？

B：不一定，有可能是本性。

A：不是，我说的是那种，平时真的很省，一交男朋友就全部给他花。

B：有没有那种，没有男朋友的时候正常，一有就失控花钱？

A：对！就是这种！

B：你看看她的号码里面，有没有 16/61 或者 38/83 这样的组合。

A：你怎么知道？

B：六煞磁场最差就是在感情方面判断力下降，很容易为了感情花钱，有时候钱花了，感情还不一定有好结果。这是号码的 pattern，不是她的问题。

A：那她要换号码吗？

B：换了可以减少这种 pattern，但更重要的是，先知道自己有这个倾向，才可以保护自己，不要被那种嘴巴甜但让你破财的人骗。''',
'ending':'六煞磁场最差：感情花钱、判断力下降。这是 pattern，不是本性。换号码+认识自己，才是完整保护。',
'cover_l1':'一有男朋友','cover_l2':'钱就不见了',
'ig_caption':'不是你花心，是号码让你在感情上判断力下降。六煞磁场最差就是这样 😶 #六煞磁场 #数字能量',
},
{
'id':29,'title':'生气磁场最好：不是叫你发脾气，是给你拼劲',
'type_tags':['对话','教知识'],'field_tags':['生气磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['PRO','pattern'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 被之前"最差"的例子影响，以为生气磁场全是坏的，B 解释两面性。',
'emotion':'B（IP）像在纠正误解的老师，耐心但有自信，语气是「每个磁场都有两面，这才是完整的认知」。',
'field_topic':'生气磁场 14/41 67/76 93/39 28/82（竞争力、拼劲）',
'shoot_topic':'电话号码',
'curve':'😕 误解生气磁场只有坏 → 💡 每个磁场有两面 → ⚡ 生气磁场最好：竞争力、拼劲 → 🎯 适合的行业',
'hook':'【揭秘悬念】生气磁场不是叫你发脾气 / 【实用价值】有些行业就是需要这个磁场',
'script':'''A：生气磁场不是最差的咩，怎么说它也有最好？

B：我刚才讲的是生气磁场最差的情况。

A：对，你讲了那个没有动力的例子。

B：每一个磁场都有两面，好的时候是能量的优点，差的时候是能量的弱点。

A：那生气磁场最好是怎样？

B：你知道那种做什么都很拼，很有冲劲，不服输的人吗？

A：知道，那种看到对手比自己好就燃起来的。

B：就是这个，生气磁场最好给你的是一种竞争力，想赢、不怕挑战、越输越想拼。这是 PRO 级别的能量。

A：这种很适合做Sales。

B：Sales、创业，或者任何需要竞争的行业都很适合。14/41、67/76 这样的组合，正确使用就是你最大的优势。''',
'ending':'生气磁场最好：竞争力、拼劲、不服输。有些行业就是需要这个能量，才能赢。',
'cover_l1':'生气磁场','cover_l2':'不是叫你发脾气',
'ig_caption':'生气磁场有最差，也有最好。最好的时候，他给你的是一种想赢的力量 ⚡ #生气磁场 #数字能量',
},
{
'id':30,'title':'全吉星是最好搭配？你想多了',
'type_tags':['对话','教知识'],'field_tags':['多磁场'],'theme_tags':['电话号码'],
'priority':'🌟 常青内容','lang_nail':['PRO','PROMAX'],
'shoot_type':'对话 · 教知识',
'duration':'60–75 秒',
'scene':'两人坐谈，A 提出看似合理但错误的问题，B 用真实逻辑反驳，最后给出正确方向。',
'emotion':'B（IP）像是在解释一个常见误区的专家，有点好笑但不取笑对方，语气是「这个问题很多人问，让我解释清楚」。',
'field_topic':'多磁场平衡搭配（70%吉星+30%凶星）',
'shoot_topic':'电话号码',
'curve':'🤔 合理化问题开场 → 💭 理论上的讨论 → 😮 颠覆认知 → 💡 正确搭配逻辑 → 🎯 个人化建议',
'hook':'【揭秘悬念】全部放吉星不是最好？/ 【争议话题】你以为全好就是好，错了',
'script':'''A：可不可以把所有吉星都放进一个号码？

B：你说什么意思？

A：就是天医、延年、生气、六煞，全部都放进去同一个号码。

B：号码的组合不是你说了算，号码是有限制的。

A：我是说理论上，如果可以，全部放吉星是最好咩？

B：理论上可以，但这样的号码反而会有问题。

A：有什么问题，全部好的不是应该最好吗？

B：你有没有见过那种，财运超好，感情超好，事业超好，社交超好，每样都是顶级的人？

A：没有哦。

B：对，因为一个人的能量是有侧重点的。你全部都放吉星，每样都一点点，反而每样都不突出。最 PRO 的搭配是：70% 吉星，30% 凶星，根据你的目标来侧重。

A：那应该怎样搭配？

B：比如你做Sales，就侧重生气和天医；你想稳定事业，就侧重延年。PROMAX 的做法是根据你的人生目标来配，不是全放好就好。''',
'ending':'最好的号码不是全吉星，而是根据你的目标侧重的搭配。这才是 PROMAX 的做法。',
'cover_l1':'全部放好星','cover_l2':'其实每样都普通',
'ig_caption':'有人问我，可不可以把所有吉星全部放进一个号码？答案出乎你意料 😮 #数字能量 #磁场搭配',
},
]

# ─── CSS to inject ───────────────────────────────────────────────
NEW_CSS = """
/* ===== Script Library ===== */
.sc-prog-bar-wrap{margin:10px 12px 0;display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.04);border-radius:12px;}
.sc-prog-bar{flex:1;height:6px;background:rgba(255,255,255,0.08);border-radius:3px;overflow:hidden;}
.sc-prog-fill{height:100%;background:linear-gradient(90deg,#22d3ee,#a78bfa);border-radius:3px;transition:width .4s;}
.sc-prog-txt{font-size:11px;color:#7070a0;flex-shrink:0;font-weight:700;}
.sc-card{margin:8px 12px 0;border-radius:14px;overflow:hidden;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);transition:opacity .3s;}
.sc-card.filmed{opacity:0.45;}
.sc-card.filmed .sc-title{text-decoration:line-through;color:#505070;}
.sc-head{padding:12px 14px;cursor:pointer;user-select:none;}
.sc-title-row{display:flex;align-items:center;gap:8px;margin-bottom:8px;}
.sc-check{width:17px;height:17px;accent-color:#22d3ee;cursor:pointer;flex-shrink:0;}
.sc-num{font-size:10px;color:#6060a0;font-weight:900;flex-shrink:0;min-width:22px;}
.sc-title{flex:1;font-size:13px;font-weight:700;color:#e0e0f0;line-height:1.3;}
.sc-arrow{font-size:11px;color:#7070a0;flex-shrink:0;transition:transform .25s;}
.sc-arrow.open{transform:rotate(180deg);}
.sc-tags{display:flex;flex-wrap:wrap;gap:4px;}
.stag{font-size:10px;border-radius:5px;padding:2px 7px;font-weight:700;}
.stag.t-type{background:rgba(96,165,250,0.18);color:#93c5fd;}
.stag.t-field{background:rgba(167,139,250,0.18);color:#c4b5fd;}
.stag.t-theme{background:rgba(52,211,153,0.14);color:#6ee7b7;}
.stag.t-prio{background:rgba(255,100,100,0.16);color:#fca5a5;}
.stag.t-lang{background:rgba(253,230,138,0.16);color:#fde68a;}
.sc-body{border-top:1px solid rgba(255,255,255,0.06);padding:12px 14px 14px;}
.sf-row{margin-bottom:10px;}
.sf-label{display:block;font-size:9px;color:#6060a0;font-weight:900;text-transform:uppercase;letter-spacing:.8px;margin-bottom:4px;}
.sf-val{display:block;font-size:12px;color:#c0c0e0;line-height:1.65;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:8px;padding:8px 10px;white-space:pre-wrap;outline:none;min-height:24px;}
.sf-val:focus{border-color:rgba(96,165,250,0.35);background:rgba(96,165,250,0.05);}
.sf-val[contenteditable=true]:empty::before{content:attr(data-ph);color:#404060;font-style:italic;}
.cover-preview{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:10px;}
.cover-line{background:rgba(34,211,238,0.08);border:1px solid rgba(34,211,238,0.2);border-radius:8px;padding:8px;text-align:center;font-size:13px;font-weight:800;color:#a5f3fc;}
.sf-hint{font-size:10px;color:#505070;margin-top:3px;font-style:italic;}
"""

# ─── JS to inject ─────────────────────────────────────────────────
NEW_JS = """
function toggleSC(id){
  var b=document.getElementById('sb-'+id);
  var a=document.getElementById('arr-'+id);
  var open=b.style.display!=='none';
  b.style.display=open?'none':'block';
  a.classList.toggle('open',!open);
}
function markFilmed(evt,id){
  evt.stopPropagation();
  var chk=document.getElementById('chk-'+id);
  var card=document.getElementById('sc-'+id);
  localStorage.setItem('sc-filmed-'+id,chk.checked?'1':'0');
  card.classList.toggle('filmed',chk.checked);
  updateScProg();
}
function updateScProg(){
  var done=0;
  for(var i=1;i<=30;i++){if(localStorage.getItem('sc-filmed-'+i)==='1')done++;}
  var fill=document.getElementById('sc-prog-fill');
  var txt=document.getElementById('sc-prog-txt');
  if(fill)fill.style.width=(done/30*100)+'%';
  if(txt)txt.textContent=done+'/30 已拍摄';
}
function saveScEdit(el,key){
  localStorage.setItem('sc-edit-'+key,el.innerText);
}
function restoreSC(){
  for(var i=1;i<=30;i++){
    var chk=document.getElementById('chk-'+i);
    var card=document.getElementById('sc-'+i);
    if(chk&&localStorage.getItem('sc-filmed-'+i)==='1'){chk.checked=true;if(card)card.classList.add('filmed');}
    var body=document.getElementById('sb-'+i);
    if(body){
      body.querySelectorAll('[data-ekey]').forEach(function(el){
        var saved=localStorage.getItem('sc-edit-'+el.dataset.ekey);
        if(saved!=null)el.innerText=saved;
      });
    }
  }
  updateScProg();
}
"""

# ─── HTML generator ───────────────────────────────────────────────
PRIO_COLOR = {
  '🔥 热门主题':'rgba(255,100,100,0.16)',
  '⚡ 热点话题':'rgba(247,151,30,0.18)',
  '📈 涨粉利器':'rgba(52,211,153,0.14)',
  '🌟 常青内容':'rgba(167,139,250,0.16)',
  '😂 搞笑内容':'rgba(96,165,250,0.16)',
}

def sf(id, key, label, val, big=False):
    ph = '点击编辑...'
    tag = 'div' if big else 'span'
    return (
        '<div class="sf-row">'
        f'<span class="sf-label">{e(label)}</span>'
        f'<{tag} class="sf-val" contenteditable="true" data-ekey="{id}-{key}" '
        f'data-ph="{ph}" onblur="saveScEdit(this,this.dataset.ekey)">'
        f'{e(val)}</{tag}>'
        '</div>'
    )

def cover_row(id, l1, l2):
    return (
        '<div class="sf-row">'
        '<span class="sf-label">🖼️ 封面文字</span>'
        '<div class="cover-preview">'
        f'<div class="cover-line" contenteditable="true" data-ekey="{id}-cover1" onblur="saveScEdit(this,this.dataset.ekey)">{e(l1)}</div>'
        f'<div class="cover-line" contenteditable="true" data-ekey="{id}-cover2" onblur="saveScEdit(this,this.dataset.ekey)">{e(l2)}</div>'
        '</div>'
        '<span class="sf-hint">每行 5-7 字，口语押韵，点击可直接编辑</span>'
        '</div>'
    )

def make_card(s):
    idx = s['id']
    tags_html = ''
    for t in s['type_tags']:
        tags_html += f'<span class="stag t-type">{e(t)}</span>'
    for t in s['field_tags']:
        tags_html += f'<span class="stag t-field">{e(t)}</span>'
    for t in s['theme_tags']:
        tags_html += f'<span class="stag t-theme">{e(t)}</span>'
    tags_html += f'<span class="stag t-prio">{e(s["priority"])}</span>'
    for t in s['lang_nail']:
        tags_html += f'<span class="stag t-lang">💬 {e(t)}</span>'

    body = (
        sf(idx,'type','🎬 拍摄类型',s['shoot_type']) +
        sf(idx,'dur','⏱ 预计时长',s['duration']) +
        sf(idx,'scene','🏠 建议场景 / 置景',s['scene'],big=True) +
        sf(idx,'emo','🎭 IP 情绪建议',s['emotion'],big=True) +
        sf(idx,'field','✨ 磁场主题',s['field_topic']) +
        sf(idx,'theme','📌 拍摄主题',s['shoot_topic']) +
        sf(idx,'curve','📈 情绪曲线',s['curve']) +
        sf(idx,'hook','🎣 开篇钩子',s['hook'],big=True) +
        sf(idx,'script','📝 内容脚本',s['script'],big=True) +
        sf(idx,'ending','🏁 结尾 / 语言钉',s['ending'],big=True) +
        cover_row(idx,s['cover_l1'],s['cover_l2']) +
        sf(idx,'ig','📱 IG 配文',s['ig_caption'],big=True)
    )

    return f"""<div class="sc-card" id="sc-{idx}">
  <div class="sc-head" onclick="toggleSC({idx})">
    <div class="sc-title-row">
      <input type="checkbox" class="sc-check" id="chk-{idx}" onclick="markFilmed(event,{idx})">
      <span class="sc-num">#{idx:02d}</span>
      <span class="sc-title">{e(s['title'])}</span>
      <span class="sc-arrow" id="arr-{idx}">▼</span>
    </div>
    <div class="sc-tags">{tags_html}</div>
  </div>
  <div class="sc-body" id="sb-{idx}" style="display:none">
    {body}
  </div>
</div>"""

def make_tab2():
    cards = '\n'.join(make_card(s) for s in SCRIPTS)
    return f"""<!-- ========== TAB 2: SCRIPTS ========== -->
<div id="tab-posts" class="section">
  <div class="page-top">
    <div class="sec-lbl">📝 拍摄脚本库</div>
    <div class="sc-prog-bar-wrap">
      <div class="sc-prog-bar"><div class="sc-prog-fill" id="sc-prog-fill" style="width:0%"></div></div>
      <span class="sc-prog-txt" id="sc-prog-txt">0/30 已拍摄</span>
    </div>
    {cards}
    <div class="page-bottom"></div>
  </div>
</div>
"""

# ─── Read & patch ─────────────────────────────────────────────────
with open(FILE,'r',encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS before </style>
content = content.replace('</style>', NEW_CSS + '\n</style>', 1)

# 2. Add JS before window.addEventListener('DOMContentLoaded'
content = content.replace(
    "window.addEventListener('DOMContentLoaded'",
    NEW_JS + "\nwindow.addEventListener('DOMContentLoaded'",
    1
)

# 3. Also add restoreSC() call inside DOMContentLoaded
content = content.replace(
    'renderFieldButtons();',
    'restoreSC();\n  renderFieldButtons();',
    1
)

# 4. Replace TAB 2 block
import re
tab2_pattern = re.compile(
    r'<!-- ={5,} TAB 2: POSTS ={5,} -->.*?</div>\s*\n(?=\s*<!-- ={5,} TAB 3)',
    re.DOTALL
)
new_tab2 = make_tab2()
content, n = tab2_pattern.subn(new_tab2, content)
if n == 0:
    print("WARNING: TAB 2 pattern not matched, trying fallback")
    # Fallback: find by unique line markers
    start_marker = '<!-- ========== TAB 2: POSTS ========== -->'
    end_marker = '<!-- ========== TAB 3: TOPICS ========== -->'
    s_idx = content.find(start_marker)
    e_idx = content.find(end_marker)
    if s_idx >= 0 and e_idx >= 0:
        content = content[:s_idx] + new_tab2 + '\n' + content[e_idx:]
        print("Fallback replacement OK")
    else:
        print("ERROR: Could not find TAB 2 block")
else:
    print(f"TAB 2 replaced (regex, {n} match)")

with open(FILE,'w',encoding='utf-8') as f:
    f.write(content)

print(f"Done. File size: {len(content)} chars, lines: {content.count(chr(10))}")
