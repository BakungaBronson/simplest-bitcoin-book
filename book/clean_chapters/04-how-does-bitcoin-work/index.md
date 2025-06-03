# HOW DOES Bitcoin WORK?

Rules not Rulers

tik-tok/
/next block
* Bitcoin uses proof-of-work, public-key cryptography
and peer-to-peer networking, to process and verify
payments in a global, distributed, online ledger.

>**Cryptography** (noun) /krɪpˈtɑːɡrəfi
>
>*: the enciphering and deciphering of messages
>in secret code or cipher
>: the computerized encoding and
>decoding of information*

~ Merriam Webster Dictionary

>**Hashing** (verb) /ˈhæʃɪŋ/
>
>*: a method of encryption
>: the process of using a mathematical algorithm against
>data to produce a numeric value (a hash digest)
>that is representative of that data.*

~ crsc.nist.gov

>**Remember:**
>
>The bitcoin ecosystem includes >>
>
>**bitcoin:** the digital **monetary asset**
>
>**Bitcoin:** the **payment network** of miners and nodes

1 bitcoin = 100,000,000 satoshis (sats)

**(You can buy sats, a fraction of a bitcoin)**

---

>*We define an electronic coin as a chain of
digital signatures. Each owner transfers
the coin to the next by digitally signing
a hash of the previous transaction and the
public key of the next owner and adding
these to the end of the coin. A payee can
verify the signatures to verify the chain
of ownership.*

~ Satoshi Nakamoto
Bitcoin White Paper, Pt.2, 2008
Describing how a bitcoin transaction works
in the distributed ledger

---
## THE BITCOIN ECOSYSTEM..
**consists of Miners, Nodes, Users, Developers**

all working independently,

and simultaneously interdependently,

to enliven that which is

BITCOIN!

![bitcoin](figure-06-m-u-n-d.png)

---
## MINERS
* **Specialized nodes** (computers called ASICS) **that
‘mine’ the blocks** that become part of the bitcoin
blockchain.
* In so doing, they **verify the validated transactions
made by users, mint new bitcoins** and **secure
the entire network.**

## USERS
* **You and me. All of us.** The people.
* Acknowledging and appreciating the value of
goods and services provided, we transact: give
and receive bitcoin, or we store it for use later, as
needed.

## NODES 
* **Nodes are computers that run the bitcoin
software.**
* **There are thousands of nodes** making up the
decentralized, global, voluntary **network that
validates transactions** (thereby preventing
double-spending, and helping to secure the
system).

## DEVELOPERS (DEVS)
* **Coders, programmers & digital authors** who work
to **maintain and scale the network, improve security,
privacy and user interface, and translate code** into
language and visuals that the rest of us can comprehend and utilize

---

## A BITCOIN TRANSACTION:
Ali wants to send Benji some bitcoin:

>1. Ali **opens the bitcoin wallet** app on her phone and
>**clicks ‘Send’.**
>2. Benji **opens his wallet app** and **clicks ‘Receive’.**
>3. **If they are together:** Ali scans the QR code on the
>wallet app on Benji’s phone.
>4. **If they are not together:** Ali copies and pastes the
>address Benji texts her, into the address field in her
>wallet.
>5. Ali **enters the amount to send,** and hits **‘Send’.**
>6. **A few seconds later,** Benji will see the amount
>pending in his wallet.
>7. **If it was sent through Lightning** it will be confirmed
>almost instantly, and is almost free.
>8. **If it was sent ‘onchain’** (on the Bitcoin mainchain),
>it includes a small fee, and usually takes around 10
>minutes to be confirmed. It can take longer,
>depending on network traffic.

---

## A BITCOIN TRANSACTION UNDER THE HOOD: 
(Definitions of the terms that are **in bold** follow)

>1. When Ali sends those sats to Benji, the payment
>**transaction** is **broadcast** to the network.
>2. The transaction gets validated by **nodes** that
>make sure Ali really has the bitcoin to send, and
>that it has not previously been spent (to prevent
>double-spending) .
>3. Once validated by a node, it waits in the **mempool**
>with other peoples' transactions.
>4. The transactions in the mempool get added in a
>block to the **blockchain** when a **miner** finds a >**nonce**
>that satisfies the **difficulty algorithm.**
>5. Each **block** has a **timestamp.**
>6. This creates **immutability,** and helps protect the
>difficulty algorithm adjustment from being
>manipulated.
>7. Each block represents one confirmation for the
>transactions included in it.
>8. As blocks are added, on average every ten mins,
>the immutability of the blockchain increases.

---

## GLOSSARY OF TERMS

