# كلمة عن شبكة Lightning
* **كتل البيتكوين صغيرة عن قصد*** (1 ميجابايت لكل منها)،
مما يؤدي إلى قدرة سلسلة البيتكوين الرئيسية على معالجة حوالي 7 معاملات في الثانية (TPS).
* تعالج Visa حوالي 24,000 TPS.
* أيضاً، **يستغرق الأمر عمومًا حوالي 10 دقائق حتى يتم
التأكيد الأول على معاملة السلسلة الرئيسية** (لأن يتم تعدين كتلة في
المتوسط كل ~10 دقائق).
* هذا غير عملي إذا كنت في متجر وتريد
إجراء دفعة سريعة مقابل مشترياتك.

> ***تفصيل مهم:** السبب في صغر حجم الكتل،
هو للحفاظ على **سلسلة الوقت صغيرة بما يكفي لأي شخص
لتشغيل العقدة الخاصة به في المنزل، مما يساعد في الحفاظ على
الشبكة لامركزية.** أدرك ساتوشي
أهمية ذلك.

>*قد يصبح مستخدمو البيتكوين
مستبدين بشكل متزايد بشأن تحديد حجم
السلسلة بحيث يسهل على الكثير من المستخدمين
والأجهزة الصغيرة.*

~ ساتوشي ناكاموتو، 2010-12-10

**قراءة مُوصى بها:**
* حرب حجم الكتل بواسطة جوناثان بير
---

>* إليكم، **شبكة Lightning (LN)،** وهي **حل لتوسيع نطاق البيتكوين من الطبقة الثانية.**
>* **"الطبقة الثانية"** تعني **أنها مبنية على قمة البيتكوين.**
>* **"حل لتوسيع النطاق"** يعني أنه يسمح للشبكة بما يلي:
>* ** زيادة سرعة المعالجة بشكل كبير.**
>* **زيادة عدد المعاملات التي يمكنها
>معالجتها في الثانية بشكل كبير.**
>* **جعل المدفوعات الصغيرة ممكنة.**

* يمكن اعتبار شبكة Lightning (إلى حد ما) بمثابة
علامة تبويب قد تحتفظ بها مع بعض الأصدقاء في البار.
* تتتبع بينكم من يدين لمن
(مثل قناة شبكة Lightning)، وفي نهاية
الليلة تقوم مجموعتك بالتسوية مع ساقي الحانة
("السلسلة الرئيسية").
* **ومع ذلك، يمكن أن تظل قنوات Lightning مفتوحة لعدة
أيام أو أسابيع أو شهور أو سنوات قبل أن يتم
"تسويتها" على السلسلة الرئيسية.**

---
## فوائد:
* **الحجم** - حجم المعاملات في الثانية هو
في الأساس لا حدود له، حيث يمكن فتح عدد لا يحصى من القنوات في
نفس الوقت، مع الاحتفاظ بكل منها
"علامة تبويب".
* **المدفوعات الصغيرة** - يمكنك إرسال أقل من 1
ساتوشي (حاليًا 0.0006 دولارًا أمريكيًا).
* **السرعة** - يستغرق الأمر عادةً ما بين مللي ثانية وعدة
ثوانٍ لتلقي دفعة.
* **الخصوصية** - لا يتم تخزين المعاملات في
سلسلة كتل البيتكوين العامة المفتوحة. في بعض النواحي، هي أكثر
خصوصية من النقد، لأنه مع Lightning،
حتى الطرف الآخر لا يعرف بالضرورة من
أنت، حيث غالبًا ما "تقفز" دفعتك عبر
قنوات مختلفة للوصول إلى المستلم.

لكي نكون واضحين، أنا لا أقول إنه من المستحيل بنسبة 100٪
اكتشافها، ولكنها أكثر صعوبة من المدفوعات على
سلسلة البيتكوين الرئيسية.
سيستغرق الأمر قدرًا هائلاً من الوقت والطاقة
لتحديد على وجه اليقين من كان يسدد المدفوعات
لمن، ولن يكون من الممكن دائمًا
القيام بذلك على الإطلاق.

>**استمتع بتصورات مذهلة** للحالة الحالية
>لشبكة Lightning على:
>* lnrouter.app/graph
>* mempool.space/graphs/lightning/nodeschannels-map

---

>*لا يمكن للبيتكوين نفسه أن يتوسع بحيث تكون كل
معاملة مالية واحدة في
العالم يتم بثها للجميع
وتضمينها في سلسلة الكتل.
يجب أن يكون هناك مستوى ثانوي من
أنظمة الدفع التي هي أخف
وزنًا وأكثر كفاءة.*

*~ هال فيني، 2010-12-30، من أوائل محبي التشفير
وثاني شخص يقوم بتشغيل Bitcoin*

**فكر في الأمر بهذه الطريقة:**
>* Bitcoin: **حساب توفير** ~ معاملات أبطأ
>لمبالغ أكبر.
>* Lightning: **حساب جاري** ~ معاملات أسرع
>لمبالغ أصغر.


>*يمكن اعتبار Bitcoin المعزز بواسطة Lightning بمثابة منتج
(ملكية رقمية) وخدمة (شبكة نقدية مفتوحة). القدرة على نقل الطاقة النقدية عبر
الزمان والمكان دون تدخل حكومي أو
الخدمات المصرفية التقليدية ذات قيمة هائلة للبشرية.*

~ مايكل سايلور، الرئيس التنفيذي
Microstrategy

**تعرف على المزيد حول Lightning هنا:**

lopp.net/lightning-information.html

---
