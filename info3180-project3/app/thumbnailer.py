from bs4 import BeautifulSoup
import requests


def matching_words(string_1, string_2):
    count = 0
    string_1 = string_1.split()
    
    for word in string_1:
        if word in string_2:
            count += 1
    return count
    
def good_match(string, num_matching_words):
    string = string.split()
    str_len = len(string)
    if str_len > 0:
        percent =(float(num_matching_words)*100/float(str_len))
        if percent >= 50:
            return True
    return False

def get_data(url):
    try:
        result      = requests.get(url)
        soup        = BeautifulSoup(result.text, "html.parser")
        thumbnails  = []
        title       = ""
        
        if "amazon.com" in url:
            soup_title  = soup.find("span",id="productTitle")
            soup_img    = soup.find_all("img", id="landingImage")
            
            if not soup_img:
                return {"error":1,"data":{},"message":"Unable to extract images."}
            else:
                for img in soup_img:
                    if img["src"] not in thumbnails:
                        thumbnails.append(img["src"])
                
                if soup_title:
                    title = soup_title.string

            return {"error":None,"data":{"title":title, "thumbnails":thumbnails},"message":"Success"}
        
        elif "ebay.com" in url:
            soup_title = soup.find("h1", id="itemTitle")
            soup_img = soup.find_all("img", id="icImg")
            
            if not soup_img:
                return {"error":1,"data":{},"message":"Unable to extract images."}
            else:
                for img in soup_img:
                    if img["src"] not in thumbnails:
                        thumbnails.append(img["src"])
                
                if soup_title:
                    children = []
                    for child in soup_title.children:
                        children.append(child)
                    title = children[1]

            return {"error":None,"data":{"title":title, "thumbnails":thumbnails},"message":"Success"}
        
        else:
            title = soup.title.string
            for img in soup.find_all("img", alt=True):
                alt = img['alt']
                src = img['src']
                numMatchingWords = matching_words(title,alt)
                if good_match(alt, numMatchingWords):
                    if src not in thumbnails and src[-4:]==".jpg" and "sprite" not in src:
                        thumbnails.append(src)
            
            if not thumbnails:
                for img in soup.findAll("img", src=True):
                    if "sprite" not in img["src"] and src[-4:]==".jpg":
                        thumbnails.append(img["src"])
            
            if not thumbnails:
                return {"error":1,"data":{},"message":"Unable to extract images."}
    
            return {"error":None,"data":{"title":title, "thumbnails":thumbnails},"message":"Success"}
    
    except requests.exceptions.RequestException:
        return {"error":2,"data":{},"message":"URL entered is invalid."}
    
    

url1 = "http://www.amazon.com/s/ref=gw_in_av_ntlIg_ara-1?_encoding=UTF8&bbn=10445813011&rh=n%3A7141123011%2Cn%3A10445813011%2Cn%3A7147440011%2Cn%3A1040660%2Cn%3A1045024&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-unrec-col-3&pf_rd_r=0WRZMQ9Q02MNQAXYPBH3&pf_rd_t=36701&pf_rd_p=4301bdc7-c526-4439-9945-c3d07b830d38&pf_rd_i=desktop-unrec"
url2 = "http://www.ebay.com/cln/ebaydealseditor/Moms-Night-Out/224588409015"
url3 = "http://www.amazon.com/s/ref=nb_sb_ss_c_0_7?url=search-alias%3Dfashion-mens-watches&field-keywords=watches&sprefix=watches%2Cundefined%2C243"
url4 = "http://www.ebay.com/itm/35-Piece-Auto-Car-Truck-SUV-Motorcycle-Emergency-Roadside-Kit-/201542299460"
url5 = "http://www.ebay.com/itm/Smart-U8-Bluetooth-Wrist-Watch-Phone-Mate-For-iOS-iPhone-Samsung-Android-/301901798088?hash=item464abfdac8:m:mC_fmv85BHWXlw8mtoGRnlw&item=301901798088&var=&vxp=mtr"
url6 = "http://www.amazon.com/Samsung-S7-Smartphone-International-Gold/dp/B01CJU9MJI/ref=sr_1_4?s=wireless&ie=UTF8&qid=1461126669&sr=1-4&keywords=samsung+s7+edge"
url7 = "http://www.amazon.com/dp/B01D8YMW9Q?psc=1"
url8 = "http://www.amazon.com/Selfie-Amya-Battery-iPhone-GalaxyS7/dp/B01D9D2Z1G/ref=sr_1_9?s=wireless&ie=UTF8&qid=1461126783&sr=1-9&keywords=iphone+7"


#print get_data(url1)
#print get_data(url2)
#print get_data(url3)
#print get_data(url4)
#print get_data(url5)
#print get_data(url6)
#print get_data(url7)
#print get_data(url8)