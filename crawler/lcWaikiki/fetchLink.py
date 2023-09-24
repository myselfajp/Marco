from bs4 import BeautifulSoup
import requests
import json
import re

def FetchLink():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    category_list=CATEGORIES
    for category in category_list:
        for page in category["pages"]:
            limit=int(page[page.index("&count=")+7:])
            try:
                page_link=page+"&m_1007=37812,32027,34479,32600,37342,32220,37473,30989,37291,30611,31696,30817,31345,31895,34192,31870,37339,30816,34108,32447,37299,37338,34307,37357"
                # print(page_link)
                try:
                    script=BeautifulSoup(requests.get(page_link,headers=headers).text,"html.parser")
                    # print("ok")
                except:
                    # print("not")
                    continue
                script=script.find("script",string=re.compile("var catalogModel*")).text
                scriptt=script[script.index("var")+19:script.index('"RegionId":null')+16]
                script=json.loads(scriptt)["CatalogList"]["Items"]
                codes=[]
            except Exception as e:
                print("5490529",e)
                break

            for x in script:
                if not x["ModelId"] in codes :
                    codes.append(x["ModelId"])
                    # print("test",x["ModelId"])
                    category["links"].append("https://www.lcwaikiki.com"+x["ModelUrl"])
                if len(category["links"]) >= limit:
                    break
    links = []
    for cat in category_list:
        products = [{"categories":cat["categories"],"url":x} for x in cat["links"]]
        links += products
    print(len(links)," link found.")
    return links

