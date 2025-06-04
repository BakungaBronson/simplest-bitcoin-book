# NOSTR

![](figure-044-nostr.png)

## NOSTR & ALTRE COSE TRASMESSE DAI RELAY

>*Si potrebbero approvare leggi contro di essa, ma la libertà di
parola, anche più della privacy, è fondamentale per una
società aperta; non cerchiamo di limitare in alcun modo la parola.*

~ Eric Hughes, Il manifesto Cypherpunk, 1993

## COS'È NOSTR

>*TL;DR: nostr è un protocollo che ha il potere di
sostituire twitter, Telegram e altre cose.*

~ @dergigi

>*nostr sta alla libertà di comunicazione
come bitcoin sta alla libertà di transazione.*

~ Keysa @SimplestBitcoinBook

* **Nostr è un protocollo semplice, decentralizzato per
reti globali, interoperabili e resistenti alla censura.**
* Nostr non si affida a un server centrale fidato.
* È un protocollo software libero e open source (FOSS),
come Bitcoin, HTTP o TCP-IP, che consente a chiunque di
costruire su nostr.
* **È come conserviamo la nostra libertà di comunicare**
con chiunque, ovunque con una connessione internet.

>*(è) un protocollo di comunicazione con un
livello di identità auto-sovrano...
e nostr è anche più di questo.*

~ @dergigi

---

## PERCHÉ ABBIAMO BISOGNO DI NOSTR

Abbiamo bisogno di nostr perché gli attuali sistemi di
comunicazione e le piattaforme di social media sono centralizzati.

**Questo è problematico perché questi sistemi:**

* Hanno il potere di censurare il tuo discorso.
* Sono vulnerabili agli attacchi normativi da parte dello stato.
* Possono scegliere, o essere detto, di sospendere o eliminare il tuo
account.
* Possono essere hackerati e quindi compromettere i tuoi dati.
* Usano algoritmi per fornirti le informazioni che vogliono
farti vedere.
* Manipolano ogni aspetto della tua esperienza su di essi.
* Tracciano tutta la tua attività.
* Raccolgono e vendono i tuoi dati.
* Usano i tuoi dati per riempire il tuo feed di pubblicità.

---

## COME FUNZIONA NOSTR

* **Nostr ha due parti:** Client e Relay.
* **Un CLIENT è un'INTERFACCIA** (app o sito web) che viene eseguito
sul protocollo nostr.
* **È dove vedi le note** che tu e le persone
che segui pubblicano (nello stesso modo in cui twitter è un'
interfaccia in cui pubblichi e leggi note di altri,
tranne che twitter è centralizzato e censura i post.)
* **Un RELAY è un SERVER e un DATABASE.** Chiunque può
eseguire un relay, che è ciò che rende nostr decentralizzato.
* **È dove le tue note vengono inviate, memorizzate e recuperate
da** dai client.
* Ci sono molti relay e puoi scegliere a quali
connetterti. Alcuni sono gratuiti e alcuni sono a pagamento.
* Quando pubblichi un messaggio, viene trasmesso ai relay
a cui sei connesso.
* I client interrogano i relay a cui sono connessi e
quindi popolano i messaggi ospitati da
quei relay.

![publish](figure-045-publish.png)

~ @BTCillustrated

---

>*Chiunque può eseguire un relay. Un relay è molto semplice e
stupido. Non fa altro che accettare post
da alcune persone e inoltrarli ad altri.
I relay non devono essere considerati affidabili.
Le firme vengono verificate sul lato client.*

~ @fiatjaf, 2019-11-02 fiatjaf.com/nostr.html

* Quando apri il tuo client nostr, vedrai tutte le
note pubblicate da te e da coloro che segui in
ordine cronologico.
* Non ci sono **algoritmi** che decidono cosa mostrarti,
cosa nasconderti o censurare i tuoi post.
* Come Bitcoin, **nostr utilizza coppie di chiavi pubblica/privata.**
* **CHIAVE PUBBLICA** = npub, come un nome utente
* **CHIAVE PRIVATA** = nsec, come una password

>* **NOTA:** La tua chiave privata non può essere ripristinata se
>persa, quindi devi **proteggerla bene!**
>* Se riveli la tua chiave privata, chiunque abbia
>accesso ad essa ha accesso al tuo
>account nostr e **non c'è modo di riottenere
>l'accesso esclusivo.**

---