---
>* **TRANSACTION ~ Sending/receiving bitcoin**
---
* A transfer of value in the form of satoshis, from
one bitcoin holder to another.

---
>* **NODE ~ A ‘branch’ of the decentralized bitcoin
‘bank’. Anyone can run a node.**
---

* Nodes are computers that run the bitcoin
software.
* Nodes, along with miners, users and
developers, form the peer-to-peer Bitcoin
network.
* Imagine **each full node as a ledger containing the
balances of every private key.**
* They interact, and reach consensus (agree) with
one another by accepting and validating
transactions from other nodes, along with blocks
from miners, and then relaying these onward to
other nodes.
* Nodes are run by an ad-hoc group of thousands
of volunteers around the world.
* A full node is one that has independently
validated the entire Bitcoin blockchain, since the
Genesis Block mined by Satoshi in 2009.
* The more active nodes there are, the more distributed, and therefore resilient, the whole network
becomes.
* There are **currently over 19,000 reachable full
nodes worldwide, & far more unreachable ones.**
* All participating nodes are equal.

---

---
>* **BROADCAST ~ Letting the network know you are
sending bitcoin to someone.**
---

* When you click ‘Send’, your wallet signs the transaction with your private key and broadcasts it,
letting all the other nodes know of your intention
to transfer value so that they can validate the
transaction

---
>* **MEMPOOL ~ A transaction waiting room**
---

* This is the ‘waiting room’ where validated transactions are sent to be picked up by a miner and
added to a block.

---
>* **BLOCK ~ A ‘page’ in the bitcoin ledger**
---

* The Bitcoin distributed ledger is made up of digital ‘blocks’.
* Each block contains verified bitcoin transactions
that keep the global ledger accurate and current.
They also contain the nonce, a time-stamp and a
hash of the previous block, all of which
contribute to the immutability of the bitcoin
blockchain.

---
>* **BLOCKCHAIN ~ The whole bitcoin ledger**
---

* The bitcoin blockchain, also known as the
timechain, is the distributed ledger that contains
every block, and every bitcoin transaction ever
made since the Genesis block was mined by
Satoshi in 2009.

---

---
>* **MINER ~ A specialized node that both confirms
transactions and issues new bitcoins**
---

* Bitcoin miners are specialized computers. They
direct lots of computing power (hashrate) in a
digital lottery to guess a number that will satisfy
the current difficulty algorithm, thereby ‘mining’
a ‘block’ (a piece of the ledger).
* A mined block is timestamped and added to the
blockchain (aka timechain).

---
>* **DIFFICULTY ALGORITHM ~ A special, adaptive
design that helps keep new bitcoin issuance
predictable.**
---

* This was one of Satoshi’s genius solutions to help
protect the bitcoin issuance from outrunning itself,
as more advanced computers are developed.
* When more miners come online, the target number (nonce) in the ‘lottery’ gets smaller, and therefore more difficult to find.
* When less miners are online, it gets easier.
* The algorithm **adjusts automatically every 2016
blocks** (about every two weeks), to ensure a predictable rate of supply, where one block is mined
on average every ten minutes.

---
>* **NONCE ~ A 32-bit random number**
---

* A 32-bit random number that miners add to the
end of the hashed list of transactions, to attempt
to satisfy the difficulty target to mine a block.
* When a miner finds a nonce that leads to
generating a hash below the current target
number, they have mined a block and get to add
it to the blockchain and claim the bitcoin block
reward.
---

---
>* **TIMESTAMP ~ Stamps the time**
---

* Every block mined has a timestamp added to it.
* This is for added security, immutability and to help
establish the difficulty adjustment

---
>* **IMMUTABILITY ~ Cannot be changed.**
---

* This means the blockchain is ‘set in digital stone’.

---
>* **PROOF-OF-WORK (PoW) ~ Cryptographic proof
that difficult work was done to satisfy an algorithm.**
---

*  Miners use the PoW algorithm to prove they have
used a lot of computational power via electricity
(work), in order to achieve consensus in a decentralized manner, and to prevent corrupt actors
from spamming the network.

---
>* **PUBLIC KEY CRYPTOGRAPHY ~ A process that
creates the digital keys to access your bitcoins**
---

* This is a system whereby two keys are created
through a cryptographic algorithm.
* **One key is public** - Like your bank account number, that you can give people to send bitcoin to
you for goods, gifts or services.
* **The other key is private** - Only you have a copy,
and you use it to unlock access to your bitcoin,
just as a password unlocks your online bank
account.
* **You must secure your private key very well,**
since anyone who has access to it has access to
your bitcoin.

---

---
>* **PEER-TO-PEER (P2P) NETWORK ~ A decentralized
network with no middlemen**
---

