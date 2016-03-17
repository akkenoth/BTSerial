from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QBrush, QColor, QFont
from PyQt5.QtCore import Qt

class LogItem(QListWidgetItem):
	itemType = None

	def __init__(self, parent = None, message = None, itemType = "log"):
		QListWidgetItem.__init__(self)
		self.itemType = itemType

		if (itemType == "log"):
			self.setText("--- " + str(message))
		elif (itemType == "in"):
			self.setText("<<< " + str(message))
		elif (itemType == "out"):
			self.setText(">>> " + str(message))
		else:
			self.setText(str(message))

		font = QFont()
		font.setFamily("Monospace")
		if (itemType == "in") or (itemType == "out"):
			font.setBold(True)
			font.setWeight(75)
		else:
			font.setBold(False)
			font.setWeight(50)
		self.setFont(font)

		brush = QBrush(QColor(0, 0, 0))
		if (itemType == "in"):
			brush = QBrush(QColor(0, 0, 85))
		elif (itemType == "out"):
			brush = QBrush(QColor(0, 85, 0))
		brush.setStyle(Qt.NoBrush)
		self.setForeground(brush)
