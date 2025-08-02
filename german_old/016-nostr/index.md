# NOSTR

![](figure-044-nostr.png)

## NOSTR & ANDERE DURCH RELAIS ÜBERTRAGENE DINGE

>*Man könnte Gesetze dagegen erlassen, aber die Freiheit der
Rede ist, noch mehr als die Privatsphäre, grundlegend für eine
offene Gesellschaft; wir versuchen, keinerlei Rede einzuschränken.*

~ Eric Hughes, Das Manifest des Cypherpunks, 1993

## WAS IST NOSTR

>*TL;DR: nostr ist ein Protokoll, das die Macht hat,
Twitter, Telegram und andere Dinge zu ersetzen.*

~ @dergigi

>*nostr ist für die Freiheit der Kommunikation
das, was Bitcoin für die Freiheit der Transaktion ist.*

~ Keysa @SimplestBitcoinBook

* **Nostr ist ein einfaches, dezentrales Protokoll für
zensurresistente, globale, interoperable Netzwerke.**
* Nostr ist nicht auf einen vertrauenswürdigen zentralen Server angewiesen.
* Es ist ein freies und Open-Source-Softwareprotokoll (FOSS),
wie Bitcoin, HTTP oder TCP-IP, das es jedem ermöglicht,
auf nostr aufzubauen.
* **Es ist, wie wir unsere Freiheit behalten, zu kommunizieren**
mit jedem, überall mit einer Internetverbindung.

>*(es ist) ein Kommunikationsprotokoll mit einer
selbstbestimmten Identitätsschicht...
und nostr ist auch mehr als das.*

~ @dergigi

---

## WARUM WIR NOSTR BRAUCHEN

Wir brauchen nostr, weil die aktuellen Kommunikationssysteme
und Social-Media-Plattformen zentralisiert sind.

**Das ist problematisch, weil diese Systeme:**

* Die Macht haben, deine Rede zu zensieren.
* Anfällig für regulatorische Angriffe durch den Staat sind.
* Wählen oder angewiesen werden können, dein
Konto zu sperren oder zu löschen.
* Gehackt werden können und somit deine Daten gefährden.
* Algorithmen verwenden, um dir die Informationen zu liefern, die sie wollen,
dass du sie siehst.
* Jeden Aspekt deiner Erfahrung auf ihnen manipulieren.
* Deine gesamte Aktivität verfolgen.
* Deine Daten ernten und verkaufen.
* Deine Daten verwenden, um deinen Feed mit Werbung zuzumüllen.

---

## WIE FUNKTIONIERT NOSTR

* **Nostr hat zwei Teile:** Clients und Relays.
* **Ein CLIENT ist eine BENUTZEROBERFLÄCHE** (App oder Website), die
auf dem nostr-Protokoll läuft.
* **Hier siehst du die Notizen**, die du und die Leute
denen du folgst, posten (auf die gleiche Weise wie Twitter eine
Benutzeroberfläche ist, auf der du Notizen von anderen postest und liest,
außer dass Twitter zentralisiert ist und Beiträge zensiert.)
* **Ein RELAY ist ein SERVER und eine DATENBANK.** Jeder kann
ein Relay betreiben, was nostr dezentralisiert macht.
* **Hier werden deine Notizen gesendet, gespeichert und abgerufen
von** Clients.
* Es gibt viele Relays und du kannst wählen, mit welchen du dich
verbinden möchtest. Einige sind kostenlos und einige sind kostenpflichtig.
* Wenn du eine Nachricht postest, wird sie an die Relays gesendet,
mit denen du verbunden bist.
* Die Clients fragen die Relays ab, mit denen sie verbunden sind, und
dann füllen sie die Nachrichten aus, die von
diesen Relays gehostet werden.

![publish](figure-045-publish.png)

~ @BTCillustrated

---