* Full nodes (peers) collaboratively maintain a peerto-peer network for transaction and block validation and verification.
* In this type of network, each node is able to
both provide/request data to/from its peers.
* There are no gatekeepers in a P2P network.

---
>* **LIGHTNING NETWORK ~ A network built on bitcoin that makes it possible to send or receive
sats very fast and almost for free.**
---

* Lightning is a Layer 2 scaling solution. This means
it provides a way for bitcoin to scale, giving it the
potential to process millions of transactions per
second (TPS).

---
>* **WALLET ~ A ‘wallet’ holds the cryptographic
keys to access your bitcoin.**
---

* It can be on a phone, computer or on a separate
small hardware device (the safest).
* A bitcoin wallet would more accurately be called a
signing device. Your bitcoin never actually leaves
the blockchain, the digital ledger.
* When you wish to send or spend your bitcoin, the
wallet will sign and broadcast the transaction to
the network, so that it can be validated and
added into a block on the blockchain.

---
>* **DEVELOPERS ~ Computer programmers**
---

* Cypherpunks/programmers that maintain the network, improve security, check for bugs, submit
pull requests (for new updates or features), review
pull requests, audit the code.

---

---
>* **PUBLIC KEY ~ Like a bank account number for
receiving bitcoin.**
---

* You can give it to people to send you bitcoin,
just like you would give your account number to
someone so they can send you fiat

---
>* **PRIVATE KEY ~ For securing, accessing and sending bitcoin, like the key to a safety deposit box.**
---

* A bitcoin private key is a secret string of numbers
and letters that allows you to send/spend your
bitcoin.
* Only you have a copy. ** **It is very important to
keep it very safe and secure, as anyone who
obtains a copy can spend your bitcoin.** **

---
>* **DISTRIBUTED LEDGER ~ A ledger maintained by
everyone who wishes to help maintain it.**
---

* Instead of a centrally-controlled ledger that is
invisible to the public, like one that a bank maintains, Bitcoin is a transparent, open, decentralized
ledger visible to anyone, anytime.
* The addresses are strings of letters and numbers,
with no names attached.
* While pseudonymous, it is possible to track transactions, especially if the bitcoin was bought from
a centralized KYC exchange.
* The Bitcoin network is trustless and anyone can
audit it anytime, unlike a bank where one must
trust that the ledgers are being kept honestly.

---

## MORE ON MINING
![whatsminer](figure-07-whatsminer.png) Whatsminer M50S

![Antminer](figure-08-Antminer.png) Antminer S21 Pro

![Bitaxe](figure-09-Bitaxe%20.png)  Bitaxe 401 Supra

* **Miners devote computing power AKA hashrate,
via electricity to the network,** to add blocks to the
Bitcoin blockchain.
* These computers run 24 hours a day, usually in sets
of a few, to a few hundred or thousand.
* **They are basically running a lottery. When one of
them guesses a number** (the nonce) that generates a
hash that satisfies the current difficulty target, **they
get to add the next block to the timechain.**
* **All the above is the proof-of-work (PoW) needed to
birth new bitcoins.**

---

## BITCOIN BLOCK REWARD 
**= Subsidy + Fees**

>* **For their work, miners get:**
> * **A subsidy, in the form of freshly minted bitcoins.**
> * **Plus, the fees from the verified transactions
>included in that block**

* **When you send bitcoin to someone, that transaction
includes a fee** and needs to be verified by a miner,
and then included in a block.
* The **bitcoin block subsidy** gets cut in half every four
years
* It is **currently 3.125 bitcoin** per block that is mined.
* **The next ‘halving’ will be in 2028,** at which point
the block reward will drop to 1.5625 bitcoin per
block mined.
* As mentioned before, **this keeps the issuance stable.**
* **In the year 2140, the last piece of bitcoin will be
mined.**
* After that, miners will only get the fees from the transactions they verify in each block.

>*In a few decades when the reward gets too
small, the transaction fee will become the
main compensation for nodes (miners).*

~ Satoshi Nakamoto
Bitcointalk.org, 2010-02-14

>* **Miners will always be needed to verify transactions,
thereby keeping the network updated and secure.**

* While one needs to be aware that there are costs
involved, and profitability is negligible for home
miners, it is a powerful way to help secure and keep
the network decentralized.
* Miners last quite a few years. There are currently many
Antminer S9’s for example, that have been running
for over 6 years.
* When miners are retired **they can easily be taken
apart and recycled.**
* **Tons of fascinating innovation is happening,** with
people using the excess heat from miners to
heat their homes, saunas, greenhouses, hot tubs,
dry jerky and vegetables, heat decks, dry wood and
more!

---
