# NOSTR

![](figure-044-nostr.png)

## NOSTR & AWỌN OHUN MIIRAN TI A FI ṢỌ ỌNÀ RELAYS

>*Ẹnikan le ṣe awọn ofin lodi si i, ṣugbọn ominira
ọrọ, paapaa ju asiri lọ, jẹ pataki si
awujọ ti o ṣii; a ko wa lati ni ihamọ eyikeyi ọrọ rara.*

~ Eric Hughes, Ifihan Cypherpunk, 1993

## KINI NOSTR

>*TL;DR: nostr jẹ ilana ti o ni agbara lati
rọpo twitter, Telegram, ati awọn nkan miiran.*

~ @dergigi

>*nostr jẹ si ominira ibaraẹnisọrọ
bi bitcoin ṣe jẹ si ominira ti idunadura.*

~ Keysa @SimplestBitcoinBook

* **Nostr jẹ ilana ti o rọrun, ti a pin kaakiri fun
sooro-censorship, kariaye, awọn nẹtiwọọki interoperable.**
* Nostr ko gbẹkẹle olupin aarin ti o gbẹkẹle.
* O jẹ sọfitiwia ọfẹ ati orisun ṣiṣi (FOSS) ilana,
bii Bitcoin, HTTP tabi TCP-IP, eyiti o fun ẹnikẹni laaye lati
kọ lori nostr.
* **O jẹ bii a ṣe n ṣetọju ominira wa lati sọrọ**
pẹlu ẹnikẹni, nibikibi pẹlu asopọ intanẹẹti kan.

>*(o jẹ) ilana ibaraẹnisọrọ pẹlu
ipele idanimọ ti ara ẹni...
ati nostr tun ju iyẹn lọ.*

~ @dergigi

---

## IDI TI A FI NI LATI NI NOSTR

A nilo nostr nitori ibaraẹnisọrọ lọwọlọwọ
awọn eto ati awọn iru ẹrọ media awujọ jẹ aarin.

**Eyi jẹ iṣoro nitori awọn eto wọnyi:**

* Ni agbara lati ṣe atunyẹwo ọrọ rẹ.
* Ṣe ipalara si awọn ikọlu ilana nipasẹ ipinlẹ.
* Le yan, tabi sọ fun, lati daduro tabi paarẹ rẹ
akọọlẹ.
* Le jẹ gige, ati nitorinaa ba data rẹ jẹ.
* Lo awọn algoridimu lati fun ọ ni alaye ti wọn fẹ
o lati rii.
* Ṣe afọwọyi gbogbo abala iriri rẹ lori wọn.
* Tọpinpin gbogbo iṣẹ rẹ.
* Ikore ati ta data rẹ.
* Lo data rẹ lati sọ kikọ sii rẹ di idoti pẹlu awọn ipolowo.

---

## BAWO NI ỌJỌ NOSTR ṢE ṢIṢẸ

* **Nostr ni awọn apakan meji:** Awọn alabara ati Awọn relays.
* **ALABARA jẹ INTERFACE** (app tabi oju opo wẹẹbu) ti o ṣiṣẹ
lori ilana nostr.
* **O jẹ ibiti o ti rii awọn akọsilẹ** ti iwọ ati awọn eniyan
o tẹle ifiweranṣẹ (ni ọna kanna ti twitter jẹ
ni wiwo nibiti o ti fiweranṣẹ ati ka awọn akọsilẹ nipasẹ awọn miiran,
ayafi ti twitter jẹ aarin & o ṣe atunyẹwo awọn ifiweranṣẹ.)
* **RELAY jẹ SERVER ati DATABASE.** Ẹnikẹni le
ṣiṣe relay kan, eyiti o jẹ ki nostr jẹ ipinya.
* **t jẹ ibiti awọn akọsilẹ rẹ ti firanṣẹ, ti o fipamọ ati gba pada
lati** nipasẹ awọn alabara.
* Ọpọlọpọ awọn relays ati pe o le yan eyi ti o
lati sopọ si. Diẹ ninu jẹ ọfẹ ati diẹ ninu sanwo.
* Nigbati o ba fi ifiranṣẹ ranṣẹ, o tan kaakiri si awọn relays
o ti sopọ si.
* Awọn alabara beere awọn relays ti wọn ti sopọ si, ati
lẹhinna wọn kun awọn ifiranṣẹ ti o gbalejo nipasẹ
awọn relays yẹn.

![publish](figure-045-publish.png)

~ @BTCillustrated

---

>*Ẹnikẹni le ṣiṣẹ relay kan. Relay kan rọrun pupọ ati
odiotu. Ko ṣe ohunkohun yatọ si gbigba awọn ifiweranṣẹ
lati ọdọ diẹ ninu awọn eniyan ati fifiranṣẹ si awọn miiran.
Awọn relays ko ni lati gbẹkẹle.
Awọn ibuwọlu jẹrisi ni ẹgbẹ alabara.*