>*Jeder kann ein Relay betreiben. Ein Relay ist sehr einfach und
dumm. Es tut nichts anderes, als Beiträge von
einigen Leuten anzunehmen und an andere weiterzuleiten.
Relays müssen nicht vertrauenswürdig sein.
Signaturen werden clientseitig verifiziert.*

~ @fiatjaf, 2019-11-02 fiatjaf.com/nostr.html

* Wenn du deinen nostr-Client öffnest, siehst du alle
Notizen, die von dir und denen, denen du folgst, in
chronologischer Reihenfolge gepostet wurden.
* Es gibt keine **Algorithmen**, die entscheiden, was dir gezeigt wird,
was dir vorenthalten wird oder deine Beiträge zensiert.
* Wie Bitcoin verwendet **nostr Public/Private-Key-Paare.**
* **ÖFFENTLICHER SCHLÜSSEL** = npub, wie ein Benutzername
* **PRIVATER SCHLÜSSEL** = nsec, wie ein Passwort

>* **HINWEIS:** Dein privater Schlüssel kann nicht zurückgesetzt werden, wenn
>er verloren geht, daher musst du ihn **gut sichern!**
>* Wenn du deinen privaten Schlüssel preisgibst, hat jeder, der
>Zugriff darauf hat, Zugriff auf dein nostr-
>Konto, und **es gibt keine Möglichkeit,
>den alleinigen Zugriff wiederzuerlangen.**

---

* Du kannst einen für Menschen lesbaren Benutzernamen mit
NIP-05 erstellen. **Zum Beispiel:**
* **Mein öffentlicher Schlüssel, oder npub ist:**
<small>npub1dpna3xwwddnhhzg9ycpvlcz2ze0jdwm2rf3eqd2lf9leaewtq7tqhw0ef2</small>

* **Meine NIP-05 Nostr-Adresse ist:**

SimplestBitcoinBook@nostrplebs.com

* **Du kannst nach Personen auf nostr suchen**, indem du ihre:
* npub
* NIP-05 (aka nostr Adresse), falls vorhanden
* Benutzername von NIP-05 -> @SimplestBitcoinBook

* **Hole dir hier eine NIP-05-Kennung:**
* nostrplebs.com
* verified-nostr.com
* getalby.com
* Oder richte eine mit deiner eigenen Domain ein

* Sobald du dein nostr-Schlüsselpaar hast, kannst du dich mit diesen
selben Schlüsseln in jeden nostr-Client einloggen, und du wirst sehen,
dass du **deine Identität und Follower-/Following-Listen
auf allen Clients behältst.**
* Dies unterscheidet sich von Legacy-Social-Media, wo du ein
separates Konto, Benutzernamen und Passwort für jede
Plattform benötigst und du unterschiedliche Inhalte, Follows und
Follower auf jeder einzelnen hast.
>*Auf der grundlegendsten Ebene ist Nostr ein Kommunikations-
protokoll, das als sozialer Klebstoff dient, der
all deine Apps zusammenhält.*

~ derekross@nostrplebs.com

---

# WIE MAN NOSTR NUTZT

>1. **Wähle eine Client-App** zum Herunterladen aus. (Es spielt keine Rolle,
welche du auswählst, da du sie alle ausprobieren kannst, sobald
du dein Schlüsselpaar generiert hast.)
>2. **Beliebte Client-Beispiele:**
>* Damus auf iOS
>* Amethyst auf Android
>* Primal auf iOS/Android/Desktop
>3. **Erstelle einen Benutzernamen.** Keine weiteren Informationen sind erforderlich.
>4. **Die App generiert das Konto.**
>5. **Du kannst ein Profilbild und ein Banner hinzufügen**, wenn du möchtest.
>6. **Dein Konto verbindet sich automatisch mit einigen
Relays**, sobald du mindestens ein Interesse auswählst (z. B.:
Bitcoin, Kunst, Menschenrechte, Sport, Musik usw.)
>7. Abhängig vom Client folgt er automatisch einigen
Konten mit einem ähnlichen Interesse oder lässt dich einige
auswählen.
>8. **Du kannst dann Relays und Konten hinzufügen oder entfernen.**

