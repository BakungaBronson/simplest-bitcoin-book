# BAGAIMANA Bitcoin BEKERJA?

Aturan, Bukan Penguasa

tik-tok/
/blok berikutnya
* Bitcoin menggunakan proof-of-work, kriptografi kunci publik
dan jaringan peer-to-peer, untuk memproses dan memverifikasi
pembayaran dalam buku besar daring global yang terdistribusi.

>**Kriptografi** (kata benda) /krɪpˈtɑːɡrəfi
>
>*: penyandian dan penguraian pesan
>dalam kode rahasia atau sandi
>: pengkodean dan
>dekode informasi terkomputerisasi*

~ Kamus Merriam Webster

>**Hashing** (kata kerja) /ˈhæʃɪŋ/
>
>*: metode enkripsi
>: proses penggunaan algoritma matematika terhadap
>data untuk menghasilkan nilai numerik (hash digest)
>yang mewakili data tersebut.*

~ crsc.nist.gov

>**Ingat:**
>
>Ekosistem bitcoin mencakup >>
>
>**bitcoin:** **aset moneter** digital
>
>**Bitcoin:** **jaringan pembayaran** penambang dan node

1 bitcoin = 100.000.000 satoshi (sats)

**(Anda dapat membeli sats, sebagian kecil dari bitcoin)**

---

>*Kami mendefinisikan koin elektronik sebagai rantai
tanda tangan digital. Setiap pemilik mentransfer
koin ke pemilik berikutnya dengan menandatangani secara digital
hash dari transaksi sebelumnya dan
kunci publik pemilik berikutnya dan menambahkan
ini ke ujung koin. Penerima pembayaran dapat
memverifikasi tanda tangan untuk memverifikasi rantai
kepemilikan.*

~ Satoshi Nakamoto
Buku Putih Bitcoin, Bag.2, 2008
Menjelaskan cara kerja transaksi bitcoin
dalam buku besar terdistribusi

---
## EKOSISTEM BITCOIN..
**terdiri dari Penambang, Node, Pengguna, Pengembang**

semua bekerja secara mandiri,

dan secara bersamaan saling bergantung,

untuk menghidupkan apa yang ada

BITCOIN!

![bitcoin](figure-06-m-u-n-d.png)

---
## PENAMBANG
* **Node khusus** (komputer yang disebut ASICS) **yang
'menambang' blok** yang menjadi bagian dari bitcoin
blockchain.
* Dengan demikian, mereka **memverifikasi transaksi yang divalidasi
yang dilakukan oleh pengguna, mencetak bitcoin baru** dan **mengamankan
seluruh jaringan.**

## PENGGUNA
* **Anda dan saya. Kita semua.** Orang-orang.
* Menyadari dan menghargai nilai dari
barang dan jasa yang diberikan, kita bertransaksi: memberi
dan menerima bitcoin, atau kita menyimpannya untuk digunakan nanti, sebagaimana
dibutuhkan.

## NODE
* **Node adalah komputer yang menjalankan bitcoin
perangkat lunak.**
* **Ada ribuan node** yang membentuk
terdesentralisasi, global, sukarela **jaringan yang
memvalidasi transaksi** (dengan demikian mencegah
pembelanjaan ganda, dan membantu mengamankan
sistem).

## PENGEMBANG (DEVS)
* **Coder, pemrogram & penulis digital** yang bekerja
untuk **memelihara dan menskalakan jaringan, meningkatkan keamanan,
privasi dan antarmuka pengguna, dan menerjemahkan kode** ke dalam
bahasa dan visual yang dapat dipahami dan dimanfaatkan oleh kita semua

---

## SEBUAH TRANSAKSI BITCOIN:
Ali ingin mengirimkan beberapa bitcoin kepada Benji:

