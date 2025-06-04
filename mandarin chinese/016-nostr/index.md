# NOSTR

![](figure-044-nostr.png)

## NOSTR 及通过中继器传输的其他内容

>*你可以通过立法来反对它，但是言论自由，甚至比隐私更为重要，是开放社会的基础；我们寻求完全不限制任何言论。*

~ Eric Hughes, The Cypherpunk's manifesto, 1993

## 什么是NOSTR

>*TL;DR: nostr 是一种协议，它有能力取代 twitter、Telegram 和其他东西。*

~ @dergigi 

>*nostr 对于通信自由的意义
正如比特币对于交易自由的意义。*

~ Keysa @SimplestBitcoinBook

* **Nostr 是一个简单、去中心化的协议，用于实现
抗审查、全球化、可互操作的网络。**
* Nostr 不依赖于受信任的中心服务器。
* 它是自由和开源 (FOSS) 软件协议，
就像比特币、HTTP 或 TCP-IP 一样，它允许任何人
在 nostr 的基础上进行构建。
* **这是我们保持与拥有互联网连接的任何人、任何地点进行通信自由的方式**。

>*(它) 是一种具有
自主身份层的通信协议......
而且 nostr 远不止于此。* 

~ @dergigi

---

## 为什么我们需要NOSTR

我们需要 nostr，因为当前的通信
系统和社交媒体平台是中心化的。

**这存在问题，因为这些系统：**

* 有权审查你的言论。
* 容易受到国家监管的攻击。
* 可以选择，或被告知，暂停或删除你的
账户。
* 可能被黑客攻击，从而泄露你的数据。
* 使用算法向你推送他们想让你看到的
信息。
* 操纵你在它们上面的每一个体验方面。
* 跟踪你的所有活动。
* 收集和出售你的数据。
* 使用你的数据来在你的信息流中充斥广告。

---

## NOSTR如何工作

* **Nostr 有两个部分：** 客户端和中继器。
* **客户端是一个界面**（应用或网站），它运行
在 nostr 协议上。
* **在这里，你可以看到你和关注的人发布的笔记**（就像 twitter 是一个
界面，你可以在这里发布和阅读其他人的笔记一样，
除了 twitter 是中心化的，而且会审查帖子）。
* **中继器是一个服务器和一个数据库。** 任何人都可以
运行中继器，这使得 nostr 成为去中心化的。
* **它是你的笔记被发送、存储和检索的地方，**
由客户端进行。
* 有很多中继器，你可以选择连接到哪些。有些是免费的，有些是付费的。
* 当你发布消息时，它会被广播到你连接的中继器。
* 客户端查询它们连接的中继器，
然后它们会填充由
这些中继器托管的消息。

![publish](figure-045-publish.png)

~ @BTCillustrated

---

>*任何人都可以运行中继器。中继器非常简单和
愚蠢。除了接受一些人的帖子
并转发给其他人之外，它什么也不做。
中继器不需要被信任。
签名在客户端验证。*

~ @fiatjaf, 2019-11-02 fiatjaf.com/nostr.html

* 当你打开你的 nostr 客户端时，你将会看到所有由你和你关注的人发布的
笔记，按时间顺序排列。
* 没有**算法**决定要向你展示什么，
从你那里隐藏什么，或者审查你的帖子。
* 像比特币一样，**nostr 使用公钥/私钥对。**
* **公钥** = npub，就像一个用户名
* **私钥** = nsec，就像一个密码

>* **注意：** 你的私钥如果
>丢失，则无法重置，所以你**必须妥善保管！**
>* 如果你泄露了你的私钥，那么任何拥有
>访问权限的人都可以访问你的 nostr
>账户，并且**没有办法重新获得
>唯一访问权限。**

---

* 你可以使用
NIP-05 创建一个人类可读的用户名。**例如：**
* **我的公钥，或 npub 是：**
<small>npub1dpna3xwwddnhhzg9ycpvlcz2ze0jdwm2rf3eqd2lf9leaewtq7tqhw0ef2</small>

