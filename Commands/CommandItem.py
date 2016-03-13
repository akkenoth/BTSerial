from PyQt5.QtWidgets import QListWidgetItem
from Commands.CommandType import CommandType

class CommandItem(QListWidgetItem):
	name = None
	code = None
	description = None

	def __init__(self, commandType, *parameters):
		if not isinstance(commandType, CommandType):
			raise TypeError("CommandItem: commandType should be an instance of CommandType class.")
		self.name = commandType.name
		text = self.name + "("
		for p in parameters:
			text += p + ", "
		text = text[:-2] + ")"

		try:
			self.code = commandType.code % parameters
		except TypeError as e:
			raise TypeError("CommandItem: one or more parameters didn't match expected types: " + e.msg)
		self.code.encode('ascii', 'ignore')
		self.description = commandType.description

		QListWidgetItem.__init__(self)
		self.setText(text)
		self.setToolTip(self.code + " | " + self.description)
