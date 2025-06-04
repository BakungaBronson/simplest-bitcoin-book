# UNA PAROLA SULLA LIGHTNING NETWORK
* **I blocchi Bitcoin sono intenzionalmente piccoli*** (1MB ciascuno),
il che fa sì che la mainchain di Bitcoin possa elaborare circa 7 transazioni al secondo (TPS).
* Visa elabora circa 24.000 TPS.
* Inoltre, **generalmente ci vogliono circa 10 minuti
perché la prima conferma vada a buon fine su una
transazione mainchain** (dato che un blocco viene
minato in media ogni ~10 minuti).
* Questo non è pratico se sei in un negozio e vuoi
fare un pagamento rapido per i tuoi beni.

> ***Dettaglio Importante:** La ragione per cui i blocchi sono piccoli,
è per mantenere **la timechain abbastanza piccola da permettere a chiunque
di far funzionare il proprio nodo a casa, il che aiuta a mantenere
la rete decentralizzata.** Satoshi si rese conto della
importanza di questo.

>*Gli utenti di Bitcoin potrebbero diventare sempre più
tirannici riguardo alla limitazione della dimensione
della catena, in modo che sia facile per molti utenti
e piccoli dispositivi.*

~ Satoshi Nakamoto, 2010-12-10

**Letture Consigliate:**
* The Blocksize War di Jonathan Bier
---

>* Entra in scena la **Lightning Network (LN),** una **soluzione di
>scaling di livello 2 per Bitcoin.**
>* **'Livello 2'** significa **che è costruita sopra Bitcoin.**
>* **'Soluzione di Scaling'** significa che permette alla rete di:
>* ** Aumentare enormemente la velocità di elaborazione.**
>* **Aumentare enormemente il numero di transazioni che
>può elaborare al secondo.**
>* **Rendere possibili i micropagamenti.**

* La Lightning Network può essere (in un certo senso) pensata come
un conto che potresti tenere aperto con alcuni amici al bar.
* Tenete traccia tra tutti voi di chi deve cosa
(come un canale Lightning Network), e alla fine
della serata il vostro gruppo salda il conto con il barista
('la mainchain').
* **I canali Lightning, tuttavia, possono rimanere aperti
per giorni, settimane, mesi o anni prima di essere
'saldati' sulla mainchain.**

---
## BENEFICI DI :
* **VOLUME** - Il volume di transazioni al secondo è
in sostanza illimitato, poiché innumerevoli canali possono essere
aperti contemporaneamente, ognuno tenendo il proprio
'conto'.
* **MICROPAGAMENTI** - Puoi inviare anche solo 1
satoshi (attualmente $0.0006).
* **VELOCITÀ** - Di solito ci vuole tra un millisecondo e pochi
secondi per ricevere un pagamento.
* **PRIVACY** - Le transazioni non vengono memorizzate sulla
blockchain di Bitcoin aperta e pubblica. In un certo senso è
ancora più privato del contante, perché con Lightning,
anche l'altra parte non sa necessariamente chi
sei, dato che il tuo pagamento spesso 'salta' attraverso
diversi canali per raggiungere il destinatario.

Per essere chiari, non sto dicendo che sia impossibile al 100% da
scoprire, solo molto più che con i pagamenti sulla
mainchain di Bitcoin.
Ci vorrebbe un'enorme quantità di tempo ed energia
per stabilire con certezza chi stava effettuando pagamenti
a chi, e non sarebbe sempre possibile
farlo del tutto.

>**Goditi fantastiche visualizzazioni** dello stato attuale
>della Lightning Network su:
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*Bitcoin stesso non può scalare per fare in modo che ogni
singola transazione finanziaria nel
mondo sia trasmessa a tutti e
inclusa nella blockchain.
Ci deve essere un livello secondario di
sistemi di pagamento che sia più leggero
ed efficiente.*

*~ Hal Finney, 2010-12-30, Pioniere cypherpunk
e la seconda persona ad avviare Bitcoin*

**Pensala così:**
>* Bitcoin: **Conto di Risparmio** ~ Transazioni più lente per
>importi maggiori.
>* Lightning: **Conto Corrente** ~ Transazioni più veloci
>per importi minori.


>*Bitcoin migliorato da Lightning può essere visto sia come un
prodotto (proprietà digitale) che come un servizio (rete monetaria aperta).
La capacità di trasferire energia monetaria attraverso
il tempo e lo spazio senza l'intervento del governo o
il sistema bancario convenzionale è enormemente prezioso per l'umanità.*

~ Michael Saylor, CEO
Microstrategy

**Scopri di più su Lightning qui:**

lopp.net/lightning-information.html

---
