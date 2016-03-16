from PyQt5.QtWidgets import QDialog, QInputDialog
from Commands.CommandType import CommandType
from Layouts.CommandTypeEditWidget import Ui_BTSerialCommandTypeEditDialog

class CommandTypeEdit(QDialog):
	textType = True

	def __init__(self, parent = None, name = None, code = None, description = None, textType = True):
		QDialog.__init__(self, parent)
		self.ui = Ui_BTSerialCommandTypeEditDialog()
		self.ui.setupUi(self)
		self.setupUIActions()
		self.applyValues(name, code, description, textType)

	def setupUIActions(self):
		self.ui.radioButtonText.toggled.connect(self.commandTypeToggled)
		self.ui.toolButtonAddByte.clicked.connect(self.addItemByte)
		self.ui.toolButtonAddParam.clicked.connect(self.addItemParam)
		self.ui.toolButtonMoveDown.clicked.connect(self.moveItemDown)
		self.ui.toolButtonMoveUp.clicked.connect(self.moveItemUp)
		self.ui.toolButtonRemove.clicked.connect(self.removeItem)

		self.ui.groupBoxCommandBytes.setVisible(False)
		self.adjustSize()

	def applyValues(self, name, code, description, textType):
		if name is not None:
			self.ui.lineEditName.setText(str(name))
		if description is not None:
			self.ui.lineEditDescription.setText(str(description))
		self.textType = bool(textType)
		if not self.textType:
			self.ui.radioButtonByte.toggle()
		if code is not None:
			if self.textType:
				self.ui.lineEditCodeString.setText(str(code))
			else:
				for i in range(len(code)):
					if code[i] == '%':
						self.ui.listWidgetBytes.addItem("%" + str(code[i+1]))
					elif (i == 0) or (code[i-1] != '%'):
						self.ui.listWidgetBytes.addItem(str(code[i]))

	def commandTypeToggled(self, textType = True):
		self.ui.lineEditCodeString.setVisible(textType)
		self.ui.groupBoxCommandBytes.setVisible(not textType)
		self.adjustSize()
		self.textType = textType

	def addItemByte(self):
		inputOk = True
		byteValue, inputOk = QInputDialog.getInt(self, "BTSerial - enter byte value", "Enter command byte value (0 - 255).", min = 0, max = 255)
		if inputOk == False:
			return
		self.ui.listWidgetBytes.addItem(str(byteValue))

	def addItemParam(self):
		inputOk = True
		paramLen, inputOk = QInputDialog.getInt(self, "BTSerial - enter byte value", "Enter param length in bytes (1 - 4).", min = 1, max = 4)
		if inputOk == False:
			return
		self.ui.listWidgetBytes.addItem("%" + str(paramLen))

	def moveItemDown(self):
		count = self.ui.listWidgetBytes.count()
		row = self.ui.listWidgetBytes.currentRow()
		if (count <= 1) or (row == count - 1) or (row < 0):
			return
		commandItem = self.ui.listWidgetBytes.takeItem(row)
		self.ui.listWidgetBytes.insertItem(row + 1, commandItem)
		self.ui.listWidgetBytes.setCurrentRow(row + 1)

	def moveItemUp(self):
		count = self.ui.listWidgetBytes.count()
		row = self.ui.listWidgetBytes.currentRow()
		if (count <= 1) or (row <= 0):
			return
		commandItem = self.ui.listWidgetBytes.takeItem(row)
		self.ui.listWidgetBytes.insertItem(row - 1, commandItem)
		self.ui.listWidgetBytes.setCurrentRow(row - 1)

	def removeItem(self):
		row = self.ui.listWidgetBytes.currentRow()
		if row == -1:
			return
		self.ui.listWidgetBytes.takeItem(row)

	def getName(self):
		return self.ui.lineEditName.text()

	def getDescription(self):
		return self.ui.lineEditDescription.text()

	def getIstextType(self):
		return self.ui.radioButtonText.isChecked()

	def getCode(self):
		if(self.getIstextType()):
			return self.ui.lineEditCodeString.text()
		else:
			code = ""
			for i in range(self.ui.listWidgetBytes.count()):
				itemText = self.ui.listWidgetBytes.item(i).text()
				if itemText[0] == '%':
					code += itemText
				else:
					code += chr(int(itemText))
			return code

	@staticmethod
	def getCommandType(parent = None, name = None, code = None, description = None, textType = True):
		newCommandDialog = CommandTypeEdit(parent, name, code, description, textType)
		accepted = newCommandDialog.exec_()
		if accepted == QDialog.Rejected:
			return (None, False)
		name = newCommandDialog.getName()
		code = newCommandDialog.getCode()
		description = newCommandDialog.getDescription()
		return (CommandType(name, code, description), True)
