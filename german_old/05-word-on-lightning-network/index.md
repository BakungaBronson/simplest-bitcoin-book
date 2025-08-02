# EIN WORT ZUM LIGHTNING NETWORK
* **Bitcoin-Blöcke sind absichtlich klein*** (jeweils 1 MB),
was dazu führt, dass die Bitcoin-Hauptkette etwa 7 Transaktionen pro Sekunde (TPS) verarbeiten kann.
* Visa verarbeitet etwa 24.000 TPS.
* Außerdem **dauert es in der Regel etwa 10 Minuten, bis die
erste Bestätigung für eine Hauptketten-
Transaktion durchläuft** (da ein Block im
Durchschnitt alle ~10 Minuten geschürft wird).
* Dies ist nicht praktikabel, wenn Sie in einem Geschäft sind und
eine schnelle Bezahlung für Ihre Waren vornehmen möchten.

> ***Wichtiges Detail:** Der Grund, warum die Blöcke klein sind,
ist, um **die Timechain klein genug zu halten, damit jeder
seinen eigenen Knoten zu Hause betreiben kann, was dazu beiträgt,
das Netzwerk dezentralisiert zu halten.** Satoshi erkannte die
Bedeutung davon

>*Bitcoin-Nutzer könnten zunehmend
tyrannischer werden, wenn es darum geht, die Größe der
Kette zu begrenzen, damit es für viele Nutzer
und kleine Geräte einfach ist.*

~ Satoshi Nakamoto, 2010-12-10

**Empfohlene Lektüre:**
* Der Blocksize War von Jonathan Bier
---

>* Treten Sie ein, das **Lightning Network (LN),** eine **Layer-2-Bitcoin-
>Skalierungslösung.**
>* **"Layer 2"** bedeutet, **dass es auf Bitcoin aufbaut.**
>* **"Skalierungslösung"** bedeutet, dass es dem Netzwerk Folgendes ermöglicht:
>* **Die Verarbeitungsgeschwindigkeit wird erheblich erhöht.**
>* **Die Anzahl der Transaktionen, die es
>pro Sekunde verarbeiten kann, wird erheblich erhöht.**
>* **Ermöglichen von Mikrozahlungen.**

* Das Lightning Network kann (sozusagen) als eine Art
Rechnung betrachtet werden, die Sie möglicherweise mit einigen Freunden in der Bar haben.
* Sie behalten den Überblick, wer wem was schuldet
(wie ein Lightning-Network-Kanal), und am Ende
des Abends rechnet Ihre Gruppe mit dem Barkeeper ab
("die Hauptkette").
* **Lightning-Kanäle können jedoch für
Tage, Wochen, Monate oder Jahre offen bleiben, bevor sie
auf der Hauptkette "abgerechnet" werden.**

---
## VORTEILE VON:
* **VOLUMEN** - Das Volumen der Transaktionen pro Sekunde ist
im Wesentlichen unbegrenzt, da unzählige Kanäle
gleichzeitig geöffnet werden können, wobei jeder seine eigene
"Rechnung" führt.
* **MIKROZAHLUNGEN** - Sie können so wenig wie 1
Satoshi senden (derzeit 0,0006 $).
* **GESCHWINDIGKEIT** - Es dauert normalerweise zwischen einer Millisekunde und
ein paar Sekunden, bis eine Zahlung empfangen wird.
* **DATENSCHUTZ** - Transaktionen werden nicht auf der offenen,
öffentlichen Bitcoin-Blockchain gespeichert. In gewisser Weise ist sie sogar
privater als Bargeld, denn mit Lightning
weiß selbst die andere Partei nicht unbedingt, wer
Sie sind, da Ihre Zahlung oft durch
verschiedene Kanäle "springt", um den Empfänger zu erreichen.

Um es klarzustellen, ich sage nicht, dass es zu 100 % unmöglich ist,
aufzudecken, nur weitaus mehr als bei Zahlungen auf der
Bitcoin-Hauptkette.
Es würde eine immense Menge an Zeit und Energie kosten,
mit Sicherheit festzustellen, wer Zahlungen
an wen leistet, und es wäre nicht immer möglich,
dies überhaupt zu tun.

>**Genießen Sie erstaunliche Visualisierungen** des aktuellen Zustands
>des Lightning Network unter:
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*Bitcoin selbst kann nicht skaliert werden, um jede
einzelne Finanztransaktion der
Welt an alle zu übertragen und
in die Blockchain aufzunehmen.
Es muss eine sekundäre Ebene von
Zahlungssystemen geben, die leichter
und effizienter ist.*

*~ Hal Finney, 2010-12-30, Früher Cypherpunk
& die zweite Person, die Bitcoin betrieben hat*

**Stellen Sie es sich so vor:**
>* Bitcoin: **Sparkonto** ~ Langsamere Transaktionen für
>größere Beträge.
>* Lightning: **Girokonto** ~ Schnellere Transaktionen
>für kleinere Beträge.


>*Bitcoin, erweitert durch Lightning, kann sowohl als
Produkt (digitales Eigentum) als auch als Dienstleistung (offenes monetäres
Netzwerk) betrachtet werden. Die Fähigkeit, monetäre Energie durch
Zeit und Raum ohne staatliche Intervention oder
konventionelles Bankwesen zu übertragen, ist für die Menschheit von enormem Wert.*

~ Michael Saylor, CEO
Microstrategy

**Erfahren Sie hier mehr über Lightning:**

lopp.net/lightning-information.html

---
