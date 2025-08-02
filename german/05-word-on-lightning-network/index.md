# EIN WORT ZUM LIGHTNING NETZWERK
* **Bitcoin-Blöcke sind absichtlich klein*** (je 1 MB),
wodurch die Bitcoin-Hauptkette etwa 7 Transaktionen pro Sekunde (TPS) verarbeiten kann.
* Visa verarbeitet etwa 24.000 TPS.
* Außerdem **dauert es in der Regel etwa 10 Minuten, bis die
erste Bestätigung für eine Hauptketten-Transaktion
erfolgt** (da ein Block im
Durchschnitt alle ~10 Minuten abgebaut wird).
* Das ist nicht praktikabel, wenn du in einem Geschäft bist und schnell für deine Waren bezahlen möchtest.

> ***Wichtiges Detail:** Der Grund, warum die Blöcke klein sind,
ist, **die Timechain klein genug zu halten, damit jeder
seinen eigenen Knoten zu Hause betreiben kann, was dazu beiträgt,
das Netzwerk dezentral zu halten.** Satoshi erkannte die
Bedeutung dessen

>*Bitcoin-Nutzer könnten zunehmend
tyrannisch werden, wenn es darum geht, die Größe
der Kette zu begrenzen, damit sie für viele Nutzer
und kleine Geräte einfach ist.*

~ Satoshi Nakamoto, 10.12.2010

**Empfohlene Lektüre:**
* The Blocksize War von Jonathan Bier
---

>* Hier kommt das **Lightning Network (LN) ins Spiel,** eine **Layer-2-Bitcoin-
>Skalierungslösung.**
>* **"Layer 2"** bedeutet, **dass es auf Bitcoin aufgebaut ist.**
>* **"Skalierungslösung"** bedeutet, dass es dem Netzwerk Folgendes ermöglicht:
>* **Die Geschwindigkeit der Verarbeitung deutlich zu erhöhen.**
>* **Die Anzahl der Transaktionen, die es
>pro Sekunde verarbeiten kann, deutlich zu erhöhen.**
>* **Mikrozahlungen zu ermöglichen.**

* Das Lightning Network kann (sozusagen) als eine Art
Rechnung betrachtet werden, die du mit einigen Freunden in der Bar hast.
* Ihr behaltet untereinander den Überblick, wer wem was schuldet
(wie ein Lightning Network Kanal), und am Ende
des Abends begleicht eure Gruppe die Rechnung mit dem Barkeeper
("die Hauptkette").
* **Lightning-Kanäle können jedoch für
Tage, Wochen, Monate oder Jahre geöffnet bleiben, bevor sie
in der Hauptkette "beglichen" werden.**

---
## VORTEILE VON :
* **VOLUMEN** - Das Volumen der Transaktionen pro Sekunde ist
im Wesentlichen unbegrenzt, da unzählige Kanäle gleichzeitig
geöffnet werden können, von denen jeder seine eigene
"Rechnung" führt.
* **MIKROZAHLUNGEN** - Du kannst so wenig wie 1
Satoshi senden (derzeit 0,0006 $).
* **GESCHWINDIGKEIT** - Es dauert in der Regel zwischen einer Millisekunde und einigen
Sekunden, um eine Zahlung zu erhalten.
* **PRIVATSPHÄRE** - Transaktionen werden nicht in der offenen,
öffentlichen Bitcoin-Blockchain gespeichert. In gewisser Weise ist es sogar
privater als Bargeld, denn bei Lightning weiß
nicht einmal die andere Partei unbedingt, wer
du bist, da deine Zahlung oft durch
verschiedene Kanäle "springt", um den Empfänger zu erreichen.

Um es klarzustellen, ich sage nicht, dass es zu 100 % unmöglich ist, dies
aufzudecken, nur viel mehr als bei Zahlungen auf der
Bitcoin-Hauptkette.
Es würde eine immense Menge an Zeit und Energie
kosten, um mit Sicherheit festzustellen, wer Zahlungen
an wen leistet, und es wäre nicht immer möglich,
dies überhaupt zu tun.

>**Genieße erstaunliche Visualisierungen** des aktuellen Zustands
>des Lightning Networks unter:
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*Bitcoin selbst kann nicht so skaliert werden, dass jede
einzelne Finanztransaktion der
Welt an jeden übertragen und
in die Blockchain aufgenommen wird.
Es muss eine zweite Ebene von
Zahlungssystemen geben, die leichter
und effizienter ist.*

*~ Hal Finney, 30.12.2010, Früher Cypherpunk
& die zweite Person, die Bitcoin betrieben hat*

**Stell es dir so vor:**
>* Bitcoin: **Sparkonto** ~ Langsamere Transaktionen für
>größere Beträge.
>* Lightning: **Girokonto** ~ Schnellere Transaktionen
>für kleinere Beträge.


>*Bitcoin, erweitert durch Lightning, kann sowohl als Produkt (digitales Eigentum) als auch als Dienstleistung (offenes monetäres
Netzwerk) betrachtet werden. Die Fähigkeit, monetäre Energie durch
Zeit und Raum ohne staatliche Intervention oder
konventionelles Bankwesen zu transferieren, ist für die Menschheit von enormem Wert.*

~ Michael Saylor, CEO
Microstrategy

**Erfahre hier mehr über Lightning:**

lopp.net/lightning-information.html

---
