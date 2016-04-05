from PyQt5.QtWidgets import QListWidgetItem

class ServiceItem(QListWidgetItem):
	servicePort = None
	serviceName = None

	def __init__(self, parent = None, port = None, name = None):
		QListWidgetItem.__init__(self)
		self.servicePort = port
		self.serviceName = name

		self.setText("%s: %s" % (str(self.servicePort), str(self.serviceName)))
