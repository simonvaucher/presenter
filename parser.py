#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import sqlite3 as lite
from bs4 import BeautifulSoup
from bs4 import NavigableString

class Verse():
    book = 0
    chapter = 0
    num = 0
    translation = 0
    text = ''
    alt_text = ''
    is_paragraph = False

def doSomething():
    f = open("OT/Bereshit/Bereshit02.htm","r")
    html_doc = f.read()

    soup = BeautifulSoup(html_doc)
    # print(soup.get_text())

    print('all good inside parser')
    return soup.find_all(["p"])[0].get_text()

def parse(url):
    f = open(url,"r")
    html_doc = f.read()

    soup = BeautifulSoup(html_doc)
    p = soup.p
    verses = []
    verse = Verse()
    num = 0
    record = False
    record_next = False
    is_paragraph_next = True
    close_tag = ''

    for e in p.next_elements:
        if not isinstance(e, NavigableString):
            if e.name == 'b':
                if 'class' in e.attrs:
                    num += 1
                    verse.num = num
                    if is_paragraph_next:
                        verse.is_paragraph = True
                        is_paragraph_next = False
                    record_next = True
                continue # this is for the html-1 b tag, ARGH


            if e.name in ['big', 'small']:
                verse.text += '<' + e.name + '>'
                close_tag = '</' + e.name + '>'
                continue

            if e.get('name'):
                record = False
                verses.append(verse)
                verse = Verse()
                continue

            if e.name == 'p':
                is_paragraph_next = True
                continue

            if e.name == 'a' and 'href' in e.attrs:
                record = False


        if record_next:
            record_next = False
            record = True
            continue

        if record:
            verse.text += unicode(e)
            if close_tag:
                verse.text += close_tag
                close_tag = ''

    verses.append(verse) # don't forget to append last verse...
    return verses


# con = lite.connect('scriptures.db')
# with con:
#     cur = con.cursor()
#     # cur.execute("DROP TABLE Books")
#     # cur.execute("CREATE TABLE Books(Id INTEGER PRIMARY KEY, Name VARCHAR, Hebname VARCHAR)")
#     bla = doSomething()
#     cur.execute("INSERT INTO Books(Name, Hebname) VALUES('Bereshit', ?)", (bla,))
