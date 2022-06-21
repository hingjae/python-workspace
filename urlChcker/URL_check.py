import requests

def URL_check():
    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLS you want to check. (separated by comma)")

    input_URLS = input().split(",")
    URLS = []
    for URL in input_URLS:
        URL = URL.strip()
        URLS.append(URL)

    for URL in URLS:
        if URL.find('.') != -1: #It is URL
            if "http://" in URL:
                try:
                    URL_STATUS = requests.get(URL)
                    print(URL+" is up!")
                except:
                    print(URL+" is down!")
            else:
                URL = "http://" + URL
                try:
                    URL_STATUS = requests.get(URL)
                    print(URL+" is up!")
                except:
                    print(URL+" is down!")
        else:
            print("It is not URL")

    