>1. Ali **membuka aplikasi dompet bitcoin** di ponselnya dan
>**klik 'Kirim'.**
>2. Benji **membuka aplikasi dompetnya** dan **klik 'Terima'.**
>3. **Jika mereka bersama:** Ali memindai kode QR di
>aplikasi dompet di ponsel Benji.
>4. **Jika mereka tidak bersama:** Ali menyalin dan menempel
>alamat yang dikirimkan Benji kepadanya melalui teks, ke dalam bidang alamat di miliknya
>dompet.
>5. Ali **memasukkan jumlah yang akan dikirim,** dan menekan **'Kirim'.**
>6. **Beberapa detik kemudian,** Benji akan melihat jumlah
>tertunda di dompetnya.
>7. **Jika dikirim melalui Lightning** itu akan dikonfirmasi
>hampir seketika, dan hampir gratis.
>8. **Jika dikirim 'onchain'** (di rantai utama Bitcoin),
>itu termasuk biaya kecil, dan biasanya membutuhkan waktu sekitar 10
>menit untuk dikonfirmasi. Mungkin perlu waktu lebih lama,
>tergantung pada lalu lintas jaringan.

---

## TRANSAKSI BITCOIN DI BAWAH KAP:
(Definisi istilah yang **dicetak tebal** menyusul)

>1. Ketika Ali mengirimkan sats tersebut ke Benji, pembayaran
>**transaksi** adalah **siaran** ke jaringan.
>2. Transaksi tersebut divalidasi oleh **node** yang
>memastikan Ali benar-benar memiliki bitcoin untuk dikirim, dan
>bahwa itu belum pernah dibelanjakan sebelumnya (untuk mencegah
>pembelanjaan ganda).
>3. Setelah divalidasi oleh sebuah node, ia menunggu di **mempool**
>dengan transaksi orang lain.
>4. Transaksi di mempool ditambahkan dalam sebuah
>blok ke **blockchain** ketika **penambang** menemukan sebuah >**nonce**
>yang memenuhi **algoritma kesulitan.**
>5. Setiap **blok** memiliki **cap waktu.**
>6. Ini menciptakan **kekekalan,** dan membantu melindungi
>penyesuaian algoritma kesulitan dari
>dimanipulasi.
>7. Setiap blok mewakili satu konfirmasi untuk
>transaksi yang termasuk di dalamnya.
>8. Saat blok ditambahkan, rata-rata setiap sepuluh menit,
>kekekalan blockchain meningkat.

---

## DAFTAR ISTILAH

---
>* **TRANSAKSI ~ Mengirim/menerima bitcoin**
---
* Transfer nilai dalam bentuk satoshi, dari
satu pemegang bitcoin ke yang lain.

---
>* **NODE ~ Sebuah 'cabang' dari bitcoin yang terdesentralisasi
'bank'. Siapa pun dapat menjalankan sebuah node.**
---

* Node adalah komputer yang menjalankan bitcoin
perangkat lunak.
* Node, bersama dengan penambang, pengguna dan
pengembang, membentuk Bitcoin peer-to-peer
jaringan.
* Bayangkan **setiap node penuh sebagai buku besar yang berisi
saldo setiap kunci pribadi.**
* Mereka berinteraksi, dan mencapai konsensus (setuju) dengan
satu sama lain dengan menerima dan memvalidasi
transaksi dari node lain, bersama dengan blok
dari penambang, dan kemudian menyampaikan ini ke depan ke
node lain.
* Node dijalankan oleh sekelompok relawan ad-hoc yang berjumlah ribuan
di seluruh dunia.
* Node penuh adalah node yang secara independen
memvalidasi seluruh blockchain Bitcoin, sejak
Genesis Block ditambang oleh Satoshi pada tahun 2009.
* Semakin banyak node aktif, semakin terdistribusi, dan oleh karena itu tangguh, seluruh jaringan
menjadi.
* Saat ini **ada lebih dari 19.000 node penuh yang dapat dijangkau
di seluruh dunia, & jauh lebih banyak yang tidak dapat dijangkau.**
* Semua node yang berpartisipasi adalah sama.

---

---
>* **SIARAN ~ Memberi tahu jaringan bahwa Anda
mengirim bitcoin ke seseorang.**
---

