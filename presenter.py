#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from PyQt4.QtGui import *
import parser


class Presenter(QWidget):
    def __init__(self, text):
        super(Presenter, self).__init__()
        self.initUI(text)
    
    def initUI(self, text):
        txt = ""
        con = lite.connect('scriptures.db')

        with con:
            cur = con.cursor()    
            cur.execute("SELECT Name, Hebname FROM Books WHERE Name=:name", {"name": "Bereshit"})

            rows = cur.fetchall()
            txt = rows[-1]
            print txt

        self.resize(550, 550)
        self.move(400, 200)
        self.setWindowTitle('test')

        txtEdit = QTextEdit(self)
        txtEdit.setText(txt[1])

        self.show()

def main():
    txt = parser.doSomething()
    # print txt

    app = QApplication(sys.argv)

    # w = QWidget()
    # w.resize(550, 550)
    # w.move(400, 200)
    # w.setWindowTitle('test')

    # txtEdit = QTextEdit()
    # txtEdit.setText('bla')
    # w.show()

    presenter = Presenter(txt)
    sys.exit(app.exec_())

if __name__ == '__main__':
	main()

