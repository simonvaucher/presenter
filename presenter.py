#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import parser

class Presenter(QWidget):
    def __init__(self, text):
        super(Presenter, self).__init__()
        self.initUI(text)
    
    def initUI(self, text):
        # txt = ""
        # con = lite.connect('scriptures.db')

        # with con:
        #     cur = con.cursor()    
        #     cur.execute("SELECT Name, Hebname FROM Books WHERE Name=:name", {"name": "Bereshit"})

        #     rows = cur.fetchall()
        #     txt = rows[-1]
        #     print txt

        self.resize(550, 550)
        self.move(400, 200)
        self.setWindowTitle('presenter / parser test')

        txtEdit = QTextEdit()
        txtEdit.setText(text)

        hbox = QHBoxLayout()
        # hbox.addStretch(0)
        hbox.addWidget(txtEdit)
        self.setLayout(hbox)   
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
def main():
    # txt = parser.doSomething()
    # print txt[::-1]
    # url = "OT/Bereshit/Bereshit01.htm"
    # url = "NT/Modern/Luke/Luke24.htm"
    # url = "OT/Tehillim/Tehillim49.htm"

    # CRAZY TABLE STUFF
    url = "OT/Daniel/Daniel02.htm"

    verses = parser.parse(url)

    txt = '<p>num of verses:{}</p>'.format(len(verses))
    for v in verses:
        line = u'<small> {}</small> {}<em><strong> {}</strong></em>'.format(v.num, v.text, v.alt_text)
        if v.is_paragraph:
            line = "<p>" + line
        txt += line
        print line
        # print v.num
        # print v.text
        # print v.alt_text

    app = QApplication(sys.argv)

    presenter = Presenter(txt)
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()

