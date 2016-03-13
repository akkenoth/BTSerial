import sys
import json
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from UI.MainWindow import Ui_BTSerialMainWindow
from Commands.CommandItem import CommandItem
from Commands.CommandType import CommandType

from pprint import pprint

class BTSerial(QMainWindow):
	ui = None
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_BTSerialMainWindow()
		self.ui.setupUi(self)
		self.setupUIActions()

	def setupUIActions(self):
		self.ui.pushButtonAddToQueue.clicked.connect(self.addCommandToQueue)
		self.ui.actionQuit.triggered.connect(self.closeConfirmation)
		self.ui.actionLoadList.triggered.connect(self.loadCommandList)

	def addCommandToQueue(self):
		command = self.ui.listWidgetCommands.currentItem()
		if command is None:
			return
		commandTxt = command.text()
		self.ui.listWidgetQueue.addItem(commandTxt)

	def loadCommandList(self):
		# Add confirmation if there are commands on the list
		filename = QFileDialog.getOpenFileName(self, "BTSerial - load command list")
		if not filename[0]:
			return

		data = None
		try:
			with open(filename[0], 'r') as data_raw:
				data = json.load(data_raw)
		except IOError:
			QMessageBox.warning(self, "BTSerial - Error", "Error reading file: " + filename[0], QMessageBox.Ok, QMessageBox.Ok)
			return
		except JSONDecodeError as error:
			QMessageBox.warning(self, "BTSerial - Error", "Error parsing file: " + e.msg, QMessageBox.Ok, QMessageBox.Ok)
			return
		if not isinstance(data["commands"], list):
			QMessageBox.warning(self, "BTSerial - Error", "\"commands\" object is not an array.", QMessageBox.Ok, QMessageBox.Ok)
			return

		commandTypeList = []
		for c in data["commands"]:
			if not (isinstance(c["name"], str) and isinstance(c["code"], str) and isinstance(c["description"], str)):
				QMessageBox.warning(self, "BTSerial - Error", "Invalid command structure.", QMessageBox.Ok, QMessageBox.Ok)
				print("invalid command structure")
				return
			command = CommandType(c["name"], c["code"], c["description"])
			commandTypeList.append(command)

		self.ui.listWidgetCommands.clear()
		for c in commandTypeList:
			self.ui.listWidgetCommands.addItem(c)

	def closeEvent(self, event):
		event.ignore()
		self.closeConfirmation()

	def closeConfirmation(self):
		confirmation = QMessageBox.question(self, "BTSerial - Quit?", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if confirmation == QMessageBox.Yes:
			QCoreApplication.instance().quit()
