import sys
from PyQt4.QtGui import *

def main():

	app = QApplication(sys.argv)

	w = QWidget()
	w.resize(250, 150)
	w.move(300, 300)
	w.setWindowTitle('test')
	w.show()

	print 'all good'
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

