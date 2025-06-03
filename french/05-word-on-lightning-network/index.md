# UN MOT SUR LE LIGHTNING NETWORK
* **Les blocs Bitcoin sont intentionnellement petits*** (1 Mo chacun),
ce qui fait que la chaîne principale de bitcoin peut traiter environ 7 transactions par seconde (TPS).
* Visa traite environ 24 000 TPS.
* De plus, **il faut généralement environ 10 minutes pour que la
première confirmation soit validée sur une
transaction de la chaîne principale** (puisqu'un bloc est miné en
moyenne toutes les ~10 minutes).
* Ce n'est pas pratique si vous êtes dans un magasin et que vous voulez
effectuer un paiement rapide pour vos marchandises.

> ***Détail important :** La raison pour laquelle les blocs sont petits,
c'est pour que **la chaîne temporelle reste suffisamment petite pour que chacun puisse
faire fonctionner son propre nœud à la maison, ce qui contribue à maintenir la
décentralisation du réseau.** Satoshi a compris l'importance de ceci.

>*Les utilisateurs de Bitcoin pourraient devenir de plus en plus
tyranniques quant à la limitation de la taille de
la chaîne afin qu'elle soit facile à utiliser pour de nombreux utilisateurs
et de petits appareils.*

~ Satoshi Nakamoto, 2010-12-10

**Lecture recommandée :**
* The Blocksize War par Jonathan Bier
---

>* Entrez, le **Lightning Network (LN),** une **solution de mise à l'échelle
>bitcoin de niveau 2.**
>* **'Niveau 2'** signifie **qu'il est construit au-dessus de bitcoin.**
>* **'Solution de mise à l'échelle'** signifie qu'elle permet au réseau de :
>* **Augmenter considérablement la vitesse de traitement.**
>* **Augmenter considérablement le nombre de transactions qu'il
>peut traiter par seconde.**
>* **Rendre les micropaiements possibles.**

* Le Lightning Network peut être (en quelque sorte) considéré comme
un onglet que vous pourriez garder avec des amis au bar.
* Vous gardez une trace entre vous tous de qui doit quoi
(comme un canal Lightning Network), et à la fin
de la soirée, votre groupe règle la note avec le barman
(‘la chaîne principale’).
* **Les canaux Lightning, cependant, peuvent rester ouverts pendant
des jours, des semaines, des mois ou des années avant d'être
'réglés' sur la chaîne principale.**

---
## AVANTAGES DE :
* **VOLUME** - Le volume de transactions par seconde est
en substance illimité, car d'innombrables canaux peuvent être
ouverts en même temps, chacun conservant son propre
‘onglet’.
* **MICROPAYMENTS** - Vous pouvez envoyer aussi peu que 1
satoshi (actuellement 0,0006 $).
* **VITESSE** - Il faut généralement entre une milliseconde et
quelques secondes pour recevoir un paiement.
* **VIE PRIVÉE** - Les transactions ne sont pas stockées sur la
blockchain bitcoin ouverte et publique. À certains égards, c'est encore
plus privé que l'argent liquide, car avec Lightning,
même l'autre partie ne sait pas nécessairement qui
vous êtes, car votre paiement ‘saute’ souvent à travers
différents canaux pour atteindre le destinataire.

Pour être clair, je ne dis pas qu'il est impossible à 100 % de
découvrir, mais beaucoup plus que pour les paiements sur la
chaîne principale de bitcoin.
Il faudrait une quantité immense de temps et d'énergie
pour établir avec certitude qui effectuait des paiements
à qui, et il ne serait pas toujours possible de
le faire du tout.

> **Profitez de visualisations étonnantes** de l'état actuel
>du Lightning Network à l'adresse suivante :
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*Bitcoin lui-même ne peut pas évoluer pour que chaque
transaction financière dans le
monde soit diffusée à tous et
incluse dans la blockchain.
Il doit y avoir un niveau secondaire de
systèmes de paiement qui soit plus léger
et plus efficace.*

*~ Hal Finney, 2010-12-30, premier cypherpunk
& la deuxième personne à exécuter Bitcoin*

**Voyez les choses de cette façon :**
>* Bitcoin : **Compte d'épargne** ~ Transactions plus lentes pour
>des montants plus importants.
>* Lightning : **Compte courant** ~ Transactions plus rapides
>pour des montants plus faibles.


>*Bitcoin amélioré par Lightning peut être considéré à la fois comme un
produit (propriété numérique) et un service (réseau monétaire ouvert). La capacité de transférer de l'énergie monétaire à travers
le temps et l'espace sans intervention gouvernementale ni
banque conventionnelle est extrêmement précieuse pour l'humanité.*

~ Michael Saylor, PDG
Microstrategy

**Pour en savoir plus sur Lightning, consultez :**

lopp.net/lightning-information.html

---
