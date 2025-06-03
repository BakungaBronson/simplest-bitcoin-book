# NOSTR

![](figure-044-nostr.png)

## NOSTR & AUTRES CHOSES TRANSMISES PAR DES RELAIS

>*On pourrait promulguer des lois contre cela, mais la liberté
d'expression, encore plus que la vie privée, est fondamentale pour une
société ouverte ; nous ne cherchons absolument pas à restreindre l'expression.*

~ Eric Hughes, Le manifeste du Cypherpunk, 1993

## QU'EST-CE QUE NOSTR

>*TL;DR : nostr est un protocole qui a le pouvoir de
remplacer twitter, Telegram et autres.*

~ @dergigi

>*nostr est à la liberté de communication
ce que bitcoin est à la liberté de transaction.*

~ Keysa @SimplestBitcoinBook

* **Nostr est un protocole simple et décentralisé pour des
réseaux mondiaux, interopérables et résistants à la censure.**
* Nostr ne repose pas sur un serveur central de confiance.
* Il s'agit d'un protocole logiciel libre et open source (FOSS),
comme Bitcoin, HTTP ou TCP-IP, qui permet à quiconque de
construire sur nostr.
* **C'est ainsi que nous conservons notre liberté de communiquer**
avec n'importe qui, n'importe où avec une connexion internet.

