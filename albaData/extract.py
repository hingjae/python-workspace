import os
import requests
from bs4 import BeautifulSoup
from save import save_to_file

os.system("clear")
alba_url = "http://www.alba.co.kr"

def extract_url(html):
    brand_url = html.find("a", {"class":"goodsBox-info"})["href"]
    return brand_url

def extract():
    result = requests.get(alba_url)
    soup = BeautifulSoup(result.text, "html.parser")
    super_brand = soup.find("div",{"id":"MainSuperBrand"})
    brand_list = super_brand.find_all("li", {"class":"impact"}) #find_all은 list로 받는게 좋음.
    count = 0
    brand_url_list = []
    for brand in brand_list:
        count = count+1
        brand_url = extract_url(brand)
        brand_url_list.append(brand_url)
    return brand_url_list

def extract_info(html):
    try:
        location = html.find("td",{"class":"local"}).text
        title = html.find("td", {"class":"title"}).find("span", {"class":"company"}).text
        time = html.find("td", {"class":"data"}).string
        pay = html.find("td", {"class":"pay"}).text
        reg_date = html.find("td", {"class":"regDate"}).text
    except:
        return {'location': "NoneType", 'title': "NoneType", 'time': "NoneType", 'pay': "NoneType", 'reg_date': "NoneType"}
    return {'location': location, 'title': title, 'time': time, 'pay': pay, 'reg_date': reg_date}

def access_info(brand_url_list):
    for brand_url in brand_url_list:
        infos = []
        result = requests.get(brand_url)
        soup = BeautifulSoup(result.text, "html.parser")
        NormalInfo = soup.find("div", {"id":"NormalInfo"})
        table = NormalInfo.find("tbody")
        table_row_list = table.find_all("tr",{"class":""})
        file_name = soup.find("head").find("title").text
        for tr in table_row_list:
            info = extract_info(tr)
            infos.append(info)
            save_to_file(infos, file_name)
