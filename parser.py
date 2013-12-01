import sys
from bs4 import BeautifulSoup

def doSomething():
    f = open("OT/Bereshit/Bereshit01.htm","r")
    html_doc = f.read()

    soup = BeautifulSoup(html_doc)
    # print(soup.get_text())

    print('all good inside parser')
    return soup.find_all(["p"])[0].get_text()