~ @fiatjaf, 2019-11-02 fiatjaf.com/nostr.html

* Nigbati o ba ṣii alabara nostr rẹ, iwọ yoo rii gbogbo awọn
awọn akọsilẹ ti o fiweranṣẹ nipasẹ iwọ ati awọn ti o tẹle ni
iseese ọna.
* Ko si awọn **algoridimu** ti n pinnu ohun lati fi han ọ,
kini lati da duro lati ọdọ rẹ, tabi ṣe atunyẹwo awọn ifiweranṣẹ rẹ.
* Bii Bitcoin, **nostr nlo awọn orisii bọtini gbangba/ikọkọ.**
* **Bọtini gbangba** = npub, bii orukọ olumulo
* **Bọtini ikọkọ** = nsec, bii ọrọ igbaniwọle

>* **AKIYESI:** Bọtini ikọkọ rẹ ko le tunto ti o ba jẹ
>sọnu, nitorinaa o **gbọdọ ni aabo daradara!**
>* Ti o ba jo bọtini ikọkọ rẹ, ẹnikẹni ti o ni
>wiwọle si o ni wiwọle si nostr rẹ
>akọọlẹ, ati **ko si ọna lati tun bọsipọ
>wiwọle nikan.**

---

* O le ṣẹda orukọ olumulo ti o le ka eniyan nipa lilo
NIP-05. **Fun apẹẹrẹ:**
* **Bọtini Gbangba mi, tabi npub jẹ:**
<small>npub1dpna3xwwddnhhzg9ycpvlcz2ze0jdwm2rf3eqd2lf9leaewtq7tqhw0ef2</small>

* **Adirẹsi Nostr NIP-05 mi ni:**

SimplestBitcoinBook@nostrplebs.com

* **O le wa awọn eniyan lori nostr** nipa titẹ wọn:
* npub
* NIP-05 (aka adirẹsi nostr) ti wọn ba ni ọkan
* Orukọ olumulo lati NIP-05 -> @SimplestBitcoinBook

* **Gba Idanimọ NIP-05 nibi:**
* nostrplebs.com
* verified-nostr.com
* getalby.com
* Tabi ṣeto ọkan pẹlu ašẹ tirẹ

* Ni kete ti o ba ni orisii bọtini nostr rẹ, o le wọle si eyikeyi
alabara nostr pẹlu awọn bọtini kanna, ati pe iwọ yoo rii iyẹn
o **da idanimọ rẹ duro ati atokọ awọn ọmọlẹyin/atẹle
lori gbogbo awọn alabara.**
* Eyi yatọ si media awujọ Legacy, nibiti o nilo a
akọọlẹ lọtọ, orukọ olumulo ati ọrọ igbaniwọle fun ọkọọkan
Syeed, ati pe o ni akoonu ti o yatọ, tẹle ati
awọn ọmọlẹyin lori ọkọọkan.
>*Ni ipele ipilẹ julọ rẹ, Nostr jẹ ibaraẹnisọrọ
ilana ti o ṣe bi lẹ pọ awujọ ti o so
gbogbo awọn ohun elo rẹ papọ.*

~ derekross@nostrplebs.com

---

# BAWO NI A ṢE LATI NOSTR

>1. **Yan ohun elo alabara kan** lati ṣe igbasilẹ. (Ko ṣe pataki
eyi ti o yan, bi o ṣe le gbiyanju gbogbo wọn ni kete ti
o ni orisii bọtini rẹ ti ipilẹṣẹ.)
>2. **Awọn apẹẹrẹ Onibara olokiki:**
>* Damus lori iOS
>* Amethyst lori Android
>* Primal lori iOS/Android/Desktop
>3. **Ṣẹda Orukọ Olumulo.** Ko si alaye miiran ti o nilo.
>4. **Ohun elo naa yoo ṣe ipilẹṣẹ akọọlẹ naa.**
>5. **O le ṣafikun aworan profaili ati asia** ti o ba fẹ.
>6. **Akọọlẹ rẹ yoo sopọ laifọwọyi si diẹ
relays** ni kete ti o ba yan o kere ju anfani kan (fun apẹẹrẹ:
bitcoin, aworan, awọn ẹtọ eniyan, awọn ere idaraya, orin ati be be lo)
>7. Ti o da lori alabara, yoo tẹle laifọwọyi a
diẹ awọn akọọlẹ pẹlu iru iwulo kan, tabi jẹ ki o yan a
diẹ.
>8. **O le lẹhinna ṣafikun tabi yọ awọn relays ati awọn akọọlẹ kuro.**

