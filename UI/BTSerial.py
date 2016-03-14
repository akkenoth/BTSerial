import json
import sys

import pprint

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QInputDialog

from Commands.CommandItem import CommandItem
from Commands.CommandType import CommandType
from UI.CommandTypeEdit import CommandTypeEdit
from Layouts.MainWindow import Ui_BTSerialMainWindow

class BTSerial(QMainWindow):
	ui = None
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_BTSerialMainWindow()
		self.ui.setupUi(self)
		self.setupUIActions()

	def setupUIActions(self):
		self.ui.actionConnect.triggered.connect(self.connectToDevice)
		self.ui.actionDisconnect.triggered.connect(self.disconnectFromDevice)
		self.ui.actionLoadQueue.triggered.connect(self.loadCommandQueue)
		self.ui.actionLoadTypes.triggered.connect(self.loadCommandList)
		self.ui.actionQuit.triggered.connect(self.closeConfirmation)
		self.ui.actionSaveQueue.triggered.connect(self.saveCommandQueue)
		self.ui.actionSaveTypes.triggered.connect(self.saveCommandList)
		self.ui.actionSettings.triggered.connect(self.openSettings)
		self.ui.listWidgetCommands.itemDoubleClicked.connect(self.createCommandItem)
		self.ui.listWidgetCommands.setSortingEnabled(True)
		self.ui.pushButtonAddCommandType.clicked.connect(self.createCommandType)
		self.ui.pushButtonAddDelay.clicked.connect(self.addDelayToQueue)
		self.ui.pushButtonAddToQueue.clicked.connect(self.createCommandItemButtonWrapper)
		self.ui.pushButtonDeleteCommandItem.clicked.connect(self.deleteCommandItem)
		self.ui.pushButtonDeleteCommandType.clicked.connect(self.deleteCommandType)
		self.ui.pushButtonEditCommandItem.clicked.connect(self.editCommandItem)
		self.ui.pushButtonEditCommandType.clicked.connect(self.editCommandType)
		self.ui.pushButtonExecute.clicked.connect(self.executeCommands)
		self.ui.pushButtonMoveCommandItemDown.clicked.connect(self.moveCommandDownQueue)
		self.ui.pushButtonMoveCommandItemUp.clicked.connect(self.moveCommandUpQueue)

	### Program menu ###

	def connectToDevice(self):
		pass

	def disconnectFromDevice(self):
		pass

	def openSettings(self):
		pass

	def applySettings(self):
		pass

	### Commands menu ###

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
		invalidStructure = False
		for c in data["commands"]:
			if not(("name" in c) and ("code" in c) and (type(c["name"]) is str)):
				invalidStructure = True
				break
			name = str(c["name"])
			description = ""
			if ("description" in c) and (type(c["description"]) is str):
				description = str(c["description"])
			textType = True
			if ("textType" in c) and (type(c["textType"]) is bool):
				textType = bool(c["textType"])
			if (textType and not (type(c["code"]) is str)) or ((not textType) and not (type(c["code"]) is list)):
				invalidStructure = True
				break

			try:
				command = CommandType(name, c["code"], description, textType)
			except:
				e = sys.exc_info()[0]
				pprint.pprint(c["code"])
				sys.stdout.flush()
				print("error: " + str(e))
				sys.stdout.flush()
				invalidStructure = True
				break
			commandTypeList.append(command)

		if invalidStructure is True:
			QMessageBox.warning(self, "BTSerial - Error", "Invalid command structure.", QMessageBox.Ok, QMessageBox.Ok)
			return

		self.ui.listWidgetCommands.clear()
		for c in commandTypeList:
			self.ui.listWidgetCommands.addItem(c)

	def saveCommandList(self):
		pass

	def loadCommandQueue(self):
		pass

	def saveCommandQueue(self):
		pass

	### Command types actions ###

	def createCommandType(self):
		commandType, inputOk = CommandTypeEdit.getCommandType(self)
		if inputOk == False:
			return
		self.ui.listWidgetCommands.addItem(commandType)

	def editCommandType(self):
		pass

	def deleteCommandType(self):
		pass

	### Command item creation ###

	def createCommandItemButtonWrapper(self):
		self.createCommandItem(self.ui.listWidgetCommands.currentItem())

	def createCommandItem(self, commandType):
		if commandType is None:
			return
		cmdParams = []
		code = commandType.code
		inputOk = True
		for i in range(len(code)):
			if code[i] is not '%':
				continue
			# Unsafe!
			if code[i+1] == '1':
				label = "Enter value for parameter " + str(cmdParams.__len__() + 1)
				value, inputOk = QInputDialog.getInt(self, "BTSerial - enter parameter value", label, min = 0, max = 255)
			elif code[i+1] == '2':
				label = "Enter value for parameter " + str(cmdParams.__len__() + 1)
				value, inputOk = QInputDialog.getInt(self, "BTSerial - enter parameter value", label, min = 0, max = 65535)
			else:
				QMessageBox.warning(self, "BTSerial - Error", "Invalid command code, cannot parse.", QMessageBox.Ok, QMessageBox.Ok)
				return
			if inputOk == False:
				return
			cmdParams.append(int(value))
		item = CommandItem(0, commandType, cmdParams)
		self.ui.listWidgetQueue.addItem(item)

	def addDelayToQueue(self):
		inputOk = True
		delay, inputOk = QInputDialog.getInt(self, "BTSerial - enter delay value", "Enter delay length (in milliseconds).", min = 0, max = 10000)
		if inputOk == False:
			return
		item = CommandItem(delay)
		self.ui.listWidgetQueue.addItem(item)

	### Command item actions ###

	def moveCommandUpQueue(self):
		count = self.ui.listWidgetQueue.count()
		row = self.ui.listWidgetQueue.currentRow()
		if (count <= 1) or (row <= 0):
			return
		commandItem = self.ui.listWidgetQueue.takeItem(row)
		self.ui.listWidgetQueue.insertItem(row - 1, commandItem)
		self.ui.listWidgetQueue.setCurrentRow(row - 1)

	def moveCommandDownQueue(self):
		count = self.ui.listWidgetQueue.count()
		row = self.ui.listWidgetQueue.currentRow()
		if (count <= 1) or (row == count - 1) or (row < 0):
			return
		commandItem = self.ui.listWidgetQueue.takeItem(row)
		self.ui.listWidgetQueue.insertItem(row + 1, commandItem)
		self.ui.listWidgetQueue.setCurrentRow(row + 1)

	def editCommandItem(self):
		pass

	def deleteCommandItem(self):
		row = self.ui.listWidgetQueue.currentRow()
		if row == -1:
			return
		confirmation = QMessageBox.Yes
		# skip confirm for delays
		if self.ui.listWidgetQueue.item(row).delay == 0:
			confirmation = QMessageBox.question(self, "BTSerial - Confirm delete", "Confirm deleting command from queue",
				QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if confirmation == QMessageBox.Yes:
			self.ui.listWidgetQueue.takeItem(row)

	### Execute actions ###

	def executeCommands(self):
		pass

	### Special handlers ###

	def closeEvent(self, event):
		event.ignore()
		self.closeConfirmation()

	def closeConfirmation(self):
		confirmation = QMessageBox.question(self, "BTSerial - Quit?", "Are you sure you want to quit?",
			QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if confirmation == QMessageBox.Yes:
			QCoreApplication.instance().quit()
