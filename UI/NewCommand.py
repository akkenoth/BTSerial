from PyQt5.QtWidgets import QDialog, QInputDialog
from Layouts.NewCommandWidget import Ui_BTSerialNewCommandDialog

class NewCommand(QDialog):
	textBased = True

	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.ui = Ui_BTSerialNewCommandDialog()
		self.ui.setupUi(self)
		self.setupUIActions()

	def setupUIActions(self):
		self.ui.radioButtonText.toggled.connect(self.commandTypeToggled)
		self.ui.toolButtonAddByte.clicked.connect(self.addItemByte)
		self.ui.toolButtonAddParam.clicked.connect(self.addItemParam)
		self.ui.toolButtonMoveDown.clicked.connect(self.moveItemDown)
		self.ui.toolButtonMoveUp.clicked.connect(self.moveItemUp)
		self.ui.toolButtonRemove.clicked.connect(self.removeItem)

		self.ui.groupBoxCommandBytes.setVisible(False)
		self.adjustSize()

	def commandTypeToggled(self, textBased = True):
		self.ui.lineEditCodeString.setVisible(textBased)
		self.ui.groupBoxCommandBytes.setVisible(not textBased)
		self.adjustSize()
		self.textBased = textBased

	def addItemByte(self):
		inputOk = True
		byteValue, inputOk = QInputDialog.getInt(self, "BTSerial - enter byte value", "Enter command byte value (0 - 255).", min = 0, max = 255)
		if inputOk == False:
			return
		self.ui.listWidgetBytes.addItem(str(byteValue))

	def addItemParam(self):
		inputOk = True
		paramLen, inputOk = QInputDialog.getInt(self, "BTSerial - enter byte value", "Enter param length in bytes (0 - 4).", min = 0, max = 4)
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