![create account on nostr](figure-046-create%20account%20on%20nostr%20.png)

~ @BTCillustrated

---

## IṢAKOSO BỌTINI
* Ni kete ti awọn bọtini rẹ ti ipilẹṣẹ, o to akoko lati
fi sori ẹrọ **afikun ibuwọlu.**
* Nigbati o ba fẹ wọle si oju opo wẹẹbu kan ti o nṣiṣẹ lori
nostr ilana, yoo beere fun nsec rẹ, tabi bọtini ikọkọ.
* **MAA ṢE** tẹ sii taara, bi awọn oju opo wẹẹbu ṣe le jo data
* **Dipo, lo afikun ibuwọlu nigbagbogbo.**
* Eyi jẹ ohun elo ti o tọju bọtini ikọkọ rẹ, ati iwọ
fun ni aṣẹ lati fowo si awọn iṣẹlẹ, gẹgẹbi awọn akọsilẹ, lori rẹ
dipo. Maṣe yọ ara rẹ lẹnu, eyi rọrun ju bi o ti dun lọ!
* **Awọn afikun ibuwọlu olokiki:**
* Nostore (iOS Safari)
* Amber (Android)
* Nsec App (Mobile/Desktop)
* Alby (Desktop)
* Nos2X (Desktop)
* Nostr Connect (Desktop)

## ZAPS
* Zapping ni bii a ṣe bitcoin lori nostr! Ṣiṣẹda V4V
(Iye4Iye) aje, akọsilẹ nipasẹ akọsilẹ, zap nipasẹ zap.
* O le firanṣẹ ati gba awọn sats (aka zaps) fun awọn akọsilẹ tabi
akoonu ti o ni riri nipa sisopọ Bitcoin kan
Apamọwọ Lightning si akọọlẹ nostr rẹ.
* Ọpọlọpọ awọn ọna lo wa lati ṣe eyi. Ti alabara rẹ ba
yan ko rin ọ nipasẹ rẹ, kan beere lori nostr
pẹlu tag #asknostr, ati pe ẹnikan yoo ṣe itọsọna fun ọ.
Awọn Nostriches jẹ ore

---

## Awọn orisun NOSTR
Ni isalẹ ni atokọ ti awọn oju opo wẹẹbu ti o ni o tayọ, ni irọrun
awọn itọsọna ti o ṣeeṣe lori nostr ati awọn iyalẹnu rẹ!

* nostr-resources.com nipasẹ @derGigi
* nostr.com nipasẹ @fiatjaf
* nostr.net nipasẹ @aljaz
* nostr.how nipasẹ @JeffG
* usenostr.org nipasẹ @pluja
* benwehrman.com/nostr-guide nipasẹ @benwehrman
* nostrapps.com nipasẹ @Karnage

## KINI IDI TI ẸYẸ AWỌN?

![ostrich](figure-047-ostrich.png)

**Ìtàn Orísun Nostrich**

nipasẹ Walker@primal.net

**December 16, 2022:**

Mo ṣe awari ChatGPT3 ati,
nipa ti ara, beere lọwọ rẹ
“Ṣe o le kọ awada kan nipa #nostr?”
ChatGPT3 dahun pe:
Ibeere: Kini o pe ni ostrich ti o ni imọlara?
A: A nosTrich!
Awon ko tobi pupo, sugbon o ko le da bot kan lebi. Laibikita, Emi
nifẹ imọran ti idanimọ wiwo fun nostr, ati awọn ostriches jẹ
awọn ẹiyẹ itura. Nitorinaa Mo lọ si Midjourney ati ṣẹda #Nostrich

**December 20, 2022:**

@jb55 daba “Nostrich” gẹgẹbi mascot Nostr osise
ati aami.
Iṣẹju mẹta lẹhinna, @jack tweets aworan Nostrich.
Iyokù, bi wọn ti sọ, jẹ itan-akọọlẹ.

~ @Walker

---

## Awọn alabara/APPLIKASI NOSTR

Ṣabẹwo si **nostrapps.com** lati wa awọn wọnyi, ati ọpọlọpọ diẹ sii
awọn ohun elo iyalẹnu ti a kọ sori ọfẹ, orisun ṣiṣi nostr protocol.
Lo afikun ibuwọlu rẹ lati wọle si gbogbo wọn!