* Ketika Anda mengklik 'Kirim', dompet Anda menandatangani transaksi dengan kunci pribadi Anda dan menyiarkannya,
memberi tahu semua node lain tentang niat Anda
untuk mentransfer nilai sehingga mereka dapat memvalidasi
transaksi

---
>* **MEMPOOL ~ Ruang tunggu transaksi**
---

* Ini adalah 'ruang tunggu' tempat transaksi yang divalidasi dikirim untuk diambil oleh penambang dan
ditambahkan ke blok.

---
>* **BLOK ~ Sebuah 'halaman' dalam buku besar bitcoin**
---

* Buku besar terdistribusi Bitcoin terdiri dari 'blok' digital.
* Setiap blok berisi transaksi bitcoin terverifikasi
yang menjaga buku besar global tetap akurat dan terkini.
Mereka juga berisi nonce, stempel waktu dan
hash dari blok sebelumnya, yang semuanya
berkontribusi pada kekekalan bitcoin
blockchain.

---
>* **BLOCKCHAIN ~ Seluruh buku besar bitcoin**
---

* Blockchain bitcoin, juga dikenal sebagai
timechain, adalah buku besar terdistribusi yang berisi
setiap blok, dan setiap transaksi bitcoin yang pernah
dibuat sejak blok Genesis ditambang oleh
Satoshi pada tahun 2009.

---

---
>* **PENAMBANG ~ Node khusus yang mengonfirmasi
transaksi dan menerbitkan bitcoin baru**
---

* Penambang Bitcoin adalah komputer khusus. Mereka
mengarahkan banyak daya komputasi (hashrate) dalam
lotre digital untuk menebak angka yang akan memenuhi
algoritma kesulitan saat ini, dengan demikian 'menambang'
sebuah 'blok' (sepotong buku besar).
* Blok yang ditambang diberi stempel waktu dan ditambahkan ke
blockchain (alias timechain).

---
>* **ALGORITMA KESULITAN ~ Khusus, adaptif
desain yang membantu menjaga penerbitan bitcoin baru
dapat diprediksi.**
---

* Ini adalah salah satu solusi jenius Satoshi untuk membantu
melindungi penerbitan bitcoin agar tidak melampaui dirinya sendiri,
karena komputer yang lebih canggih sedang dikembangkan.
* Ketika lebih banyak penambang online, nomor target (nonce) dalam 'lotre' menjadi lebih kecil, dan oleh karena itu lebih sulit ditemukan.
* Ketika lebih sedikit penambang online, itu menjadi lebih mudah.
* Algoritma **menyesuaikan secara otomatis setiap 2016
blok** (kira-kira setiap dua minggu), untuk memastikan tingkat pasokan yang dapat diprediksi, di mana satu blok ditambang
rata-rata setiap sepuluh menit.

---
>* **NONCE ~ Angka acak 32-bit**
---

* Angka acak 32-bit yang ditambahkan penambang ke
akhir daftar transaksi yang di-hash, untuk dicoba
untuk memenuhi target kesulitan untuk menambang blok.
* Ketika penambang menemukan nonce yang mengarah ke
menghasilkan hash di bawah target saat ini
angka, mereka telah menambang blok dan dapat menambahkannya
itu ke blockchain dan klaim hadiah blok bitcoin.
---

---
>* **CAP WAKTU ~ Menempelkan waktu**
---

* Setiap blok yang ditambang memiliki stempel waktu yang ditambahkan ke dalamnya.
* Ini untuk keamanan tambahan, kekekalan dan untuk membantu
menetapkan penyesuaian kesulitan

---
>* **KEKEKALAN ~ Tidak dapat diubah.**
---

* Ini berarti blockchain 'terukir dalam batu digital'.

---
>* **PROOF-OF-WORK (PoW) ~ Bukti kriptografi
bahwa pekerjaan sulit dilakukan untuk memenuhi algoritma.**
---

* Penambang menggunakan algoritma PoW untuk membuktikan bahwa mereka memiliki
menggunakan banyak daya komputasi melalui listrik
(pekerjaan), untuk mencapai konsensus dalam terdesentralisasi
cara, dan untuk mencegah pelaku korup
dari mengirim spam ke jaringan.

