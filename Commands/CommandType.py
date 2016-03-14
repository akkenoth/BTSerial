from PyQt5.QtWidgets import QListWidgetItem

class CommandType(QListWidgetItem):
	name = None
	code = None
	description = None
	textType = True

	def __init__(self, name, code, description = "", textType = True):
		QListWidgetItem.__init__(self)
		self.name = str(name)
		self.description = str(description)

		if (textType is True) or (type(code) is str):
			self.code = str(code)
		elif type(code) is list:
			self.code = ""
			for i in code:
				if i[0] == '%':
					self.code += str(i)
				elif (i[0] == '0') and (i[1] == 'x'):
					self.code += chr(int(i, 16))
		else:
			raise TypeError("Bad code structure")

		self.setText(self.name + " ["+ str(self.code) + "]")
		self.setToolTip(self.description)
