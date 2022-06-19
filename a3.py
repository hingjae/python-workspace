import os
import requests

print("Welcome to IsItDown.py!")
print("Please write a URL or URLS you want to check. (separated by comma)")

URLS = input().split(",")
strip_URLS = []
for URL in URLS:
    URL = URL.strip()
    strip_URLS.append(URL)



# os.system('clear')