---
>* **KRIPTOGRAFI KUNCI PUBLIK ~ Proses yang
menciptakan kunci digital untuk mengakses bitcoin Anda**
---

* Ini adalah sistem di mana dua kunci dibuat
melalui algoritma kriptografi.
* **Satu kunci bersifat publik** - Seperti nomor rekening bank Anda, yang dapat Anda berikan kepada orang untuk mengirim bitcoin ke
Anda untuk barang, hadiah atau layanan.
* **Kunci lainnya bersifat pribadi** - Hanya Anda yang memiliki salinan,
dan Anda menggunakannya untuk membuka akses ke bitcoin Anda,
sama seperti kata sandi membuka bank online Anda
akun.
* **Anda harus mengamankan kunci pribadi Anda dengan sangat baik,**
karena siapa pun yang memiliki akses ke sana memiliki akses ke
bitcoin Anda.

---

---
>* **JARINGAN PEER-TO-PEER (P2P) ~ Terdesentralisasi
jaringan tanpa perantara**
---

* Node penuh (peer) secara kolaboratif memelihara jaringan peer-to-peer untuk validasi dan verifikasi transaksi dan blok.
* Dalam jenis jaringan ini, setiap node mampu
baik menyediakan/meminta data ke/dari peer-nya.
* Tidak ada penjaga gerbang di jaringan P2P.

---
>* **JARINGAN LIGHTNING ~ Jaringan yang dibangun di atas bitcoin yang memungkinkan untuk mengirim atau menerima
sats sangat cepat dan hampir gratis.**
---

* Lightning adalah solusi penskalaan Layer 2. Ini berarti
itu menyediakan cara bagi bitcoin untuk menskalakan, memberikannya
potensi untuk memproses jutaan transaksi per
detik (TPS).

---
>* **DOMPET ~ 'Dompet' memegang kriptografi
kunci untuk mengakses bitcoin Anda.**
---

* Itu bisa di telepon, komputer atau di terpisah
perangkat perangkat keras kecil (yang paling aman).
* Dompet bitcoin akan lebih akurat disebut
perangkat penandatanganan. Bitcoin Anda tidak pernah benar-benar pergi
blockchain, buku besar digital.
* Ketika Anda ingin mengirim atau membelanjakan bitcoin Anda,
dompet akan menandatangani dan menyiarkan transaksi ke
jaringan, sehingga dapat divalidasi dan
ditambahkan ke dalam blok di blockchain.

---
>* **PENGEMBANG ~ Pemrogram komputer**
---

* Cypherpunks/pemrogram yang memelihara jaringan, meningkatkan keamanan, memeriksa bug, mengirimkan
tarik permintaan (untuk pembaruan atau fitur baru), tinjau
tarik permintaan, audit kode.

---

---
>* **KUNCI PUBLIK ~ Seperti nomor rekening bank untuk
menerima bitcoin.**
---

* Anda dapat memberikannya kepada orang-orang untuk mengirimi Anda bitcoin,
sama seperti Anda akan memberikan nomor rekening Anda kepada
seseorang sehingga mereka dapat mengirimi Anda uang fiat

---
>* **KUNCI PRIBADI ~ Untuk mengamankan, mengakses, dan mengirim bitcoin, seperti kunci brankas.**
---

* Kunci pribadi bitcoin adalah string rahasia dari angka
dan huruf yang memungkinkan Anda mengirim/membelanjakan milik Anda
bitcoin.
* Hanya Anda yang memiliki salinan. ** **Sangat penting untuk
jaga agar tetap sangat aman dan terjamin, karena siapa pun yang
mendapatkan salinan dapat membelanjakan bitcoin Anda.** **

---
>* **BUKU BESAR TERDISTRIBUSI ~ Buku besar yang dikelola oleh
semua orang yang ingin membantu memeliharanya.**
---