![create account on nostr](figure-046-create%20account%20on%20nostr%20.png)

~ @BTCillustrated

---

## SCHLÜSSELVERWALTUNG
* Sobald deine Schlüssel generiert wurden, ist es an der Zeit,
eine **Signaturerweiterung** zu installieren.
* Wenn du dich auf einer Website anmelden möchtest, die auf dem
nostr-Protokoll läuft, wird nach deinem nsec oder privaten Schlüssel gefragt.
* **Gib ihn NICHT** direkt ein, da Websites Daten
verlieren können
* **Verwende stattdessen immer eine Signaturerweiterung.**
* Dies ist ein Tool, das deinen privaten Schlüssel speichert, und du
ermächtigst es, Ereignisse, wie z. B. Notizen, in deinem
Namen zu signieren. Keine Sorge, das ist einfacher als es sich anhört!
* **Beliebte Signaturerweiterungen:**
* Nostore (iOS Safari)
* Amber (Android)
* Nsec App (Mobile/Desktop)
* Alby (Desktop)
* Nos2X (Desktop)
* Nostr Connect (Desktop)

## ZAPS
* Zappen ist, wie wir Bitcoin auf nostr betreiben! Eine V4V
(Value4Value)-Wirtschaft schaffen, Notiz für Notiz, Zap für Zap.
* Du kannst Sats (aka Zaps) für Notizen oder
Inhalte, die du schätzt, senden und empfangen, indem du ein
Bitcoin-Lightning-Wallet mit deinem nostr-Konto verbindest.
* Es gibt verschiedene Möglichkeiten, dies zu tun. Wenn der von dir
gewählte Client dich nicht durch den Prozess führt, frage einfach auf nostr
mit dem Tag #asknostr, und jemand wird dich anleiten.
Strauße sind freundlich

---

## NOSTR-RESSOURCEN
Unten ist eine Liste von Websites, die ausgezeichnete, leicht
verständliche Anleitungen zu nostr und seinen Wundern haben!

* nostr-resources.com von @derGigi
* nostr.com von @fiatjaf
* nostr.net von @aljaz
* nostr.how von @JeffG
* usenostr.org von @pluja
* benwehrman.com/nostr-guide von @benwehrman
* nostrapps.com von @Karnage

## WARUM DER STRAUSS?

![ostrich](figure-047-ostrich.png)

**Die Entstehungsgeschichte des Nostrich**

von Walker@primal.net

**16. Dezember 2022:**

Ich entdeckte ChatGPT3 und
fragte es natürlich
"Kannst du einen Witz über #nostr schreiben?"
ChatGPT3 antwortete:
F: Wie nennt man einen neugierigen Strauß?
A: Einen NosTrich!
Der Witz war nicht großartig, aber man kann es einem Bot nicht verdenken. Trotzdem
gefiel mir die Idee einer visuellen Identität für nostr, und Strauße sind
coole Vögel. Also wandte ich mich an Midjourney und erstellte The #Nostrich

**20. Dezember 2022:**

@jb55 schlug den "Nostrich" als offizielles Nostr-Maskottchen
und Logo vor.
Drei Minuten später twittert @jack das Nostrich-Bild.
Der Rest ist, wie man so sagt, Geschichte.

~ @Walker

---

## NOSTR CLIENTS/APPS

Besuche **nostrapps.com**, um diese und viele weitere
erstaunliche Apps zu finden, die auf dem freien, Open-Source-nostr-Protokoll basieren.
Verwende deine Signaturerweiterung, um dich bei allen anzumelden!

