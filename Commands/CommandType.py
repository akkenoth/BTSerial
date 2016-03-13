from PyQt5.QtWidgets import QListWidgetItem

class CommandType(QListWidgetItem):
	name = None
	code = None
	description = None

	def __init__(self, name, code, description = ""):
		QListWidgetItem.__init__(self)
		self.name = name
		self.code = code
		self.description = description
		self.setText(self.name + " ["+ self.code + "]")
		self.setToolTip(self.description)