* **Awọn itẹ-ẹiyẹ Nostr** - Aaye ohun afetigbọ fun iwiregbe, jamming,
awọn apejọ kekere, awọn adarọ ese laaye.
* **Ọja Plebian** - Ọja ti ara ẹni ti o jẹ ti ara ẹni ti
Intanẹẹti, ti agbara nipasẹ Bitcoin & Lightning.
* **Npub.pro** - Ṣe ara rẹ ni oju opo wẹẹbu ti o da lori nostr.
* **Iwiregbe Corny** - Awọn aaye ohun afetigbọ laaye.
* **Wavlake** - Syeed ṣiṣan orin ti o nlo
Nẹtiwọọki Lightning Bitcoin lati pese iye fun iye.
* **Zap.stream** - Gbalejo ṣiṣan laaye rẹ ki o gba awọn zaps sat.
* **Flare** - Onibara fun wiwo, ikojọpọ, ati ibaraenisepo
pẹlu akoonu fidio.
* **Blowater** - Ti a ṣe lati rọpo Telegram/Slack/Discord.
* **Stemstr** - Iriri awujọ fun awọn oṣere orin si
sopọ, ṣe ifowosowopo ati pin orin iyalẹnu.
* **Nostr.build** - Aworan, fidio & ikojọpọ media & ogun.
* Hivetalk - Ni akoko gidi, awọn ipe fidio ni ikọkọ patapata ati
awọn ipade, rọpo Sun-un.
* **Zap.cooking** - Pin awọn ilana lori Nostr.
* **Flockstr** - Awọn iṣẹlẹ ati iṣeto ipade.
* **Memestr** - Wo ki o ṣe awọn memes lori Nostr
* **Quotestr** - Ṣe akọsilẹ Nostr kan agbasọ aworan.

---

## DA RU MO WA
* Nostr tun jẹ ọdọ pupọ. Gẹgẹ bi bitcoin, ṣugbọn pupọ
ọdọ, o jẹ gbongbo, idoti, agbaye, ilẹ-soke
idasile.
* Ti o ba rii iye ni ti a pin kaakiri, censorship-
sooro, ilana ibaraẹnisọrọ orisun ṣiṣi,
jọwọ darapọ mọ wa ni lilo rẹ, idagbasoke rẹ, fifunni
esi si awọn devs, ati kopa ninu ohunkohun
ọna ti o rilara pe a pe ọ, lati ṣe iranlọwọ lati dagba irinṣẹ ọrọ ọfẹ yii.
* O jẹ iriri iyalẹnu lati ṣe alabapin ninu idagba
imọ-ẹrọ ti a kọ lati ṣetọju ominira ọrọ sisọ
ati ṣiṣi ibaraẹnisọrọ ni kariaye.
* Bọ sinu ki o kọ ẹkọ pẹlu iyoku wa ọba
awọn ẹmi, ti o n gba rudurudu abimọ lati ṣẹda ẹwa,
ati lati kọ ojo iwaju didan fun awọn ọmọ-ọmọ wa!

*O ṣe pataki ju gbogbo rẹ lọ pe a gbọdọ ranti pe
nostr jẹ eto awọn olupin ti o loose pupọ pẹlu pataki ko si
asopọ laarin wọn, ... ati ilana ti titọju
ti sopọ mọ awọn miiran ati wiwa akoonu gbọdọ jẹ
ṣe itọsọna nipasẹ ọpọlọpọ awọn igbiyanju hakkiish oriṣiriṣi. Lati
kọ awọn ohun elo Nostr ati lati lo Nostr ọkan
gbọdọ gba rudurudu abimọ.*

*~ @fiatjaf lati:*

*'Iran kan fun wiwa akoonu ati lilo relay
fun ipilẹ awujọ-nẹtiwọọki ni Nostr'*

---

Oore-ọfẹ nla fun Satoshi, Fiatjaf, awọn cypherpunks
ti o ti kọja, lọwọlọwọ ati ọjọ iwaju, Nostr fam, BT vortex, awọn
maixi majele, awọn maxis ti kii ṣe majele, awọn meme-lords ati -
awọn obinrin, awọn onigbagbọ, awọn alaroye, awọn oluran...
ati nigbagbogbo,
idile mi olufẹ, awọn ọrẹ,
ati Ẹnikan ti o nmi nipasẹ gbogbo wa,
fun ri mi nigbagbogbo nipasẹ,
iyebiye ju ohunkohun lọ, paapaa bitcoin

Ọfẹ PDF ti iwe yii ati awọn itumọ
wa ni: thesimplestbitcoinbook.net

![c1](figure-048-c1.png)

Tẹle mi lori nostr:

![c2](figure-049-c2.jpg)

Awọn asọye, awọn ibeere, awọn imudojuiwọn, esi:

thesimplestbitcoinbook@proton.me

Ko le ṣe ileri pe Emi yoo de ọdọ rẹ ni akoko ti akoko ...

le jẹ ẹsẹ lasan lori oke kan ni ibikan

Stack sats

Duro lagbara

Duro otitọ

ni opin, Ife

851522