* **Nostr Nests** - Ein Audio-Raum für Chatten, Jammen,
Mikro-Konferenzen, Live-Podcasts.
* **Plebian Market** - Der selbstbestimmte Marktplatz des
Internets, betrieben von Bitcoin & Lightning.
* **Npub.pro** - Erstelle dir eine nostr-basierte Website.
* **Corny Chat** - Live-Audio-Räume.
* **Wavlake** - Eine Musik-Streaming-Plattform, die das
Lightning-Netzwerk von Bitcoin nutzt, um Wert für Wert zu bieten.
* **Zap.stream** - Hoste deinen Live-Stream und erhalte Sat-Zaps.
* **Flare** - Ein Client zum Anzeigen, Hochladen und Interagieren
mit Videoinhalten.
* **Blowater** - Entwickelt, um Telegram/Slack/Discord zu ersetzen.
* **Stemstr** - Eine soziale Erfahrung für Musikkünstler, um
sich zu vernetzen, zusammenzuarbeiten und erstaunliche Musik zu teilen.
* **Nostr.build** - Bild-, Video- und Medien-Uploader & Host.
* Hivetalk - Echtzeit-, total private Videoanrufe und
Meetings, ersetzt Zoom.
* **Zap.cooking** - Teile Rezepte über Nostr.
* **Flockstr** - Veranstaltungen und Meetup-Planung.
* **Memestr** - Anzeigen und Erstellen von Memes über Nostr
* **Quotestr** - Mache eine Nostr-Notiz zu einem Bildzitat.

---

## MACH MIT
* Nostr ist noch sehr jung. Genau wie Bitcoin, aber viel
jünger, ist es ein von unten aufgebautes, chaotisches, globales
Experiment.
* Wenn du den Wert in einem dezentralen, zensurresistenten,
Open-Source-Kommunikationsprotokoll siehst,
bitte schließe dich uns an, es zu nutzen, es zu entwickeln,
Feedback an die Entwickler zu geben und auf jede
Art und Weise teilzunehmen, wie du dich berufen fühlst, um dieses
Tool für freie Meinungsäußerung zu fördern.
* Es ist eine erstaunliche Erfahrung, sich an einer wachsenden
Technologie zu beteiligen, die entwickelt wurde, um die freie Meinungsäußerung
und offene Kommunikation weltweit zu bewahren.
* Tauche ein und lerne zusammen mit dem Rest von uns souveränen
Seelen, umarme das inhärente Chaos, um Schönheit zu erschaffen,
und eine strahlende Zukunft für unsere Enkelkinder zu gestalten!

*Wichtiger als alles andere ist, dass wir uns vor Augen halten müssen, dass
nostr nur eine sehr lose Ansammlung von Servern ist, die im Grunde keine
Verbindung untereinander haben, ... und der Prozess, mit anderen in Verbindung zu bleiben
und Inhalte zu finden, muss durch viele verschiedene
Hack-Versuche angegangen werden. Um Nostr-Anwendungen zu schreiben und Nostr zu verwenden,
muss man das inhärente Chaos annehmen.*

*~ @fiatjaf von:*

*'Eine Vision für die Inhaltsfindung und Relay-Nutzung
für grundlegendes Social Networking in Nostr'*

---

Tiefe Dankbarkeit an Satoshi, Fiatjaf, die Cypherpunks
Vergangenheit, Gegenwart und Zukunft, die Nostr-Familie, den BT-Vortex, die
toxischen Maxis, die nicht-toxischen Maxis, die Meme-Lords und -
Damen, die Gläubigen, die Zyniker, die Seher...
und immer,
meine geliebte Familie, Freunde
und der Eine, der durch uns alle atmet,
weil er mich immer durchbringt,
kostbarer als alles, sogar Bitcoin

Kostenlose PDF-Datei dieses Buches und die Übersetzungen
verfügbar unter: thesimplestbitcoinbook.net

![c1](figure-048-c1.png)

Folge mir auf nostr:

![c2](figure-049-c2.jpg)

Kommentare, Fragen, Aktualisierungen, Feedback:

thesimplestbitcoinbook@proton.me

Kann nicht versprechen, dass ich es rechtzeitig schaffen werde ...

bin vielleicht barfuß auf einem Berg irgendwo

Stack Sats

Bleib stark

Bleib treu

am Ende, Liebe

851522
