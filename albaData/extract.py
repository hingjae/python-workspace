import os
import csv
import requests
from bs4 import BeautifulSoup

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
