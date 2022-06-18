import os
import requests

print("Welcome to IsItDown.py!")
print("Please write a URL or URLS you want to check. (separated by comma)")

URLS = input().split(",")

print(URLS)
# os.system('clear')