import os
from URL_check import URL_check

answer = "y"
while answer is "y":
    URL_check()
    answer = input("do you want to play again? y/n ")
    if answer is "n":
        pass
    else:
        os.system('clear')