* Puoi creare un nome utente leggibile usando
NIP-05. **Ad esempio:**
* **La mia chiave pubblica, o npub è:**
<small>npub1dpna3xwwddnhhzg9ycpvlcz2ze0jdwm2rf3eqd2lf9leaewtq7tqhw0ef2</small>

* **Il mio indirizzo Nostr NIP-05 è:**

SimplestBitcoinBook@nostrplebs.com

* **Puoi cercare persone su nostr** inserendo il loro:
* npub
* NIP-05 (aka indirizzo nostr) se ne hanno uno
* Nome utente da NIP-05 -> @SimplestBitcoinBook

* **Ottieni un identificatore NIP-05 qui:**
* nostrplebs.com
* verified-nostr.com
* getalby.com
* Oppure impostane uno con il tuo dominio

* Una volta che hai la tua coppia di chiavi nostr, puoi accedere a qualsiasi
client nostr con quelle stesse chiavi e vedrai che
**mantieni la tua identità e le liste di follower/following
su tutti i client.**
* Questo differisce dai social media legacy, dove hai bisogno di un
account separato, nome utente e password per ogni
piattaforma e hai contenuti, follower e
seguaci diversi su ciascuna.
>*Al suo livello più elementare, Nostr è un protocollo di comunicazione
che agisce come il collante sociale che lega
tutte le tue app insieme.*

~ derekross@nostrplebs.com

---

# COME USARE NOSTR

>1. **Scegli un'app client** da scaricare. (Non importa
quale selezioni, poiché puoi provarli tutti una volta
che hai generato la tua coppia di chiavi.)
>2. **Esempi di client popolari:**
>* Damus su iOS
>* Amethyst su Android
>* Primal su iOS/Android/Desktop
>3. **Crea un nome utente.** Non sono necessarie altre informazioni.
>4. **L'app genererà l'account.**
>5. **Puoi aggiungere un'immagine del profilo e un banner** se lo desideri.
>6. **Il tuo account si connetterà automaticamente a alcuni
relay** una volta che selezioni almeno un interesse (es:
bitcoin, arte, diritti umani, sport, musica ecc.)
>7. A seconda del client, seguirà automaticamente alcuni
account con un interesse simile o ti permetterà di selezionarne alcuni.
>8. **Puoi quindi aggiungere o rimuovere relay e account.**

![create account on nostr](figure-046-create%20account%20on%20nostr%20.png)

~ @BTCillustrated

---

## GESTIONE DELLE CHIAVI
* Una volta che le tue chiavi sono state generate, è il momento di
installare un **estensione di firma.**
* Quando vuoi accedere a un sito web in esecuzione sul
protocollo nostr, ti chiederà il tuo nsec o chiave privata.
* **NON** inserirlo direttamente, poiché i siti web possono divulgare dati
* **Invece, usa sempre un'estensione di firma.**
* Questo è uno strumento che memorizza la tua chiave privata e tu
lo autorizzi a firmare eventi, come le note, per tuo
conto. Non preoccuparti, è più semplice di quanto sembri!
* **Estensioni di firma popolari:**
* Nostore (iOS Safari)
* Amber (Android)
* Nsec App (Mobile/Desktop)
* Alby (Desktop)
* Nos2X (Desktop)
* Nostr Connect (Desktop)

## ZAP
* Zapping è come usiamo bitcoin su nostr! Creando una V4V
(Value4Value) economia, nota per nota, zap per zap.
* Puoi inviare e ricevere sat (aka zap) per note o
contenuti che apprezzi collegando un portafoglio
Bitcoin Lightning al tuo account nostr.
* Ci sono vari modi per farlo. Se il client che
scegli non ti guida attraverso di esso, chiedi su nostr
con il tag #asknostr e qualcuno ti guiderà.
I Nostrici sono amichevoli

---

## RISORSE NOSTR
Di seguito è riportato un elenco di siti web che hanno eccellenti, facilmente
guide digeribili su nostr e le sue meraviglie!

* nostr-resources.com di @derGigi
* nostr.com di @fiatjaf
* nostr.net di @aljaz
* nostr.how di @JeffG
* usenostr.org di @pluja
* benwehrman.com/nostr-guide di @benwehrman
* nostrapps.com di @Karnage

## PERCHÉ LO STRUZZO?

![ostrich](figure-047-ostrich.png)

**La storia dell'origine del Nostrich**

di Walker@primal.net

**16 dicembre 2022:**

