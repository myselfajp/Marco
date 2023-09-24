from crawler.utils.addToLocal import TranslateNeeded


def size_translate(Size,brand):
    if brand in ["lc_waikiki","koton","zara","bershka","victoria_secret"]:
        translate = {
                    "Yaş":"سال",
                    "Ay":"ماه",
                    "yaş":"سال",
                    "ay":"ماه",
                    "standart":"استاندارد",
                    "STANDART":"استاندارد",
                    "tek beden":"تک سایز",
                    "Tek Beden":"تک سایز",
                    "TEK BEDEN":"تک سایز",
                    "(US XXS)":"",
                    "(US XS)":"",
                    "(US S)":"",
                    "(US M)":"",
                    "(US L)":"",
                    "(US XL)":"",
                    "(US XXL)":"",
                    "(US XXXL)":"",
                    "(US 34)":"",
                    "(US 35)":"",
                    "(US 36)":"",
                    "(US 37)":"",
                    "(US 38)":"",
                    "(US 39)":"",
                    "(US 40)":"",
                    "(US 41)":"",
                    "(US 42)":"",
                    "(US 43)":"",
                    "(US 44)":"",
                    "(US 45)":"",
                    "(US 46)":"",
                    "(US 47)":"",
                    "(US 48)":"",
                    "(US 49)":"",
                    }
                    
        for x in translate:
            Size=Size.replace(x,translate[x])
        return Size
    else:
        return Size


def genderFinder(categories = list):
    gender = None 
    if "متفرقه" in categories:
        gender = "متفرقه"
    elif "مردانه" in categories:
        gender = "مردانه"
    elif "زنانه" in categories:
        gender = "زنانه"
    elif "پسرانه" in categories:
        gender = "پسرانه"
    elif "دخترانه" in categories:
        gender = "دخترانه"
    else:
        gender = "دسته بندی نشده"
    return gender


