import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from BTSerialUI import Ui_MainWindow

class BTSerialProgram(Ui_MainWindow):
	def __init__(self, mainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(mainWindow)

		self.pushButtonAddToQueue.clicked.connect(self.addCommandToQueue)

	def addCommandToQueue(self):
		command = self.listWidgetCommands.currentItem()
		if command is None:
			return
		commandTxt = command.text()
		self.listWidgetQueue.addItem(commandTxt)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = QtWidgets.QMainWindow()

	prog = BTSerialProgram(mainWindow)
	mainWindow.show()
	sys.exit(app.exec_())
