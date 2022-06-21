from unittest import result
from extract import extract
import requests
from bs4 import BeautifulSoup

def extract_info(html):
    location = html.find("td",{"class":"local"}).text
    title = html.find("td", {"class":"title"}).find("span", {"class":"company"}).text
    time = html.find("td", {"class":"data"}).string
    pay = html.find("td", {"class":"pay"}).text
    reg_date = html.find("td", {"class":"regDate"}).text
    print(f'{location}/ {title}/ {time}/ {pay}/ {reg_date}')

def access_info(brand_url_list):
    for brand_url in brand_url_list:
        result = requests.get(brand_url)
        soup = BeautifulSoup(result.text, "html.parser")
        NormalInfo = soup.find("div", {"id":"NormalInfo"})
        table = NormalInfo.find("tbody")
        table_row_list = table.find_all("tr",{"class":""})
        for tr in table_row_list:
            extract_info(tr)

brand_url_list, brand_name_list = extract()
access_info(brand_url_list)