def price_comision(price,url):
    try:
        price =int(price)*3000

        price=(price*30//100)+price

        
        price+=200000 

        return price
    except:
        print("error price : 344451 ",price,url)
        return 


def title_translate(title,url,brand):
    orginal=title
    if brand in ["lc_waikiki","koton"]:
        chars = {
            "Kaban" : "پالتو بلند","Casual Ayakkabı":"کفش کژوال","Mayo Takımı":"ست مایو","Pijama altı":"پیژامه پایین تنه","Spor Ceket":"ژاکت اسپورت","Sütyen":"تاپ","Sneaker Çorap":"جوراب","Pantolon Etek":"جوراب شلواری","Kayak Pantolonu":"کاپشن اسکی","Jean Tunik":"تونیک جین","Jartiyer Çorabı":"جوراب","Yağmurluk Tulum":"بارانی سرهمی","Parfüm":"ادکلن","Polo Yaka T-shirt":"پولوشرت","Gelinlik":"لباس عروس","Hastane Seti":"ست لباس","Astronot Mont":"کاپشن فضانوردی(سرهمی)","":"","Kaşe Kaban" : "پالتو بلند","Şişme Mont" : "کاپشن بادی","Deri Görünümlü Mont" : "کاپشن چرم","Mont":"کاپشن","Parka":"کاپشن","Yağmurluk":"بارانی","Kazak":"بافت","Hırka":"کت پشمی","Spor Hırka":"ژاکت ورزشی","Sweatshirt":"سوئیشرت","Tunik":"تونیک","Jean":"جین","Eşofman Altı":"شلوار گرمکن","Pantolon":"شلوار","Tayt":"تایت","Şort":"شلوارک کوتاه","Capri":"شلوارک کوتاه","Şort Etek":"دامن کوتاه","Jean Şort":"شورت جین","Jean Şort Etek":"دامن کوتاه جین","Kimono":"کیمونو","Elbise":"لباس رسمی","Salopet":"پیش بندی سرهمی","Jean Elbise":"جین سرهمی","Ferace":"مانتو","Tişört":"تیشرت","Büstiyer":"نیم تنه","Atlet":"زیرپوش","Çorap":"جوراب","Külotlu Çorap":"جوراب شلواری","İç Giyim Atlet":"زیرپوش","Külot":"شورت","Emzirme Sütyeni":"سوتین","Gecelik":"لباس خواب","Pijama Takım":"ست لباس خواب","Gömlek":"پیراهن","Sabahlık":"لباس راحتی","Jean Gömlek":"پیراهن جین","Bluz":"بلوز","Etek":"دامن","Jean Etek":"دامن جین","Yelek":"جلیقه","Jean Yelek":"جلیقه جین","Trençkot":"بارانی بلند","Ceket":"ژاکت","Blazer Ceket":"ژاکت بلیزر","Gömlek Ceket":"ژاکت پیراهن","Pijama Alt":"پیژامه پایین تنه","Uyku Maskesi":"چشم بند خواب","Pijama Üst":"پیژامه بالاتنه","Süveter":"جلیقه بافت","Diz Altı Çorap":"جوراب بلند تا زیر زانو","Patik Çorap":"جوراب","Soket Çorap":"جوراب","Ev Çorabı":"جوراب خانه","Babet Çorap":"جوراب","Şal":"شال","Bone":"حجاب سر","Bandana":"روسری","Fular":"روسری","Eşarp":"شال","Bot":"بوت","Yağmur Çizmesi":"پوتین بارانی","Kar Botu":"بوت برفی","Çizme":"پوتین","Sneaker":"کفش ورزشی اسنیکر","Aktif Spor Ayakkabı":"کفش اسپرت","Ayakkabı":"کفش","Ev Ayakkabısı":"کفش خانه","Ev Terliği":"دمپایی خانه","Ev Botu":"بوت خانه","Panduf": "دمپایی خانه","Uyku Seti" : "ست خواب","Stiletto":"کفش رسمی مدل Stiletto","Topuklu Ayakkabı":"کفش پاشنه بلند","Sandalet":"صندل","Babet":"کفش طبی","Eldiven":"دستکش","Bere":"کلاه بافت","Atkı":"شال پشمی","Boyunluk":"گردنی","Omuz Çantası":"کیف رودوشی","Baget Çanta":"کیف دوشی","Alışveriş Çantası" : "کیف خرید","Set Kemer":"ست کمربند" ,"Bel Kemeri":"کمربند","Kot Kemeri":"کمربند","Kemer":"کمربند","Büzgülü Çanta":"کیف بند دار","Bel Çantası":"کیف کمری","Makyaj Çantası":"کیف لوازم آرایش","Çantalı Kemer":"کیف کمربندی","El Çantası":"کیف دستی","Kartlık":"کیف کارت","Bozuk Para Cüzdanı":"کیف پول سکه","Telefon Çantası":"کیف تلفن","Cüzdan":"کیف پول","Kol Çantası":"کیف دستی","Çapraz Çanta":"کیف کراس بادی","Sırt Çantası":"کوله پشتی","Spor Çanta":"کیف ورزشی","Şapka":"کلاه","Takım Elbise":"ست لباس رسمی","Uyku Tulumu":"لباس خواب سرهمی","Tulum":"سرهمی","Jean Ceket":"کت جین","Takım":"ست","Chino Kemeri":"کمربند","Laptop Çantası":"کیف لپتاپ","Atkı ve Bere":"شال و کلاه","Bucket Şapka":"کلاه باکت","Espadril":"کفش اسپادریل","Fötr Şapka":"کلاه لبه دار","Kar Şapkası":"کلاه برفی","Kasket":"کلاه","Kep Şapka":"کلاه کپ","Klasik Ayakkabı":"کفش رسمی کلاسیک","Ressam Şapka":"کلاه gentle هنری","Roller Şort":"شلوارک","Terlik":"دمپایی","Trekking":"کفش پیاده روی","Trekking Bot":"بوت پیاده روی","Yürüyüş ve Koşu Ayakkabısı":"کفش ورزشی و پیاده روی","Çıtçıtlı Body":"بادی","Eşofman Takım":"ست لباس ورزشی","Patik":"پاپوش پشمی","Pareo":"ساحلی","Mayo":"مایو","Yüzme Şort":"شورت شنا","Yüzme Takım":"ست لباس شنا","Yüzme Giysisi":"لباس شنا","Yüzme Giyim Üst":"لباس بالا تنه‌‌ شنا","Yürüme Öncesi":"کفش مخصوص","Yağmur Botu":"بوت بارانی","Takım Elbise":"ست لباس رسمی","Kostüm":"کاستوم","Kayak Montu":"کاپشن اسکی","Jean Salopet":"سالوپت جین","Jean Roller":"شلوارک جین","İlk Adım Ayakkabısı":"کفش مخصوص","Hip Hop Şapka":"کلاه هیپ هاپ","Bikini":"بیکینی","Bermuda":"شلوارک ساحلی","Atkı Bere Ve Eldiven Takım":"ست شال و کلاه و دستکش",
            }
        try:
            title=title.strip()
            return chars[title]
        except:
            TranslateNeeded(title,url)
            return title

    elif brand in ["bershka"]:
        chars = {
            "saten çanta":"کیف دستی","korse top":"تاپ","kol çantası":"کیف دستی","kapitone çanta":"کیف دستی","clutch çanta":"کیف دستی","el çantası":"کیف دستی","comfort jean":"شلوار جین","kargo jean":"شلوار جین گشاد","Volanlı kargo jean":"شلوار جین گشاد","leg 90’s jean":"شلوار جین دهه شصت","spor ayakkabı":"کفش اسپورت","biker ceket":"ژاکت","deri ceket":"ژاکت","kemer":"کمربند","askılı çanta":"کیف رودوشی","topuklu":"کفش پاشنه بلند","skinny fit jean":"جین تنگ","skinny jean":"جین تنگ","şapka":"کلاه","kazak":"بافت","süet ceket":"ژاکت","süveter":"بافت آستین حلقه ای","deri kaban":"پالتو چرم","şişme mont":"کاپشن بادی","şişme kaban":"پالتو بادی","kapüşonlu ince ceket":"ژاکت کلاهدار","kısa elbise":"لباس رسمی کوتاه","taşlı çanta":"کیف رودوشی","kapüşonlu sweatshirt":"سویشرت کلاه دار","jegging jean":"شلوار جین","fit jean":"جین تنگ","kısa ceket":"ژاکت کوتاه","ince ceket":"ژاکت نازک","vintage jean":"شلوار جین","Şişme yelek":"جلیقه بادی","şişme yelek":"جلیقه بادی","uzun elbise":"لباس رسمی بلند","paça jean":"شلوار جین پاچه گشاد","kesim jean":"جین زاپ دار","Eau de":"ادکلن"+title.replace("Bershka","").strip(),"korse kazak":"سوتین بافت",
            "bolero":"بالاتنه",
            "culottes":"رسمی","trousers":"شلوار","kartlık":"جا کارتی","mont":"کاپشن","atkı":"شال","jogger":"اسلش","cüzdan":"کیف پول","yelek":"جلیقه","korse":"تاپ","tayt":"تایت","trençkot":"ژاکت","şort":"شورت","ayakkabı":"کفش","bere":"کلاه","sweatshirt":"سویشرت","çanta":"کیف","kaban":"پالتو","tişört":"تیشرت","hırka":"بافت","etek":"دامن","gömlek":"پیراهن","t-shirt":"تیشرت","pantolon":"شلوار","bluz":"بلوز","top":"تاپ","ceket":"ژاکت","elbise":"لباس رسمی","jean":"جین","Kolsuz":"بدون آستین",
            }

        for x in chars:
            if x in title  :
                t_word=chars[x]
                break
        else:
            TranslateNeeded(title,url)
            return title

        if "2'li" in title:t_word="پک دوتایی "+t_word
        elif "3'li" in title:t_word="پک سه تایی "+t_word
        
        TranslateNeeded(title,orginal)#need update
        return t_word



def description(brand,category,sex):
    if brand == "lc_waikiki" and category == "233" and sex == "مردانه":
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">ارتفاع داخلی پا</th><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">90</td><td class="tg-zpf4">83</td><td class="tg-zpf4">Xs-28</td></tr><tr><td class="tg-zpf4">78.5</td><td class="tg-zpf4">96</td><td class="tg-zpf4">88</td><td class="tg-zpf4">s-30</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">102</td><td class="tg-zpf4">93</td><td class="tg-zpf4">m-32</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">108</td><td class="tg-zpf4">98</td><td class="tg-zpf4">l-34</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">114</td><td class="tg-zpf4">105</td><td class="tg-zpf4">xl-36</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">120</td><td class="tg-zpf4">113</td><td class="tg-zpf4">Xxl-38</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">126</td><td class="tg-zpf4">120</td><td class="tg-zpf4">3xxl-40</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">132</td><td class="tg-zpf4">128</td><td class="tg-zpf4">4xl-42</td></tr><tr><td class="tg-zpf4">81</td><td class="tg-zpf4">138</td><td class="tg-zpf4">136</td><td class="tg-zpf4">5xl-44</td></tr></tbody></table>
        """
    elif brand == "lc_waikiki" and  sex=="مردانه"  and (category in ["234","235","240","262","232","231","239"]):
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">90</td><td class="tg-zpf4">83</td><td class="tg-zpf4">86</td><td class="tg-zpf4">Xs-46</td></tr><tr><td class="tg-zpf4">96</td><td class="tg-zpf4">88</td><td class="tg-zpf4">92</td><td class="tg-zpf4">s-48</td></tr><tr><td class="tg-zpf4">102</td><td class="tg-zpf4">93</td><td class="tg-zpf4">98</td><td class="tg-zpf4">m-50</td></tr><tr><td class="tg-zpf4">108</td><td class="tg-zpf4">98</td><td class="tg-zpf4">104</td><td class="tg-zpf4">l-52</td></tr><tr><td class="tg-zpf4">114</td><td class="tg-zpf4">105</td><td class="tg-zpf4">110</td><td class="tg-zpf4">xl-54</td></tr><tr><td class="tg-zpf4">120</td><td class="tg-zpf4">113</td><td class="tg-zpf4">118</td><td class="tg-zpf4">Xxl-56</td></tr><tr><td class="tg-zpf4">126</td><td class="tg-zpf4">120</td><td class="tg-zpf4">126</td><td class="tg-zpf4">3xl-58</td></tr><tr><td class="tg-zpf4">132</td><td class="tg-zpf4">128</td><td class="tg-zpf4">134</td><td class="tg-zpf4">4xl-60</td></tr><tr><td class="tg-zpf4">138</td><td class="tg-zpf4">136</td><td class="tg-zpf4">142</td><td class="tg-zpf4">5xl-62</td></tr></tbody></table>
            """
    elif brand == "lc_waikiki" and  sex=="زنانه"  and category =="192":
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">ارتفاع داخلی پا</th><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">73</td><td class="tg-zpf4">86</td><td class="tg-zpf4">66</td><td class="tg-zpf4">34|xs</td></tr><tr><td class="tg-zpf4">75</td><td class="tg-zpf4">92</td><td class="tg-zpf4">70</td><td class="tg-zpf4">36|s</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">98</td><td class="tg-zpf4">74</td><td class="tg-zpf4">38||m</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">103</td><td class="tg-zpf4">79</td><td class="tg-zpf4">40|l</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">108</td><td class="tg-zpf4">84</td><td class="tg-zpf4">42|xl</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">113</td><td class="tg-zpf4">89</td><td class="tg-zpf4">44|xxl</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">119</td><td class="tg-zpf4">96</td><td class="tg-zpf4">46|3xl</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">125</td><td class="tg-zpf4">104</td><td class="tg-zpf4">48|4xl</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">131</td><td class="tg-zpf4">111</td><td class="tg-zpf4">50|5xl</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">137</td><td class="tg-zpf4">118</td><td class="tg-zpf4">52|6xl</td></tr></tbody></table>
            """
    elif  brand == "lc_waikiki" and category in ["194","195","202","295","190","200","204","191","297","193","298","205","197","198","196","203"] and sex=="زنانه":
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">قد</th><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">156-160</td><td class="tg-zpf4">86</td><td class="tg-zpf4">66</td><td class="tg-zpf4">78</td><td class="tg-zpf4">34|xs</td></tr><tr><td class="tg-zpf4">160-164</td><td class="tg-zpf4">92</td><td class="tg-zpf4">70</td><td class="tg-zpf4">84</td><td class="tg-zpf4">36|s</td></tr><tr><td class="tg-zpf4">160</td><td class="tg-zpf4">89</td><td class="tg-zpf4">68</td><td class="tg-zpf4">81</td><td class="tg-zpf4">36/34|xs-s</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">98</td><td class="tg-zpf4">74</td><td class="tg-zpf4">90</td><td class="tg-zpf4">38||m</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">101</td><td class="tg-zpf4">77</td><td class="tg-zpf4">92</td><td class="tg-zpf4">40/38|m-l</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">103</td><td class="tg-zpf4">79</td><td class="tg-zpf4">95</td><td class="tg-zpf4">40|l</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">108</td><td class="tg-zpf4">84</td><td class="tg-zpf4">100</td><td class="tg-zpf4">42|xl</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">115</td><td class="tg-zpf4">91</td><td class="tg-zpf4">106</td><td class="tg-zpf4">44/42|xl-xxl</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">113</td><td class="tg-zpf4">90</td><td class="tg-zpf4">106</td><td class="tg-zpf4">44|xxl</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">123</td><td class="tg-zpf4">102</td><td class="tg-zpf4">116</td><td class="tg-zpf4">48/46|3xl</td></tr><tr><td class="tg-zpf4">163-167</td><td class="tg-zpf4">133</td><td class="tg-zpf4">114</td><td class="tg-zpf4">126</td><td class="tg-zpf4">52/50|4xl</td></tr></tbody></table>
            """



    elif brand == "koton" and category == "233" and sex == "مردانه":
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">90</td><td class="tg-zpf4">76</td><td class="tg-zpf4">36-xxs</td></tr><tr><td class="tg-zpf4">94</td><td class="tg-zpf4">80</td><td class="tg-zpf4">38-xs</td></tr><tr><td class="tg-zpf4">98</td><td class="tg-zpf4">84</td><td class="tg-zpf4">40-s</td></tr><tr><td class="tg-zpf4">102</td><td class="tg-zpf4">88</td><td class="tg-zpf4">42-m</td></tr><tr><td class="tg-zpf4">106</td><td class="tg-zpf4">92</td><td class="tg-zpf4">44-l</td></tr><tr><td class="tg-zpf4">110</td><td class="tg-zpf4">96</td><td class="tg-zpf4">46-xl</td></tr><tr><td class="tg-zpf4">114</td><td class="tg-zpf4">100</td><td class="tg-zpf4">48-xxl</td></tr><tr><td class="tg-zpf4">118</td><td class="tg-zpf4">104</td><td class="tg-zpf4">50-3xl</td></tr><tr><td class="tg-zpf4">122</td><td class="tg-zpf4">108</td><td class="tg-zpf4">52-4xl</td></tr></tbody></table>
            <h3> سایز مناسب جین </h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">95.5</td><td class="tg-zpf4">80.5</td><td class="tg-zpf4">29</td></tr><tr><td class="tg-zpf4">97</td><td class="tg-zpf4">83</td><td class="tg-zpf4">30</td></tr><tr><td class="tg-zpf4">99.5</td><td class="tg-zpf4">85.5</td><td class="tg-zpf4">31</td></tr><tr><td class="tg-zpf4">102</td><td class="tg-zpf4">88</td><td class="tg-zpf4">32</td></tr><tr><td class="tg-zpf4">104.5</td><td class="tg-zpf4">90.5</td><td class="tg-zpf4">33</td></tr><tr><td class="tg-zpf4">107</td><td class="tg-zpf4">93</td><td class="tg-zpf4">34</td></tr><tr><td class="tg-zpf4">112</td><td class="tg-zpf4">98</td><td class="tg-zpf4">36</td></tr><tr><td class="tg-zpf4">117</td><td class="tg-zpf4">103</td><td class="tg-zpf4">38</td></tr><tr><td class="tg-zpf4">122</td><td class="tg-zpf4">108</td><td class="tg-zpf4">40</td></tr></tbody></table>
            """
    elif brand == "koton" and  sex=="مردانه"  and (category in ["234","235","240","262","232","231","239"]):
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">60</td><td class="tg-zpf4">88</td><td class="tg-zpf4">44-xxs</td></tr><tr><td class="tg-zpf4">64</td><td class="tg-zpf4">92</td><td class="tg-zpf4">46-xs</td></tr><tr><td class="tg-zpf4">68</td><td class="tg-zpf4">96</td><td class="tg-zpf4">48-s</td></tr><tr><td class="tg-zpf4">72</td><td class="tg-zpf4">100</td><td class="tg-zpf4">50-m</td></tr><tr><td class="tg-zpf4">76</td><td class="tg-zpf4">104</td><td class="tg-zpf4">52-l</td></tr><tr><td class="tg-zpf4">80</td><td class="tg-zpf4">108</td><td class="tg-zpf4">54-xl</td></tr><tr><td class="tg-zpf4">86</td><td class="tg-zpf4">112</td><td class="tg-zpf4">56-xxl</td></tr><tr><td class="tg-zpf4">92</td><td class="tg-zpf4">116</td><td class="tg-zpf4">58-3xl</td></tr><tr><td class="tg-zpf4">98</td><td class="tg-zpf4">120</td><td class="tg-zpf4">60-4xl</td></tr></tbody></table>
            """
    elif brand == "koton" and  sex=="زنانه"  and category =="192":
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">86</td><td class="tg-zpf4">60</td><td class="tg-zpf4">32(25)-xxs</td></tr><tr><td class="tg-zpf4">90</td><td class="tg-zpf4">64</td><td class="tg-zpf4">34(26)-xs</td></tr><tr><td class="tg-zpf4">94</td><td class="tg-zpf4">68</td><td class="tg-zpf4">36(27)-s</td></tr><tr><td class="tg-zpf4">98</td><td class="tg-zpf4">72</td><td class="tg-zpf4">38(28)-m</td></tr><tr><td class="tg-zpf4">102</td><td class="tg-zpf4">76</td><td class="tg-zpf4">40(29)-l</td></tr><tr><td class="tg-zpf4">106</td><td class="tg-zpf4">80</td><td class="tg-zpf4">42(30)-xl</td></tr><tr><td class="tg-zpf4">112</td><td class="tg-zpf4">86</td><td class="tg-zpf4">44(31)-xxl</td></tr><tr><td class="tg-zpf4">118</td><td class="tg-zpf4">92</td><td class="tg-zpf4">46(32)-3xl</td></tr><tr><td class="tg-zpf4">124</td><td class="tg-zpf4">98</td><td class="tg-zpf4">48(34)-4xl</td></tr></tbody></table>
            """
    elif  brand == "koton" and category in ["194","195","202","295","190","200","204","191","297","193","298","205","197","198","196","203"] and sex=="زنانه":
          text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">دور باسن</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">سایز</th></tr></thead><tbody><tr><td class="tg-zpf4">86</td><td class="tg-zpf4">60</td><td class="tg-zpf4">76</td><td class="tg-zpf4">32-xxs</td></tr><tr><td class="tg-zpf4">90</td><td class="tg-zpf4">64</td><td class="tg-zpf4">80</td><td class="tg-zpf4">34-xs</td></tr><tr><td class="tg-zpf4">94</td><td class="tg-zpf4">68</td><td class="tg-zpf4">84</td><td class="tg-zpf4">36-s</td></tr><tr><td class="tg-zpf4">98</td><td class="tg-zpf4">72</td><td class="tg-zpf4">88</td><td class="tg-zpf4">38-m</td></tr><tr><td class="tg-zpf4">102</td><td class="tg-zpf4">76</td><td class="tg-zpf4">92</td><td class="tg-zpf4">40-l</td></tr><tr><td class="tg-zpf4">106</td><td class="tg-zpf4">80</td><td class="tg-zpf4">96</td><td class="tg-zpf4">42-xl</td></tr><tr><td class="tg-zpf4">112</td><td class="tg-zpf4">86</td><td class="tg-zpf4">102</td><td class="tg-zpf4">44-xxl</td></tr><tr><td class="tg-zpf4">118</td><td class="tg-zpf4">92</td><td class="tg-zpf4">108</td><td class="tg-zpf4">46-3xl</td></tr><tr><td class="tg-zpf4">124</td><td class="tg-zpf4">98</td><td class="tg-zpf4">114</td><td class="tg-zpf4">48-4xl</td></tr></tbody></table>
            """


    elif brand == "victoria_secret" and category in ["192","197"]:
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">سایز</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور باسن</th></tr></thead><tbody><tr><td class="tg-zpf4">Xxs<br>00</td><td class="tg-zpf4">80</td><td class="tg-zpf4">58.4</td><td class="tg-zpf4">85</td></tr><tr><td class="tg-zpf4">Xs<br>0-2</td><td class="tg-zpf4">82.5<br>85</td><td class="tg-zpf4">61<br>63.5</td><td class="tg-zpf4">87<br>90</td></tr><tr><td class="tg-zpf4">S<br>4-6<br></td><td class="tg-zpf4">87.5<br>90</td><td class="tg-zpf4">66<br>68.5</td><td class="tg-zpf4">92.5<br>95</td></tr><tr><td class="tg-zpf4">M<br>8-10<br></td><td class="tg-zpf4">92.5<br>95</td><td class="tg-zpf4">71<br>73.5</td><td class="tg-zpf4">98<br>100</td></tr><tr><td class="tg-zpf4">L<br>12-14<br></td><td class="tg-zpf4">99<br>103</td><td class="tg-zpf4">77.5<br>81</td><td class="tg-zpf4">104<br>108</td></tr><tr><td class="tg-zpf4">Xl<br>16-18</td><td class="tg-zpf4">108<br>113</td><td class="tg-zpf4">86.5<br>91.5</td><td class="tg-zpf4">113<br>118</td></tr><tr><td class="tg-zpf4">Xxl<br>20</td><td class="tg-zpf4">118</td><td class="tg-zpf4">96.5</td><td class="tg-zpf4">123</td></tr></tbody></table>

            """

    #--------------------------------------------برشکا-----------------------------------------
    #برشکا مردانه بالا تنه
    elif  brand == "bershka" and sex=="مردانه"  and category in ["231","232","234","235","239","240","262","318"]:
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            <table class="tg"><thead><tr><th class="tg-zpf4">سایز</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">دور باسن</th></tr></thead><tbody><tr><td class="tg-zpf4">XXS</td><td class="tg-zpf4">81</td><td class="tg-zpf4">81</td></tr><tr><td class="tg-zpf4">XS</td><td class="tg-zpf4">87</td><td class="tg-zpf4">87</td></tr><tr><td class="tg-zpf4">S</td><td class="tg-zpf4">93</td><td class="tg-zpf4">93</td></tr><tr><td class="tg-zpf4">M</td><td class="tg-zpf4">99</td><td class="tg-zpf4">99</td></tr><tr><td class="tg-zpf4">L</td><td class="tg-zpf4">105</td><td class="tg-zpf4">105</td></tr><tr><td class="tg-zpf4">XL</td><td class="tg-zpf4">111</td><td class="tg-zpf4">111</td></tr><tr><td class="tg-zpf4">XXL</td><td class="tg-zpf4">117</td><td class="tg-zpf4">117</td></tr></tbody></table>
            """
    #برشکا مردانه پایین تنه
    elif brand == "bershka" and sex == "مردانه" and category == "233" :
        text="""
            <h3> جدول راهنمای تشخیص سایز:</h3>
            </thead><tbody><tr><td class="tg-zpf4">34-XS</td><td class="tg-zpf4">70</td><td class="tg-zpf4">87</td></tr><tr><td class="tg-zpf4">36</td><td class="tg-zpf4">74</td><td class="tg-zpf4">91</td></tr><tr><td class="tg-zpf4">S</td><td class="tg-zpf4">76</td><td class="tg-zpf4">93</td></tr><tr><td class="tg-zpf4">38</td><td class="tg-zpf4">78</td><td class="tg-zpf4">95</td></tr><tr><td class="tg-zpf4">40-M</td><td class="tg-zpf4">82</td><td class="tg-zpf4">99</td></tr><tr><td class="tg-zpf4">42</td><td class="tg-zpf4">86</td><td class="tg-zpf4">103</td></tr><tr><td class="tg-zpf4">44</td><td class="tg-zpf4">86</td><td class="tg-zpf4">107</td></tr><tr><td class="tg-zpf4">L</td><td class="tg-zpf4">88</td><td class="tg-zpf4">105</td></tr><tr><td class="tg-zpf4">46-XL</td><td class="tg-zpf4">94</td><td class="tg-zpf4">111</td></tr></tbody></table>
            """
    #برشکا زنانه بالا تنه
    elif  brand == "bershka" and sex=="زنانه" and category in ["190","191","194","195","196","197","198","200","202","203","204","205","295""297","298"]:
            text="""
        <h3> جدول راهنمای تشخیص سایز:</h3>
        <table class="tg"><thead><tr><th class="tg-zpf4">سایز</th><th class="tg-zpf4">دور سینه</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور باسن</th></tr></thead><tbody><tr><td class="tg-zpf4">XS</td><td class="tg-zpf4">82</td><td class="tg-zpf4">60</td><td class="tg-zpf4">88</td></tr><tr><td class="tg-zpf4">XS - S</td><td class="tg-zpf4">88</td><td class="tg-zpf4">66</td><td class="tg-zpf4">94</td></tr><tr><td class="tg-zpf4">M - L</td><td class="tg-zpf4">94</td><td class="tg-zpf4">72</td><td class="tg-zpf4">100</td></tr><tr><td class="tg-zpf4">L</td><td class="tg-zpf4">102</td><td class="tg-zpf4">79</td><td class="tg-zpf4">108</td></tr><tr><td class="tg-zpf4">XL</td><td class="tg-zpf4">108</td><td class="tg-zpf4">85</td><td class="tg-zpf4">114</td></tr></tbody></table>
                """
    # برشکا زنانه پایین تنه
    elif brand == "bershka" and  sex=="زنانه"  and category in ["192","193"]:
        text="""
        <h3> جدول راهنمای تشخیص سایز:</h3>
        <table class="tg"><thead><tr><th class="tg-zpf4">سایز</th><th class="tg-zpf4">دور کمر</th><th class="tg-zpf4">دور باسن</th></tr></thead><tbody><tr><td class="tg-zpf4">XS</td><td class="tg-zpf4">60</td><td class="tg-zpf4">88</td></tr><tr><td class="tg-zpf4">XS - S</td><td class="tg-zpf4">66</td><td class="tg-zpf4">94</td></tr><tr><td class="tg-zpf4">M - L</td><td class="tg-zpf4">72</td><td class="tg-zpf4">100</td></tr><tr><td class="tg-zpf4">L</td><td class="tg-zpf4">79</td><td class="tg-zpf4">108</td></tr><tr><td class="tg-zpf4">XL</td><td class="tg-zpf4">85</td><td class="tg-zpf4">114</td></tr><tr><td class="tg-zpf4">32</td><td class="tg-zpf4">58</td><td class="tg-zpf4">86</td></tr><tr><td class="tg-zpf4">34</td><td class="tg-zpf4">62</td><td class="tg-zpf4">90</td></tr><tr><td class="tg-zpf4">36</td><td class="tg-zpf4">66</td><td class="tg-zpf4">94</td></tr><tr><td class="tg-zpf4">38</td><td class="tg-zpf4">71</td><td class="tg-zpf4">99</td></tr><tr><td class="tg-zpf4">40</td><td class="tg-zpf4">76</td><td class="tg-zpf4">104</td></tr><tr><td class="tg-zpf4">42</td><td class="tg-zpf4">81</td><td class="tg-zpf4">110</td></tr><tr><td class="tg-zpf4">44</td><td class="tg-zpf4">86</td><td class="tg-zpf4">115</td></tr></tbody></table>
             """

    else:text=""



    return text