Ho scoperto ChatGPT3 e,
naturalmente, gli ho chiesto
"Puoi scrivere una barzelletta su #nostr?"
ChatGPT3 ha risposto:
D: Come chiami uno struzzo ficcanaso?
A: Un nosTrich!
La barzelletta non era eccezionale, ma non puoi biasimare un bot. Indipendentemente da ciò, io
ho amato l'idea di un'identità visiva per nostr e gli struzzi sono
uccelli fantastici. Così ho preso Midjourney e ho creato The #Nostrich

**20 dicembre 2022:**

@jb55 ha proposto il "Nostrich" come mascotte
e logo ufficiale di Nostr.
Tre minuti dopo, @jack twitta l'immagine di Nostrich.
Il resto, come si dice, è storia.

~ @Walker

---

## CLIENT/APP NOSTR

Visita **nostrapps.com** per trovare questi e tanti altri
straordinarie app costruite sul protocollo nostr gratuito e open source.
Usa la tua estensione di firma per accedere a tutti!

* **Nostr Nests** - Uno spazio audio per chattare, fare jam session,
micro-conferenze, podcast dal vivo.
* **Plebian Market** - Il marketplace auto-sovrano di
Internet, alimentato da Bitcoin & Lightning.
* **Npub.pro** - Crea un sito web basato su nostr.
* **Corny Chat** - Spazi audio dal vivo.
* **Wavlake** - Una piattaforma di streaming musicale che utilizza
La rete Lightning di Bitcoin per offrire valore per valore.
* **Zap.stream** - Ospita il tuo live stream e ottieni sat zap.
* **Flare** - Un client per visualizzare, caricare e interagire
con contenuti video.
* **Blowater** - Costruito per sostituire Telegram/Slack/Discord.
* **Stemstr** - Un'esperienza social per artisti musicali per
connettersi, collaborare e condividere musica straordinaria.
* **Nostr.build** - Caricatore e host di immagini, video e media.
* Hivetalk - Videochiamate e
riunioni in tempo reale, totalmente private, sostituisce Zoom.
* **Zap.cooking** - Condividi ricette su Nostr.
* **Flockstr** - Eventi e programmazione di incontri.
* **Memestr** - Visualizza e crea meme su Nostr
* **Quotestr** - Trasforma una nota Nostr in una citazione immagine.

---

## UNISCITI A NOI
* Nostr è ancora molto giovane. Proprio come bitcoin, ma molto
più giovane, è un esperimento popolare, disordinato, globale, dal basso.
* Se vedi il valore in un protocollo di comunicazioni
decentralizzato, resistente alla censura e open source,
unisciti a noi nell'utilizzarlo, svilupparlo, offrendo
feedback agli sviluppatori e partecipando in qualsiasi
modo ti senti chiamato, per aiutare a far crescere questo strumento di libertà di parola.
* È un'esperienza straordinaria impegnarsi in una tecnologia
in crescita costruita per preservare la libertà di parola
e la comunicazione aperta a livello globale.
* Immergiti e impara insieme al resto di noi anime sovrane,
abbracciando il caos inerente per creare bellezza
e per forgiare un futuro luminoso per i nostri nipoti!

*Più importante di tutto è che dobbiamo tenere a mente che
nostr è solo un insieme molto libero di server senza praticamente
nessuna connessione tra loro, ... e il processo di mantenersi
connessi agli altri e trovare contenuti deve essere
affrontato attraverso molti tentativi pasticciati diversi. Per
scrivere applicazioni Nostr e per usare Nostr uno
deve abbracciare il caos inerente.*

*~ @fiatjaf da:*

*'Una visione per la scoperta di contenuti e l'uso del relay
per il social networking di base in Nostr'*

---

Profonda gratitudine a Satoshi, Fiatjaf, ai cypherpunk
passati, presenti e futuri, alla famiglia Nostr, al vortice BT, ai
massimalisti tossici, ai massimalisti non tossici, ai signori e alle signore dei meme,
ai credenti, ai cinici, ai veggenti...
e sempre,
alla mia amata famiglia, agli amici,
e a Colui che respira attraverso tutti noi,
per avermi sempre accompagnato,
più prezioso di qualsiasi cosa, anche di bitcoin

PDF gratuito di questo libro e delle traduzioni
disponibile su: thesimplestbitcoinbook.net

![c1](figure-048-c1.png)

Seguimi su nostr:

![c2](figure-049-c2.jpg)

Commenti, domande, aggiornamenti, feedback:

thesimplestbitcoinbook@proton.me

Non posso promettere che lo farò in modo tempestivo ...

potrei essere a piedi nudi su una montagna da qualche parte

Accumula sat

Rimani forte

Rimani fedele

alla fine, Amore

851522
