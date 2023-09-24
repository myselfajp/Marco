from crawler.core.dict import title_translate,site_categories,site_brands,size_translate,description
from bs4 import BeautifulSoup
import requests
# import json
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def product_sku(product):
    try:
        product_id = product.find("meta", attrs={"name": "ModelId"}).attrs["content"]

        return f"lc_waikiki-{product_id}"
    except Exception as e:
        print("error 325241",e)
        return

def product_name(product,url,sex,sku):
    try:
        product_name2 = product.find("meta", attrs={"property":"og:title"}).attrs["content"].split("-")[0].strip()
        mark = product.find("meta", attrs={"name":"BrandName"}).attrs["content"]
        name=title_translate(product_name2,url,"lc_waikiki")
        if name:
            return f"{name} {sex} - محصول برند {mark} ال سی وایکیکی ترکیه - کد محصول : {sku}"
        else:
            return
    except Exception as e:
        print("error 4754323",e)
        return ''

def product_description(category,sex,sku,name):
    try:
        table = description("lc_waikiki",category,sex)
        finish="""
                <p><h5>
                    این محصول مستقیما از سایت "ال سی وایکیکی" ترکیه تهیه شده است و با فاکتور رسمی همین برند برای شما ارسال میگردد.

                محصولات سفارشی شما، هم در زمان ارسال از ترکیه، و هم در زمان ارسال در ایران، توسط تیم "مد از ما" کاملا بررسی شده و در سلامت کامل به دست شما مشتری عزیز خواهد رسید.

                * قیمت درج شده در این صفحه ، قیمت نهایی محصول بوده و هیچ مبلغ دیگری بابت هزینه ی ارسال و غیره از شما دریافت نخواهد شد
                
                زمان تحویل محصول : 10 الی 20 روز کاری
                نوع محصول : %s
                کد محصول : %s
                </h5>
                </p>
                %s
                """%(name,sku,table)
        return finish
    except Exception as e:
        print(e)
        return 

def product_images(product,sku,name):
    try:
        product_images = product.find("div", attrs={"class": "mobile-main-slider"}).find_all("img")
        product_images = [x.attrs["data-large-img-url"] for x in product_images]
        images=[]
        for x in product_images[0:4]:
            x=x.replace("/1024/","/500/").replace("/800/","/500/").replace("/1200/","/500/")
            images.append(
            {
                "src": x,
                "name":sku,
                "alt":name,
            })
        return images
    except Exception as e:
        print("error 369439",e)
        return 

def product_attributes(product,sku,name):
    try:
        color = product.find("label", attrs={"class": "color-label"}).text
        sizes = product.find("meta", attrs={"name": "Size"}).attrs["content"].split(",")
        sizes_stock = product.find_all('meta', attrs={'name': re.compile('^StockInfos_*')})

        regular_price = product.find("meta", attrs={"name": "CashPrice_1"}).attrs["content"].replace(".","").split(",")[0]
        sale_price = product.find("meta", attrs={"name": "DiscountPrice_1"}).attrs["content"].replace(".","").split(",")[0]
        if regular_price==sale_price:
            try:
                sale_price = valid.find("div", attrs={"class": "basket-discount"}).text.replace("TL","").replace(".","").strip().split(",")[0]
            except:
                pass


        color_size = {}

        for i in range(len(sizes)) :
            if sizes_stock[i].attrs["content"] != "0":
                size=size_translate(sizes[i],"lc_waikiki")
                try:
                    color_size[color]["sizes"].append(size)
                except:
                    color_size[color]={
                            "regular_price":regular_price,
                            "sale_price":sale_price,
                            "sizes":[size]
                            }
                    
        image=product.find("div", attrs={"class": "mobile-main-slider"}).find("img").attrs["data-large-img-url"]

        color_size[color]["image"]={
                "src": image,
                "name":sku,
                "alt":name,
            }

        validation_links = product.find("div", attrs={"class": "colors-area"}).find_all("a")[1:]
        validation_links = ["https://www.lcwaikiki.com"+x.attrs["href"] for x in validation_links]


        for i in validation_links:
            try:
                valid= BeautifulSoup(requests.get(i,headers=headers).text, 'html.parser')        
            except:
                return
            
            color = valid.find("label", attrs={"class": "color-label"}).text

            regular_price = valid.find("meta", attrs={"name": "CashPrice_1"}).attrs["content"].replace(".","").split(",")[0]
            sale_price = valid.find("meta", attrs={"name": "DiscountPrice_1"}).attrs["content"].replace(".","").split(",")[0]
            if regular_price==sale_price:
                try:
                    sale_price = valid.find("div", attrs={"class": "basket-discount"}).text.replace("TL","").replace(".","").strip().split(",")[0]
                except:
                    pass

            sizes = valid.find("meta", attrs={"name": "Size"}).attrs["content"].split(",")
            sizes_stock = valid.find_all('meta', attrs={'name': re.compile('^StockInfos_*')})

            for i in range(len(sizes)) :
                if sizes_stock[i].attrs["content"] != "0":
                    size=size_translate(sizes[i],"lc_waikiki")
                    try:
                        color_size[color]["sizes"].append(size)
                    except:
                        color_size[color]={
                                "regular_price":regular_price,
                                "sale_price":sale_price,
                                "sizes":[size]
                                }
            image=valid.find("div", attrs={"class": "mobile-main-slider"}).find("img").attrs["data-large-img-url"]

            color_size[color]["image"]={
                    "src": image,
                    "name":sku,
                    "alt":name,
                }
        return color_size
    except Exception as e:
        print("error 341254",e)
        return



def crawler(url,categories):
    data={}
    sex_id=categories[0]
    try:
        product=BeautifulSoup(requests.get(url,headers=headers).text,'html.parser')
        # print(json.dumps(product, indent=2))
    except:
        print("error 475335",url)
        return

    sku = product_sku(product)
    sex=site_categories(id=sex_id)
    name = product_name(product,url,sex,sku)
    short_name = name.split("-")[0]
    images = product_images(product,sku,short_name)
    attributes = product_attributes(product,sku,short_name)
    description = product_description(categories[2],sex,sku,short_name)
    brand = site_brands(name="lc_waikiki")

    data["p_url"]=url
    data["p_sku"] = sku
    data["p_name"] = name
    data["p_brand"] = brand
    data["p_images"] = images
    data["p_attributes"] = attributes
    data["p_categories"] = categories
    # data["p_description"] = description

    # a=json.dumps(data, indent=2)
    if sku and name and images and attributes:return data 
    else:
        print("product does not scrapped",url)
        return


def crawler_update(url,name,sku):
    data={}
    try:
        product=BeautifulSoup(requests.get(url,headers=headers).text,'html.parser')
        # print(json.dumps(product, indent=2))
    except:
        print("error 475335",url)
        return
    
    short_name = name.split("-")[0]
    images=product_images(product,sku,short_name)
    attributes = product_attributes(product,sku,short_name)

    data["p_images"] = images
    data["p_attributes"] = attributes

    if images and attributes:return data 
    else:
        print("product does not scrapped",url)
        return

# from core.add_to_wp import add_to_wp

# categories=[{"id":"91"},{"id":"112"},{"id":"194"}]

# data=crawler("https://www.lcwaikiki.com/tr-TR/TR/urun/LC-WAIKIKI/kadin/Yagmurluk/6095985/2634664",categories)
# print(data)
# add_to_wp(data=data,brand="lc_waikiki")