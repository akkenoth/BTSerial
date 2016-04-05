from PyQt5.QtWidgets import QListWidgetItem

class DeviceItem(QListWidgetItem):
	deviceAddress = None
	deviceName = None

	def __init__(self, parent = None, address = None, name = None):
		QListWidgetItem.__init__(self)
		self.deviceAddress = address
		self.deviceName = name

		self.setText("%s [%s]" % (str(self.deviceName), str(self.deviceAddress)))
