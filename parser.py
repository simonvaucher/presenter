#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3 as lite
from bs4 import BeautifulSoup

def doSomething():
    f = open("OT/Bereshit/Bereshit01.htm","r")
    html_doc = f.read()

    soup = BeautifulSoup(html_doc)
    # print(soup.get_text())

    print('all good inside parser')
    return soup.find_all(["p"])[0].get_text()

print 'hello'

con = lite.connect('scriptures.db')
with con:
    cur = con.cursor()    
    # cur.execute("DROP TABLE Books")
    # cur.execute("CREATE TABLE Books(Id INTEGER PRIMARY KEY, Name VARCHAR, Hebname VARCHAR)")
    bla = doSomething()
    cur.execute("INSERT INTO Books(Name, Hebname) VALUES('Bereshit', ?)", (bla,))
