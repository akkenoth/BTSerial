import json
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QInputDialog

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
		self.ui.actionConnect.triggered.connect(self.connectToDevice)
		self.ui.actionDisconnect.triggered.connect(self.disconnectFromDevice)
		self.ui.actionLoad.triggered.connect(self.loadCommandQueue)
		self.ui.actionLoadList.triggered.connect(self.loadCommandList)
		self.ui.actionQuit.triggered.connect(self.closeConfirmation)
		self.ui.actionSave.triggered.connect(self.saveCommandQueue)
		self.ui.actionSaveList.triggered.connect(self.saveCommandList)
		self.ui.actionSettings.triggered.connect(self.openSettings)
		self.ui.listWidgetCommands.itemDoubleClicked.connect(self.addCommandToQueue)
		self.ui.listWidgetCommands.setSortingEnabled(True)
		self.ui.pushButtonAddCommand.clicked.connect(self.createNewCommand)
		self.ui.pushButtonAddDelay.clicked.connect(self.addDelayToQueue)
		self.ui.pushButtonAddToQueue.clicked.connect(self.addCommandToQueueButtonWrapper)
		self.ui.pushButtonDeleteCommand.clicked.connect(self.deleteCommandFromQueue)
		self.ui.pushButtonExecute.clicked.connect(self.executeCommands)
		self.ui.pushButtonMoveCommandDown.clicked.connect(self.moveCommandDownQueue)
		self.ui.pushButtonMoveCommandUp.clicked.connect(self.moveCommandUpQueue)

	def connectToDevice(self):
		pass

	def disconnectFromDevice(self):
		pass

	def openSettings(self):
		pass

	def applySettings(self):
		pass

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
			# TODO: add code validation in CommandType ctor and try/expect here
			command = CommandType(c["name"], c["code"], c["description"])
			commandTypeList.append(command)

		self.ui.listWidgetCommands.clear()
		for c in commandTypeList:
			self.ui.listWidgetCommands.addItem(c)

	def saveCommandList(self):
		pass

	def loadCommandQueue(self):
		pass

	def saveCommandQueue(self):
		pass

	def createNewCommand(self):
		pass

	def addCommandToQueueButtonWrapper(self):
		self.addCommandToQueue(self.ui.listWidgetCommands.currentItem())

	def addCommandToQueue(self, commandType):
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
		pass

	def moveCommandUpQueue(self):
		count = self.ui.listWidgetQueue.count()
		row = self.ui.listWidgetQueue.currentRow()
		if (count <= 1) or (row == 0):
			return
		commandItem = self.ui.listWidgetQueue.takeItem(row)
		self.ui.listWidgetQueue.insertItem(row - 1, commandItem)
		self.ui.listWidgetQueue.setCurrentRow(row - 1)
	
	def moveCommandDownQueue(self):
		count = self.ui.listWidgetQueue.count()
		row = self.ui.listWidgetQueue.currentRow()
		if (count <= 1) or (row == count - 1):
			return
		commandItem = self.ui.listWidgetQueue.takeItem(row)
		self.ui.listWidgetQueue.insertItem(row + 1, commandItem)
		self.ui.listWidgetQueue.setCurrentRow(row + 1)

	def deleteCommandFromQueue(self):
		commandItem = self.ui.listWidgetQueue.currentItem()
		if commandItem is None:
			return
		confirmation = QMessageBox.Yes
		# skip confirm for delays
		if commandItem.delay == 0:
			confirmation = QMessageBox.question(self, "BTSerial - Confirm delete", "Confirm deleting command from queue", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if confirmation == QMessageBox.Yes:
			self.ui.listWidgetQueue.takeItem(self.ui.listWidgetQueue.row(commandItem))

	def executeCommands(self):
		pass

	def closeEvent(self, event):
		event.ignore()
		self.closeConfirmation()

	def closeConfirmation(self):
		confirmation = QMessageBox.question(self, "BTSerial - Quit?", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if confirmation == QMessageBox.Yes:
			QCoreApplication.instance().quit()