* Alih-alih buku besar yang dikendalikan secara terpusat yang
tidak terlihat oleh publik, seperti yang dikelola oleh bank, Bitcoin adalah terpusat yang transparan dan terbuka
buku besar terlihat oleh siapa saja, kapan saja.
* Alamatnya adalah string huruf dan angka,
tanpa nama terlampir.
* Meskipun pseudonim, adalah mungkin untuk melacak transaksi, terutama jika bitcoin dibeli dari
pertukaran KYC terpusat.
* Jaringan Bitcoin tidak dapat dipercaya dan siapa pun dapat
audit setiap saat, tidak seperti bank di mana orang harus
percaya bahwa buku besar disimpan dengan jujur.

---

## LEBIH LANJUT TENTANG PENAMBANGAN
![whatsminer](figure-07-whatsminer.png) Whatsminer M50S

![Antminer](figure-08-Antminer.png) Antminer S21 Pro

![Bitaxe](figure-09-Bitaxe%20.png) Bitaxe 401 Supra

* **Penambang mencurahkan daya komputasi AKA hashrate,
melalui listrik ke jaringan,** untuk menambahkan blok ke
Blockchain Bitcoin.
* Komputer ini berjalan 24 jam sehari, biasanya dalam set
dari beberapa, hingga beberapa ratus atau ribu.
* **Mereka pada dasarnya menjalankan lotre. Ketika salah satu dari
mereka menebak angka** (nonce) yang menghasilkan
hash yang memenuhi target kesulitan saat ini, **mereka
bisa menambahkan blok berikutnya ke timechain.**
* **Semua di atas adalah proof-of-work (PoW) yang diperlukan untuk
melahirkan bitcoin baru.**

---

## HADIAH BLOK BITCOIN
**= Subsidi + Biaya**

>* **Untuk pekerjaan mereka, penambang mendapatkan:**
> * **Subsidi, dalam bentuk bitcoin yang baru dicetak.**
> * **Plus, biaya dari transaksi terverifikasi
>termasuk dalam blok itu**

* **Ketika Anda mengirim bitcoin ke seseorang, transaksi itu
termasuk biaya** dan perlu diverifikasi oleh penambang,
dan kemudian dimasukkan dalam blok.
* **Subsidi blok bitcoin** dipotong setengah setiap empat
tahun
* Saat ini **3.125 bitcoin** per blok yang ditambang.
* **'Halving' berikutnya akan terjadi pada tahun 2028,** di mana titik
hadiah blok akan turun menjadi 1.5625 bitcoin per
blok yang ditambang.
* Seperti yang disebutkan sebelumnya, **ini menjaga penerbitan tetap stabil.**
* **Pada tahun 2140, bagian terakhir dari bitcoin akan
ditambang.**
* Setelah itu, penambang hanya akan mendapatkan biaya dari transaksi yang mereka verifikasi di setiap blok.

>*Dalam beberapa dekade ketika hadiah menjadi terlalu
kecil, biaya transaksi akan menjadi
kompensasi utama untuk node (penambang).*

~ Satoshi Nakamoto
Bitcointalk.org, 2010-02-14

>* **Penambang akan selalu dibutuhkan untuk memverifikasi transaksi,
dengan demikian menjaga jaringan tetap terbarui dan aman.**

* Sementara orang perlu menyadari bahwa ada biaya
terlibat, dan profitabilitas dapat diabaikan untuk rumah
penambang, itu adalah cara yang ampuh untuk membantu mengamankan dan menjaga
jaringan terdesentralisasi.
* Penambang bertahan cukup lama. Saat ini ada banyak
Antminer S9 misalnya, yang telah berjalan
selama lebih dari 6 tahun.
* Ketika penambang dipensiunkan **mereka dapat dengan mudah diambil
pisah dan didaur ulang.**
* **Banyak inovasi menarik yang terjadi,** dengan
orang menggunakan panas berlebih dari penambang untuk
memanaskan rumah, sauna, rumah kaca, bak air panas,
dendeng kering dan sayuran, dek panas, kayu kering dan
lebih banyak lagi!

---