>*(c'est) un protocole de communication avec une
couche d'identité auto-souveraine...
et nostr est aussi plus que cela.*

~ @dergigi

---

## POURQUOI AVONS-NOUS BESOIN DE NOSTR

Nous avons besoin de nostr car les systèmes de communication
actuels et les plateformes de médias sociaux sont centralisés.

**C'est problématique car ces systèmes :**

* Ont le pouvoir de censurer votre discours.
* Sont vulnérables aux attaques réglementaires de l'État.
* Peuvent choisir, ou être informés, de suspendre ou de supprimer votre
compte.
* Peuvent être piratés, compromettant ainsi vos données.
* Utilisent des algorithmes pour vous fournir les informations qu'ils veulent
que vous voyiez.
* Manipulent chaque aspect de votre expérience sur ceux-ci.
* Suivent toute votre activité.
* Collectent et vendent vos données.
* Utilisent vos données pour joncher votre flux de publicités.

---

## COMMENT FONCTIONNE NOSTR

* **Nostr a deux parties :** Clients et Relais.
* **Un CLIENT est une INTERFACE** (application ou site web) qui est exécutée
sur le protocole nostr.
* **C'est là que vous voyez les notes** que vous et les personnes
que vous suivez postez (de la même manière que twitter est une
interface où vous postez et lisez les notes des autres,
sauf que twitter est centralisé et censure les messages).
* **Un RELAIS est un SERVEUR et une BASE DE DONNÉES.** N'importe qui peut
exécuter un relais, ce qui rend nostr décentralisé.
* **C'est là que vos notes sont envoyées, stockées et récupérées
par** les clients.
* Il existe de nombreux relais et vous pouvez choisir auxquels
vous connecter. Certains sont gratuits et d'autres sont payants.
* Lorsque vous postez un message, il est diffusé aux relais
auxquels vous êtes connecté.
* Les clients interrogent les relais auxquels ils sont connectés, et
ensuite ils remplissent les messages hébergés par
ces relais.

![publish](figure-045-publish.png)

~ @BTCillustrated

---

>*N'importe qui peut exécuter un relais. Un relais est très simple et
idiot. Il ne fait rien d'autre qu'accepter les messages
de certaines personnes et les transmettre à d'autres.
Les relais n'ont pas besoin d'être de confiance.
Les signatures sont vérifiées côté client.*

~ @fiatjaf, 2019-11-02 fiatjaf.com/nostr.html

* Lorsque vous ouvrez votre client nostr, vous verrez toutes les
notes postées par vous et ceux que vous suivez dans
l'ordre chronologique.
* Il n'y a pas d'**algorithmes** qui décident de ce qu'il faut vous montrer,
de ce qu'il faut vous cacher ou de la censure de vos messages.
* Comme Bitcoin, **nostr utilise des paires de clés publiques/privées.**
* **CLÉ PUBLIQUE** = npub, comme un nom d'utilisateur
* **CLÉ PRIVÉE** = nsec, comme un mot de passe

>* **NOTE :** Votre clé privée ne peut pas être réinitialisée si
>perdue, vous devez donc **bien la sécuriser !**
>* Si vous divulguez votre clé privée, celui qui y a
>accès a accès à votre
>compte nostr, et **il n'y a aucun moyen de
>récupérer l'accès exclusif.**

---

* Vous pouvez créer un nom d'utilisateur lisible par l'homme en utilisant
NIP-05. **Par exemple :**
* **Ma clé publique, ou npub est :**
<small>npub1dpna3xwwddnhhzg9ycpvlcz2ze0jdwm2rf3eqd2lf9leaewtq7tqhw0ef2</small>

* **Mon adresse Nostr NIP-05 est :**

SimplestBitcoinBook@nostrplebs.com

* **Vous pouvez rechercher des personnes sur nostr** en entrant leur :
* npub
* NIP-05 (aka adresse nostr) s'ils en ont une
* Nom d'utilisateur de NIP-05 -> @SimplestBitcoinBook

* **Obtenez un identifiant NIP-05 ici :**
* nostrplebs.com
* verified-nostr.com
* getalby.com
* Ou configurez-en un avec votre propre domaine

* Une fois que vous avez votre paire de clés nostr, vous pouvez vous connecter à n'importe quel
client nostr avec ces mêmes clés, et vous verrez que
vous **conservez votre identité et vos listes de suiveurs/abonnements
sur tous les clients.**
* Cela diffère des médias sociaux hérités, où vous avez besoin d'un
compte, d'un nom d'utilisateur et d'un mot de passe distincts pour chaque
plateforme, et vous avez différents contenus, abonnements et
abonnés sur chacun d'eux.
>*À son niveau le plus élémentaire, Nostr est un protocole de communication
qui agit comme la colle sociale qui lie
toutes vos applications ensemble.*

~ derekross@nostrplebs.com

---

# COMMENT UTILISER NOSTR

>1. **Choisissez une application cliente** à télécharger. (Peu importe
celui que vous sélectionnez, car vous pouvez tous les essayer une fois
que vous avez généré votre paire de clés).
>2. **Exemples de clients populaires :**
>* Damus sur iOS
>* Amethyst sur Android
>* Primal sur iOS/Android/Desktop
>3. **Créez un nom d'utilisateur.** Aucune autre information n'est nécessaire.
>4. **L'application va générer le compte.**
>5. **Vous pouvez ajouter une photo de profil et une bannière** si vous le souhaitez.
>6. **Votre compte se connectera automatiquement à quelques
relais** une fois que vous aurez sélectionné au moins un intérêt (par exemple :
bitcoin, art, droits de l'homme, sports, musique, etc.)
>7. Selon le client, il suivra automatiquement quelques
comptes avec un intérêt similaire, ou vous laissera en sélectionner quelques-uns.
>8. **Vous pouvez ensuite ajouter ou supprimer des relais et des comptes.**

![create account on nostr](figure-046-create%20account%20on%20nostr%20.png)

~ @BTCillustrated

---

## GESTION DES CLÉS
* Une fois que vos clés ont été générées, il est temps d'installer une
**extension de signature.**
* Lorsque vous voulez vous connecter à un site web fonctionnant sur le
protocole nostr, il vous demandera votre nsec, ou clé privée.
* **NE** l'entrez **PAS** directement, car les sites web peuvent divulguer des données.
* **Au lieu de cela, utilisez toujours une extension de signature.**
* Il s'agit d'un outil qui stocke votre clé privée, et vous
l'autorisez à signer des événements, tels que des notes, en votre
nom. Ne vous inquiétez pas, c'est plus simple qu'il n'y paraît !
* **Extensions de signature populaires :**
* Nostore (iOS Safari)
* Amber (Android)
* Nsec App (Mobile/Desktop)
* Alby (Desktop)
* Nos2X (Desktop)
* Nostr Connect (Desktop)

## ZAPS
* Zapper, c'est comme le bitcoin sur nostr ! Créer une économie V4V
(Value4Value), note par note, zap par zap.
* Vous pouvez envoyer et recevoir des sats (alias zaps) pour des notes ou
du contenu que vous appréciez en connectant un portefeuille
Bitcoin Lightning à votre compte nostr.
* Il existe différentes manières de procéder. Si le client que vous
choisissez ne vous guide pas, demandez simplement sur nostr
avec le tag #asknostr, et quelqu'un vous guidera.
Les Nostriches sont amicaux.

---

## RESSOURCES NOSTR
Ci-dessous une liste de sites web qui proposent d'excellents guides facilement
digestes sur nostr et ses merveilles !

* nostr-resources.com par @derGigi
* nostr.com par @fiatjaf
* nostr.net par @aljaz
* nostr.how par @JeffG
* usenostr.org par @pluja
* benwehrman.com/nostr-guide par @benwehrman
* nostrapps.com par @Karnage

## POURQUOI L'AUTRUCHE ?

![ostrich](figure-047-ostrich.png)

**L'histoire de l'origine de Nostrich**

par Walker@primal.net

**16 décembre 2022 :**

J'ai découvert ChatGPT3 et,
naturellement, je lui ai demandé
« Pouvez-vous écrire une blague sur #nostr ? »
ChatGPT3 a répondu :
Q : Comment appelle-t-on une autruche fouineuse ?
R : Une nosTrich !
La blague n'était pas géniale, mais on ne peut pas blâmer un robot. Quoi qu'il en soit, j'ai
adoré l'idée d'une identité visuelle pour nostr, et les autruches sont
des oiseaux cool. Je me suis donc tourné vers Midjourney et j'ai créé The #Nostrich

**20 décembre 2022 :**

@jb55 a proposé le « Nostrich » comme mascotte
et logo officiels de Nostr.
Trois minutes plus tard, @jack tweete l'image de Nostrich.
Le reste, comme on dit, appartient à l'histoire.

~ @Walker

---

## CLIENTS/APPLICATIONS NOSTR

Visitez **nostrapps.com** pour trouver ceux-ci, et bien d'autres
applications étonnantes construites sur le protocole nostr gratuit et open source.
Utilisez votre extension de signature pour vous connecter à tous !

* **Nostr Nests** - Un espace audio pour discuter, jammer,
micro-conférences, podcasts en direct.
* **Plebian Market** - Le marché auto-souverain de
l'Internet, alimenté par Bitcoin & Lightning.
* **Npub.pro** - Créez-vous un site web basé sur nostr.
* **Corny Chat** - Espaces audio en direct.
* **Wavlake** - Une plateforme de streaming musical qui utilise
le réseau Lightning de Bitcoin pour offrir de la valeur pour la valeur.
* **Zap.stream** - Hébergez votre flux en direct et recevez des zaps de sats.
* **Flare** - Un client pour visualiser, télécharger et interagir
avec le contenu vidéo.
* **Blowater** - Conçu pour remplacer Telegram/Slack/Discord.
* **Stemstr** - Une expérience sociale pour les artistes musicaux afin de
se connecter, de collaborer et de partager de la musique incroyable.
* **Nostr.build** - Téléchargeur et hébergeur d'images, de vidéos et de médias.
* Hivetalk - Appels vidéo et
réunions en temps réel, totalement privées, remplace Zoom.
* **Zap.cooking** - Partagez des recettes sur Nostr.
* **Flockstr** - Événements et planification de rencontres.
* **Memestr** - Visualisez et créez des mèmes sur Nostr.
* **Quotestr** - Transformez une note Nostr en citation d'image.

---

## REJOIGNEZ-NOUS
* Nostr est encore très jeune. Tout comme bitcoin, mais beaucoup
plus jeune, c'est une expérience populaire, désordonnée, mondiale et ascendante.
* Si vous voyez la valeur d'un protocole de communications décentralisé, résistant à la censure et open source,
veuillez vous joindre à nous pour l'utiliser, le développer, offrir
des commentaires aux développeurs et participer de quelque
manière que vous vous sentiez appelé, pour aider à développer cet outil de liberté d'expression.
* C'est une expérience incroyable de s'engager dans une
technologie en pleine croissance qui est conçue pour préserver la liberté d'expression
et la communication ouverte à l'échelle mondiale.
* Plongez-vous et apprenez avec le reste d'entre nous âmes souveraines,
embrassant le chaos inhérent pour créer la beauté,
et pour forger un avenir radieux pour nos petits-enfants !

*Plus important que tout, nous devons garder à l'esprit que
nostr est juste un ensemble très lâche de serveurs sans pratiquement aucune
connexion entre eux, ... et le processus de rester
connecté aux autres et de trouver du contenu doit être
abordé par de nombreuses tentatives de piratage différentes. Pour
écrire des applications Nostr et pour utiliser Nostr, il
faut embrasser le chaos inhérent.*

*~ @fiatjaf de :*

*'Une vision de la découverte de contenu et de l'utilisation des relais
pour les réseaux sociaux de base dans Nostr'*

---

Profonde gratitude à Satoshi, Fiatjaf, les cypherpunks
passés, présents et futurs, la famille Nostr, le vortex BT, les
maxis toxiques, les maxis non toxiques, les seigneurs des mèmes et -
dames, les croyants, les cyniques, les voyants...
et toujours,
ma famille bien-aimée, mes amis,
et Celui qui respire à travers nous tous,
pour toujours me voir à travers,
plus précieux que tout, même bitcoin

PDF gratuit de ce livre et des traductions
disponibles sur : thesimplestbitcoinbook.net

![c1](figure-048-c1.png)

Suivez-moi sur nostr :

![c2](figure-049-c2.jpg)

Commentaires, questions, mises à jour, commentaires :

thesimplestbitcoinbook@proton.me

Je ne peux pas promettre que je m'en occuperai en temps voulu...

pourrait être pieds nus sur une montagne quelque part

Empilez les sats

Restez fort

Restez fidèle

à la fin, l'Amour

851522
