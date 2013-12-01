import sys
from PyQt4.QtGui import *
import parser

class Presenter(QWidget):
    def __init__(self, text):
        super(Presenter, self).__init__()
        self.initUI(text)
    
    def initUI(self, text):
        self.resize(550, 550)
        self.move(400, 200)
        self.setWindowTitle('test')

        txtEdit = QTextEdit(self)
        txtEdit.setText(text)

        self.show()

def main():
    txt = parser.doSomething()
    print txt

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