CATEGORIES = [
        {
        "categories":["زنانه","لباس","پالتو و کاپشن"],
        "pages":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/kadin_mont_kaban-56?Sort=CreateDateDESC&count=50" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/kadin_yagmurluk-64?Sort=CreateDateDESC&count=50"],
        "links":[]
        },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"195",#سویشرت و بافت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/kazak?Sort=CreateDateDESC&count=33" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/hirka?m_981=31993,31600,31054,31041,31794,30891&Sort=CreateDateDESC&count=33" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/Sweatshirt?Sort=CreateDateDESC&count=33"],
        # "links":[]
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"192",#شلوار و شلوارک
        # "ex_cat":["406"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/jean?Sort=CreateDateDESC&count=70" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/esofman-alt?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/pantolon?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/tayt?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/sort-ve-capri?Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"202",#تونیک
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/Tunik?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"295",#سرهمی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/elbise?m_981=31494&Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"190",#تیشرت
        # "ex_cat":["410"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/tisort?Sort=CreateDateDESC&count=50"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"200",#لباس بارداری
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/hamile-giyim?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"204",#لباس ورزشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/aktif-spor-giyim-kadin-urunleri?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"191",#پیراهن
        # "ex_cat":["407"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/gomlek?Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"297",#بلوز
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/bluz?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"193",#دامن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/etek?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"298",#جلیقه
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/yelek?Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"205",#کت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/trenckot?Sort=CreateDateDESC&count=10" ,"https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/ceket?m_981=31888,30874,32730,31040&Sort=CreateDateDESC&count=10"] , 
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"197",#لباس خواب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/pijama?Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"198",#لباس رسمی
        # "ex_cat":["411"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/elbise?m_981=30726,33587,32526,31594,31592,32731,31925&Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"196",#ست لباس
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/hirka?m_981=31779&Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"199",#جوراب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/%C3%87orap?Sort=CreateDateDESC&count=5"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"201",#شال و روسری
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/kadin_fular_sal-62?Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"112",#لباس
        # "valid_cat":"203",#بادی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiketarama/%C3%A7%C4%B1t%C3%A7%C4%B1tl%C4%B1%20bodyler/20889?m_981=31998&m_1036=32659&Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"216",#بوت و نیم بوت
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/bot_ve_cizme-76?Sort=CreateDateDESC&count=30"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"214",#کفش ورزشی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/spor-ayakkabi?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"217",#دمپایی و صندل
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/ev-terligi-ve-panduf-196?Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"215",#کفش مجلسی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/topuklu-ayakkabi?Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"213",#کفش روزمره
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/babet-155?Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"124",#اکسسوری
        # "valid_cat":"209",#شال و کلاه و دستکش
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/kadin_atkibereeldiven-70?Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"219",#کیف رو دوشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/canta_ve_cuzdan_kadin-83?m_981=32442,32031,32052&Sort=CreateDateDESC&count=20"] ,
        # "links":[] 
        # },
        
        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"218",#کیف پول
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/canta_ve_cuzdan_kadin-83?m_981=30777&Sort=CreateDateDESC&count=20"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"263",#کیف دستی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/canta_ve_cuzdan_kadin-83?m_981=33703&Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"299",#کیف ورزشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/canta_ve_cuzdan_kadin-83?m_981=32055&Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"222",#کوله پشتی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/canta_ve_cuzdan_kadin-83?m_981=31080&Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        #  {
        # "sex":"91",#زنانه
        # "parent_cat":"212",#کیف و کفش
        # "valid_cat":"221",#کیف کمری
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/canta_ve_cuzdan_kadin-83?m_981=30916&Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"91",#زنانه
        # "parent_cat":"124",#اکسسوری
        # "valid_cat":"208",#کمربند
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kadin/kemer?Sort=CreateDateDESC&count=10"],
        # "links":[] 
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"234",#پالتو و کاپشن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_mont_kaban-14?Sort=CreateDateDESC&count=50" ],
        # "links":[]
        # },
        
        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"235",#سویشرت و بافت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/kazak?Sort=CreateDateDESC&count=50" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/Sweatshirt?Sort=CreateDateDESC&count=50" ],
        # "links":[]
        # },


        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"233",#شلوار و شلوارک
        # "ex_cat":["406"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/esofman-alt?Sort=CreateDateDESC&count=50" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/pantolon?Sort=CreateDateDESC&count=50" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/jean?Sort=CreateDateDESC&count=50" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/sort-ve-roller?Sort=CreateDateDESC&count=50"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"240",#لباس ورزشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/erkek-aktif-spor-urunler?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/erkek-atlet-urunleri?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"262",#کت
        # "ex_cat":[],
        # "page": ["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek-ceket?Sort=CreateDateDESC&count=100"],
        # "links":[]
        # },


        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"232",#پیراهن
        # "ex_cat":["407"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/gomlek?Sort=CreateDateDESC&count=200"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"231",#تیشرت
        # "ex_cat":["410"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/tisort?Sort=CreateDateDESC&count=300"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"239",#لباس خواب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/pijama?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"92",#لباس
        # "valid_cat":"238",#جوراب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/%C3%87orap?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"229",#کیف و کفش
        # "valid_cat":"250",#بوت و نیم بوت
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/bot?Sort=CreateDateDESC&count=50"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"229",#کیف و کفش
        # "valid_cat":"248",#کفش ورزشی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_trekking-298?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/spor-ayakkabi?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"229",#کیف و کفش
        # "valid_cat":"247",#کفش روزمره
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/klasik-ayakkabi-159?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"229",#کیف و کفش
        # "valid_cat":"252",#دمپایی و صندل
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/ev-terligi-ve-panduf-196?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"104",#اکسسوری
        # "valid_cat":"244",#شال و کلاه و دستکش
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_atkibereeldiven-24?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/sapka?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"104",#اکسسوری
        # "valid_cat":"243",#کمربند
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_kemer_cuzdan-36?m_981=32536,31692,32537,32571&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"229",#کیف و کفش
        # "valid_cat":"257",#کوله پشتی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_canta-37?m_981=32376,31080&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"229",#کیف و کفش
        # "valid_cat":"254",#کیف رودوشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_canta-37?m_981=32052&Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/erkek_canta-37?m_981=32031&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"90",#مردانه
        # "parent_cat":"230",#آرایشی و بهداشتی
        # "valid_cat":"258",#ادکلن و اسپری بدن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/erkek-parfum-kisisel-bakim?m_981=30990&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },


        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"341",#تیشرت
        # "ex_cat":["410"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/tisort?m_981=31290&Sort=CreateDateDESC&count=50" ],
        # "links":[]
        # },


        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"347",#پیراهن
        # "ex_cat":["407"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/gomlek?m_981=32730,30896&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"397",#تونیک
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/gomlek?m_981=31770,31886&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"346",#جلیقه
        # "ex_cat":[],
        # "page": ["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/kizcocuk_yelek-139?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },


        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"344",#بلوز
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/bluz?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"349",#سرهمی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/kizcocuk_tulum-169?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"342",#شلوار و شلوارک
        # "ex_cat":["406"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/tayt?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/pantolon?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/esofman-alt?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/jean?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/sort-ve-capri?m_981=32387,31931,30780,31952,31682&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"345",#دامن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/etek?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"343",#پالتو و کاپشن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/kizcocuk_mont_kaban-138?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"338",#سویشرت و بافت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/Sweatshirt?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/kazak?Sort=CreateDateDESC&count=20" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/hirka?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"340",#لباس رسمی
        # "ex_cat":["411"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/elbise?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"339",#ست لباس
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/takim?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"351",#لباس خواب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/pijama?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"350",#لباس شنا
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/plaj-kiyafeti?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },
        
        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"398",#بادی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/tisort?m_981=31998&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"337",#لباس
        # "valid_cat":"352",#جوراب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/%C3%87orap?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"364",#اکسسوری
        # "valid_cat":"365",#شال و کلاه و دستکش
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/atki-bere-ve-eldiven?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },
        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"357",#کفش روزمره
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/spor-ayakkabi?m_981=31875&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"356",#کفش ورزشی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/spor-ayakkabi?m_981=31165&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"399",#کفش مجلسی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/babet-155?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"354",#بوت و نیم بوت
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/kiz-cocuk-bot-ve-cizmee?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"355",#دمپایی و صندل
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/ev-terligi-ve-panduf-196?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"358",#کیف پول
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/canta_ve_cuzdan_kiz_cocuk-163?m_981=30777&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"360",#کیف رودوشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/canta_ve_cuzdan_kiz_cocuk-163?m_981=32052,32031&Sort=CreateDateDESC&count=5"],
        # "links":[]
        # },

        # {
        # "sex":"336",#دخترانه
        # "parent_cat":"353",#کیف و کفش
        # "valid_cat":"362",#کوله پشتی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-cocuk/canta_ve_cuzdan_kiz_cocuk-163?m_981=31080&Sort=CreateDateDESC&count=5"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"373",#تیشرت
        # "ex_cat":["410"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/tisort?Sort=CreateDateDESC&count=30" ],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"377",#پیراهن
        # "ex_cat":["407"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/gomlek?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"376",#جلیقه
        # "ex_cat":[],
        # "page": ["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/erkekcocuk_yelek-99?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"374",#شلوار و شلوارک
        # "ex_cat":["406"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/esofman-alt?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/pantolon?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/jean?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/sort-ve-roller?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        #  "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"375",#پالتو و کاپشن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/erkekcocuk_mont_kaban-98?Sort=CreateDateDESC&count=30"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"370",#سویشرت و بافت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/Sweatshirt?Sort=CreateDateDESC&count=30" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/hirka?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/kazak?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"395",#کت و ژاکت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/erkekcocuk_ceket-96?m_981=30874,31040&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"371",#ست لباس
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/takim?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"380",#لباس خواب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/pijama?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"378",#لباس ورزشی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/spor-giyim-217?m_981=31604&Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"379",#لباس شنا
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/plaj-kiyafeti?Sort=CreateDateDESC&count=20"],
        # "links":[]
        # },
        
        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"369",#لباس
        # "valid_cat":"381",#جوراب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/%C3%87orap?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"412",#اکسسوری
        # "valid_cat":"393",#کمربند
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/kemer_ve_kravat_erkek_cocuk-107?m_981=31692&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"412",#اکسسوری
        # "valid_cat":"392",#شال و کلاه و دستکش
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/atki-bere-ve-eldiven?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/sapka?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"382",#کیف و کفش
        # "valid_cat":"386",#کفش روزمره
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/spor-ayakkabi?m_981=31875&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"382",#کیف و کفش
        # "valid_cat":"385",#کفش ورزشی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/spor-ayakkabi?m_981=31165,30862&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"382",#کیف و کفش
        # "valid_cat":"400",#کفش مجلسی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/klasik-ayakkabi-159?Sort=CreateDateDESC&count=5"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"382",#کیف و کفش
        # "valid_cat":"383",#بوت و نیم بوت
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/bot?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"382",#کیف و کفش
        # "valid_cat":"384",#دمپایی و صندل
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/ev-terligi-ve-panduf-196?Sort=CreateDateDESC&count=5"],
        # "links":[]
        # },

        # {
        # "sex":"368",#پسرانه
        # "parent_cat":"382",#کیف و کفش
        # "valid_cat":"390",#کوله پشتی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-cocuk/erkekcocuk_canta_ve_cuzdan-121?m_981=31080&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },
        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"322",#تیشرت
        # "ex_cat":["410"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-tisort?Sort=CreateDateDESC&count=10" ],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"326",#جلیقه
        # "ex_cat":[],
        # "page": ["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-yelek?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"324",#سرهمی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-tulum?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"325",#شلوار و شلوارک
        # "ex_cat":["406"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-tayt?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-sort?m_981=31952,31682&Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-pantolon?Sort=CreateDateDESC&count=10" ],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"401",#دامن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-sort?m_981=37278,30770&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"402",#پالتو و کاپشن
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/newborn-mont-kaban?m_981=31904,37404,30811,30743,31494,31304,37407&Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-astronot-mont?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"323",#سویشرت و بافت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-sweatshirt?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-hirka?Sort=CreateDateDESC&count=10" ],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"423",#کت و ژاکت
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/newborn-mont-kaban?m_981=31616&Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"321",#لباس رسمی
        # "ex_cat":["411"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-elbise?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"327",#ست لباس
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-takim?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-hastane-setleri?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"328",#لباس خواب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-pijama?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-uyku-tulumu?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"403",#لباس شنا
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-plaj-giyim?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"404",#بادی
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-citcitli-body?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-citicitli-body?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"320",#لباس
        # "valid_cat":"329",#جوراب
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-corap?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"334",#اکسسوری
        # "valid_cat":"335",#شال و کلاه و دستکش
        # "ex_cat":[],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/atki-bere-eldiven-yenidogan?Sort=CreateDateDESC&count=10" , "https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-sapka?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },
        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"330",#کیف و کفش
        # "valid_cat":"333",#کفش روزمره
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/bebek-yurume-oncesi?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"330",#کیف و کفش
        # "valid_cat":"405",#کفش مجلسی
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-ilk-adim-ayakkabisi?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"330",#کیف و کفش
        # "valid_cat":"331",#بوت و نیم بوت
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-bot?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },

        # {
        # "sex":"319",#نوزاد
        # "parent_cat":"330",#کیف و کفش
        # "valid_cat":"332",#دمپایی و صندل
        # "ex_cat":["408"],
        # "page":["https://www.lcwaikiki.com/tr-TR/TR/etiket/yenidogan-ev-terlik-panduf?Sort=CreateDateDESC&count=10"],
        # "links":[]
        # },
    ]

