import sys
from PyQt5.QtWidgets import QListWidgetItem
from Commands.CommandType import CommandType

class CommandItem(QListWidgetItem):
	name = None
	delay = 0
	code = None
	description = None
	text = None

	def __init__(self, delay, commandType, cmdParams = []):
		if (not isinstance(delay, int)) or (delay < 0):
			raise TypeError("CommandItem: delay must be a positive integer.")
		self.delay = delay
		if commandType is None:
			self.text = "Delay (" + self.delay + ")"
			self.code = "DELAY"
			self.description = "Delay of " + self.delay + " milliseconds"
		else:
			if not isinstance(commandType, CommandType):
				raise TypeError("CommandItem: commandType should be an instance of CommandType class.")
			self.name = commandType.name
			text = self.name + "("
			for p in cmdParams:
				text += str(p) + ", "
			self.text = text[:-2] + ")"

			currentParam = 0
			cmdCode = commandType.code
			cmdCodeCopy = commandType.code

			#iterate over copy to avoid out of range error - we're modifying cmdCode's length inside the loop 
			for i in range(len(cmdCodeCopy)):
				if cmdCodeCopy[i] is not '%':
					continue
				if cmdCodeCopy[i+1] == '1':
					cmdCode = cmdCode.replace("%1", str(chr(cmdParams[currentParam])), 1)
				elif cmdCodeCopy[i+1] == '2':
					cmdCode = cmdCode.replace("%2", str(chr(int(cmdParams[currentParam] / 255)) + chr(cmdParams[currentParam] % 255)), 1)
				currentParam += 1
			self.code = cmdCode.encode('ascii', 'ignore')
			self.description = commandType.description

		QListWidgetItem.__init__(self)
		self.setText(self.text)
		self.setToolTip(str(self.code).replace("b", "", 1) + " - " + self.description)