* **我的 NIP-05 Nostr 地址是：**

SimplestBitcoinBook@nostrplebs.com

* **你可以在 nostr 上搜索人员，** 通过输入他们的：
*  npub
*  NIP-05（又名 nostr 地址），如果他们有的话
*  来自 NIP-05 的用户名 -> @SimplestBitcoinBook

* **在这里获取 NIP-05 标识符：**
* nostrplebs.com
* verified-nostr.com
* getalby.com
* 或者使用你自己的域名设置一个

* 一旦你有了你的 nostr 密钥对，你可以使用相同的密钥登录到任何
nostr 客户端，你会看到你
**在所有客户端上保留你的身份和关注者/被关注者列表。**
* 这与传统的社交媒体不同，在传统的社交媒体中，你需要为每个平台单独的账户、用户名和密码，
并且你在每个平台上都有不同的内容、关注和被关注者。
>*在最基本的层面上，Nostr 是一种通信
协议，它充当将你所有应用绑定在一起的社交粘合剂。*

~ derekross@nostrplebs.com

---

# 如何使用NOSTR

>1. **选择一个客户端**应用程序来下载。（选择哪个客户端并不重要，因为一旦你生成了密钥对，就可以尝试所有客户端。）
>2. **流行的客户端示例：**
>* Damus on iOS
>* Amethyst on Android
>* Primal on iOS/Android/Desktop
>3. **创建一个用户名。** 不需要其他信息。
>4. **应用程序将生成该帐户。**
>5. **你可以添加个人资料图片和横幅**，如果你喜欢的话。
>6. **一旦你至少选择一个兴趣（例如：比特币、艺术、人权、体育、音乐等），你的帐户将自动连接到几个
中继器。**
>7. 根据客户端的不同，它会自动关注一些具有相似兴趣的帐户，或者让你选择几个。
>8. **然后你可以添加或删除中继器和帐户。**

![create account on nostr](figure-046-create%20account%20on%20nostr%20.png)

~ @BTCillustrated

---

## 密钥管理
* 一旦你的密钥生成，就该
安装一个**签名扩展程序**了。
* 当你想登录到在
nostr 协议上运行的网站时，它会要求你提供 nsec 或私钥。
* **不要**直接输入它，因为网站可能会泄露数据。
* **相反，始终使用签名扩展程序。**
* 这是一个存储你的私钥的工具，并且你授权它代表你签署事件，例如笔记。
别担心，这比听起来简单！
* **流行的签名扩展程序：**
* Nostore (iOS Safari)
* Amber (Android)
* Nsec App (Mobile/Desktop)
* Alby (Desktop)
* Nos2X (Desktop)
* Nostr Connect (Desktop)

## ZAPS
* Zapping 是我们在 nostr 上使用比特币的方式！创建一个 V4V
（Value4Value）经济，一条一条地，一次一次地 zap。
* 你可以通过将比特币
闪电网络钱包连接到你的 nostr 帐户，为你欣赏的笔记或
内容发送和接收 sats（又名 zaps）。
* 有多种方法可以做到这一点。如果你的
选择的客户端没有引导你完成此过程，只需在 nostr
上使用 #asknostr 标签提问，就会有人指导你。
Nostriches 是友好的。

---

## NOSTR 资源
以下是一个网站列表，其中包含关于 nostr 及其奇迹的
优秀、易于理解的指南！

*  nostr-resources.com by @derGigi
* nostr.com by @fiatjaf
* nostr.net by @aljaz
* nostr.how by @JeffG
* usenostr.org by @pluja
* benwehrman.com/nostr-guide by @benwehrman
* nostrapps.com by @Karnage

## 为什么是鸵鸟？

![ostrich](figure-047-ostrich.png)

**Nostrich 的起源故事**

by Walker@primal.net

**2022 年 12 月 16 日：**

