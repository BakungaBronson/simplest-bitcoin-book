# लाइटनिंग नेटवर्क पर एक शब्द
* **बिटकॉइन ब्लॉक जानबूझकर छोटे होते हैं** (प्रत्येक 1MB),
जिसके परिणामस्वरूप बिटकॉइन मेनचेन लगभग 7 लेनदेन प्रति सेकंड (TPS) संसाधित करने में सक्षम है।
* वीज़ा लगभग 24,000 TPS संसाधित करता है।
* इसके अलावा, **आमतौर पर मेनचेन पर पहले पुष्टिकरण को पूरा होने में लगभग 10 मिनट लगते हैं** (क्योंकि एक ब्लॉक का खनन औसतन हर ~10 मिनट में किया जाता है)।
* यदि आप किसी स्टोर पर हैं और अपने सामान के लिए जल्दी से भुगतान करना चाहते हैं तो यह व्यावहारिक नहीं है।

> ***महत्वपूर्ण विवरण:** ब्लॉक के छोटे होने का कारण यह है कि **टाइमचेन को इतना छोटा रखना है कि कोई भी घर पर अपना नोड चला सके, जो नेटवर्क को विकेंद्रीकृत रखने में मदद करता है।** सातोशी ने इसके महत्व को समझा

>*बिटकॉइन उपयोगकर्ता चेन के आकार को सीमित करने के बारे में तेजी से
तानाशाहीपूर्ण हो सकते हैं ताकि बहुत सारे उपयोगकर्ताओं
और छोटे उपकरणों के लिए यह आसान हो।*

~ सातोशी नाकामोतो, 2010-12-10

**अनुशंसित पठन:**
* जोनाथन बीयर द्वारा ब्लॉकसाइज़ वार
---

>* प्रवेश करें, **लाइटनिंग नेटवर्क (LN),** एक **लेयर 2 बिटकॉइन
>स्केलिंग समाधान।**
>* **'लेयर 2'** का अर्थ है **यह बिटकॉइन के ऊपर बनाया गया है।**
>* **'स्केलिंग समाधान'** का अर्थ है कि यह नेटवर्क को इसकी अनुमति देता है:
>* ** प्रसंस्करण की गति को बहुत बढ़ाना।**
>* ** लेनदेन की संख्या में बहुत वृद्धि करना जिसे वह
>प्रति सेकंड संसाधित कर सकता है।**
>* **माइक्रोपेमेंट को संभव बनाना।**

* लाइटनिंग नेटवर्क को (कुछ हद तक) उस टैब की तरह माना जाता है जिसे आप बार में कुछ दोस्तों के साथ रखते हैं।
* आप सभी के बीच ट्रैक रखते हैं कि कौन क्या बकाया है
(जैसे लाइटनिंग नेटवर्क चैनल), और रात के अंत में आपका समूह बारमैन के साथ समझौता करता है
('मेनचेन')।
* **हालांकि, लाइटनिंग चैनल मुख्य श्रृंखला पर 'निपटान' होने से पहले दिनों, हफ्तों, महीनों या वर्षों तक खुले रह सकते हैं।**

---
## के लाभ:
* **मात्रा** - प्रति सेकंड लेनदेन की मात्रा
अनिवार्य रूप से असीमित है, क्योंकि एक ही समय में अनगिनत चैनल खोले जा सकते हैं, जिनमें से प्रत्येक अपना
'टैब' रखता है।
* **माइक्रोपेमेंट** - आप 1 सतोशी ($0.0006 वर्तमान में) जितना कम भेज सकते हैं।
* **गति** - भुगतान प्राप्त करने में आमतौर पर एक मिलीसेकंड और कुछ सेकंड लगते हैं।
* **गोपनीयता** - लेनदेन खुले, सार्वजनिक बिटकॉइन ब्लॉकचेन पर संग्रहीत नहीं हैं। कुछ मायनों में यह नकदी से भी अधिक निजी है, क्योंकि लाइटनिंग के साथ, यहां तक ​​कि दूसरे पक्ष को भी यह नहीं पता होता कि आप कौन हैं, क्योंकि आपका भुगतान अक्सर रिसीवर तक पहुंचने के लिए विभिन्न चैनलों के माध्यम से 'कूदता' है।

स्पष्ट होने के लिए, मैं यह नहीं कह रहा हूं कि इसे उजागर करना 100% असंभव है, बस बिटकॉइन मेनचेन पर भुगतान की तुलना में बहुत अधिक है।
भुगतान कौन कर रहा था, यह निश्चित रूप से स्थापित करने में बहुत अधिक समय और ऊर्जा लगेगी, और ऐसा करना हमेशा संभव नहीं होगा।

>**लाइटनिंग नेटवर्क की वर्तमान स्थिति के अद्भुत दृश्यों का आनंद लें:**
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*बिटकॉइन स्वयं हर
एक वित्तीय लेनदेन को दुनिया में प्रसारित करने और
ब्लॉकचेन में शामिल करने के लिए स्केल नहीं कर सकता है।
भुगतान प्रणालियों का एक द्वितीयक स्तर होना चाहिए जो हल्का
वजन वाला और अधिक कुशल हो।*

*~ हाल फ़िनी, 2010-12-30, अर्ली साइफ़रपंक
और बिटकॉइन चलाने वाले दूसरे व्यक्ति*

**इसे इस तरह समझें:**
>* बिटकॉइन: **बचत खाता** ~ बड़ी राशि के लिए धीमी लेनदेन।
>* लाइटनिंग: **चेकिंग खाता** ~ छोटी राशि के लिए तेज़ लेनदेन।


>*लाइटनिंग द्वारा संवर्धित बिटकॉइन को एक उत्पाद (डिजिटल संपत्ति) और एक सेवा (खुला मौद्रिक नेटवर्क) दोनों के रूप में देखा जा सकता है। सरकारी हस्तक्षेप या
पारंपरिक बैंकिंग के बिना समय और स्थान के माध्यम से मौद्रिक ऊर्जा स्थानांतरित करने की क्षमता मानवता के लिए बहुत मूल्यवान है।*

~ माइकल सायलर, सीईओ
माइक्रोस्ट्रेटजी

**लाइटनिंग के बारे में यहाँ और जानें:**

lopp.net/lightning-information.html

---
