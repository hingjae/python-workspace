from unittest import result
from extract import extract
import requests
from bs4 import BeautifulSoup
from save import save_to_file

def extract_info(html):
    try:
        location = html.find("td",{"class":"local"}).text
        title = html.find("td", {"class":"title"}).find("span", {"class":"company"}).text
        time = html.find("td", {"class":"data"}).string
        pay = html.find("td", {"class":"pay"}).text
        reg_date = html.find("td", {"class":"regDate"}).text
    except:
        return
    # print(f'{location}/ {title}/ {time}/ {pay}/ {reg_date}')
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

brand_url_list = extract()
access_info(brand_url_list)
