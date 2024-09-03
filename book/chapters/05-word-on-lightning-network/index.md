# A WORD ON THE LIGHTNING NETWORK
* **Bitcoin blocks are intentionally small*** (1MB each),
resulting in the bitcoin mainchain being able to process about 7 transactions per second (TPS).
* Visa processes about 24,000 TPS.
* Also, **it generally takes about 10 minutes for the
first confirmation to go through on a mainchain
transaction** (since a block is mined on
average every ~10 minutes).
* This is not practical if you are at a store and want to
make a quick payment for your goods.

> ***Important Detail:** The reason the blocks are small,
is to keep **the timechain small enough for anyone to
run their own node at home, which helps keep the
network decentralized.** Satoshi realized the
importance of this

>*Bitcoin users might get increasingly
tyrannical about limiting the size of
the chain so it’s easy for lots of users
and small devices.*

~ Satoshi Nakamoto, 2010-12-10

**Recommended Reading:**
* The Blocksize War by Jonathan Bier
---

>* Enter, the **Lightning Network (LN),** a **Layer 2 bitcoin
>scaling solution.**
>* **‘Layer 2’** means **it is built on top of bitcoin.**
>* **‘Scaling Solution’** means it allows the network to:
>* ** Vastly increase the speed of processing.**
>* **Vastly increase the number of transactions it
>can process per second.**
>* **Make micropayments possible.**

* The Lightning Network can be (sort of) thought of like
a tab you might keep with some friends at the bar.
* You keep track between all of you who owes what
(like a Lightning Network channel), and at the end
of the night your group settles with the barman
(‘the mainchain’).
* **Lightning channels, however, can stay open for
days, weeks, months or years before being
‘settled’ on the mainchain.**

---
## BENEFITS OF :
* **VOLUME** - The volume of transactions per second is
in essence limitless, as countless channels can be
opened at the same time, each keeping their own
‘tab’.
* **MICROPAYMENTS** - You can send as little as 1
satoshi (currently $0.0006).
* **SPEED** - It usually takes between a millisecond and a
few seconds to receive a payment.
* **PRIVACY** - Transactions are not stored on the open,
public bitcoin blockchain. In some ways it is even
more private than cash, because with Lightning,
even the other party does not necessarily know who
you are, as your payment often ‘hops’ through
different channels to reach the receiver.

To be clear, I am not saying it is 100% impossible to
uncover, just far more so than with payments on the
bitcoin mainchain.
It would take an immense amount of time and energy
to establish with certainty who was making payments
to whom, and it would not always be possible to
do so at all.

>**Enjoy amazing visualizations** of the current state
>of the Lightning Network at:
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*Bitcoin itself cannot scale to have every
single financial transaction in the
world be broadcast to everyone and
included in the blockchain.
There needs to be a secondary level of
payment systems which is lighter
weight and more efficient.*

*~ Hal Finney, 2010-12-30, Early cypherpunk
& the second person to run Bitcoin*

**Think of it like this:**
>* Bitcoin: **Savings Account** ~ Slower transactions for
>larger amounts.
>* Lightning: **Checking Account** ~ Faster transactions
>for smaller amounts.


>*Bitcoin enhanced by Lightning can be viewed as both a
product (digital property) and a service (open monetary
network). The ability to transfer monetary energy through
time and space without government intervention or
conventional banking is enormously valuable to humanity.*

~ Michael Saylor, CEO
Microstrategy

**Learn more about Lightning here:**

lopp.net/lightning-information.html

---

