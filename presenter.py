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
    url = "OT/Bereshit/Bereshit03.htm"

    verses = parser.parse(url)
    print verses[0].text
    txt = ''
    for v in verses:
        line = u'<small>{}</small>{}'.format(v.num, v.text)
        if v.is_paragraph:
            line = "<p>" + line
        txt += line
    print txt

    app = QApplication(sys.argv)

    presenter = Presenter(txt)
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()