我发现了 ChatGPT3，并且
自然地问它
“你能写一个关于 #nostr 的笑话吗？”
ChatGPT3 回应说：
问：你如何称呼一个爱管闲事的鸵鸟？
答：一个 nosTrich！
这个笑话不是很好，但是你不能责怪一个机器人。无论如何，我
喜欢为 nostr 提供视觉标识的想法，而且鸵鸟是
很酷的鸟类。所以我去了 Midjourney 并创建了 The #Nostrich

**2022 年 12 月 20 日：**

@jb55 提议将“Nostrich”作为官方的 Nostr 吉祥物
和标志。
三分钟后，@jack 发推了 Nostrich 图像。
正如他们所说，剩下的就是历史了。

~ @Walker

---

## NOSTR 客户端/应用

访问 **nostrapps.com** 来找到这些，以及更多
建立在免费、开源 nostr 协议之上的惊人应用程序。
使用你的签名扩展程序登录所有这些应用程序！

* **Nostr Nests** - 用于聊天、即兴演奏、
微型会议、现场播客的音频空间。
* **Plebian Market** - 互联网上自主的主权市场，由比特币和闪电网络提供支持。
* **Npub.pro** - 为自己创建一个基于 nostr 的网站。
* **Corny Chat** - 实时音频空间。
* **Wavlake** - 一个音乐流媒体平台，它利用比特币的闪电网络来提供价值。
* **Zap.stream** - 托管你的直播并获得 sat zaps。
* **Flare** - 一个用于查看、上传和交互
视频内容的客户端。
* **Blowater** - 旨在取代 Telegram/Slack/Discord。
* **Stemstr** - 一个供音乐艺术家
联系、协作和分享精彩音乐的社交体验。
* **Nostr.build** - 图像、视频和媒体上传器和主机。
* Hivetalk - 实时、完全私密的视频通话和
会议，取代 Zoom。
* **Zap.cooking** - 通过 Nostr 分享食谱。
* **Flockstr** - 活动和聚会安排。
* **Memestr** - 通过 Nostr 查看和制作模因
* **Quotestr** - 使 Nostr 笔记成为图像引用。

---

## 加入我们
* Nostr 仍然非常年轻。就像比特币一样，但更
年轻，它是一个草根的、混乱的、全球的、自下而上的
实验。
* 如果你看到了去中心化、抗审查、开源通信协议的价值，
请加入我们，使用它、开发它、向开发人员提供
反馈，并以你认为被召唤的任何
方式参与，以帮助发展这个言论自由工具。
* 参与一项旨在维护全球言论自由和开放通信的成长型技术，这是一种了不起的体验。
* 投入其中，与我们其余的主权
灵魂一起学习，拥抱内在的混乱，创造美丽，
并为我们的孙辈创造一个光明的未来！

*比所有这些更重要的是，我们必须记住，nostr 仅仅是非常松散的一组服务器，它们之间基本上没有任何
连接，...并且保持与他人联系和查找内容的过程
必须通过许多不同的临时尝试来解决。要编写 Nostr 应用程序和使用 Nostr，
必须拥抱内在的混乱。*

*~ @fiatjaf 来自：*

*'Nostr 中用于基本社交网络的内容发现和中继使用的愿景'*

---

向中本聪、Fiatjaf、过去、现在和未来的密码朋克、Nostr fam、BT 漩涡、有毒的最大主义者、
无毒的最大主义者、模因之王和女士们、信徒、犬儒主义者、先知......
以及始终，
我挚爱的家人、朋友，
以及那位呼吸贯穿我们所有人的那一位，
感谢他/她始终看顾着我，
比任何事物都更珍贵，甚至比特币

本书的免费 PDF 和翻译
可在以下网址获取：thesimplestbitcoinbook.net

![c1](figure-048-c1.png)

在 nostr 上关注我：

![c2](figure-049-c2.jpg)

评论、问题、更新、反馈：

thesimplestbitcoinbook@proton.me

不能保证我会及时回复 ...

可能赤脚在某座山上

Stack sats

Stay strong

Stay true

in the end, Love

851522
