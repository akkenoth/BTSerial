import bluetooth

from PyQt5.QtWidgets import QDialog
from Layouts.DeviceSelectorWidget import Ui_DeviceSelectorDialog
from UI.DeviceItem import DeviceItem

class DeviceSelector(QDialog):
	connection = None

	def __init__(self, parent = None):
		QDialog.__init__(self, parent)
		self.ui = Ui_DeviceSelectorDialog()
		self.ui.setupUi(self)
		self.setupUIActions()

	def setupUIActions(self):
		self.ui.labelScanningDevices.setVisible(False)
		self.ui.labelScanningServices.setVisible(False)

		self.ui.pushButtonScan.released.connect(self.startDevicesScan)

		###TODO: fix
		#self.ui.listWidgetDevices.itemClicked.connect(self.ui.buttonBoxDevices.setEnabled(True))
		#self.ui.listWidgetServices.itemClicked.connect(self.ui.buttonBoxServices.setEnabled(True))
		self.ui.lineEditPort.textEdited.connect(self.portTextEdited)

		self.ui.buttonBoxService.accepted.connect(self.startServicesScan)
		self.ui.buttonBoxService.rejected.connect(self.reject)

		self.adjustSize()

	def portTextEdited(self, text):
		self.ui.buttonBoxServices.setEnabled(bool(str(text).strip()))

	def startDevicesScan(self):
		self.ui.pushButtonScan.setEnabled(False)
		self.ui.labelScanningDevices.setVisible(True)
		self.adjustSize()
		devices = []
		try:
			devices = bluetooth.discover_devices(duration = 5, lookup_names = True)
		except Exception as e:
			print("Error: %s\n" % str(e))
			self.ui.labelScanningDevices.setText("Error scanning: %s" % str(e))
			self.ui.pushButtonScan.setEnabled(True)
			return

		if len(devices) is 0:
			self.ui.labelScanningDevices.setText("No devices found!")
			self.ui.pushButtonScan.setEnabled(True)
		else:
			self.ui.labelScanningDevices.setVisible(False)
			listWidgetDevices.setEnabled(True)
			for addr, name in devices:
				deviceItem = DeviceItem(self, addr, name)
				self.ui.listWidgetDevices.addItem(deviceItem)
			self.adjustSize()

	def startServicesScan(self):
		print("startServicesScan!")

	def getConnection(self):
		return self.connection

	@staticmethod
	def connect(parent = None):
		selector = DeviceSelector(parent)
		accepted = selector.exec_()
		if accepted == QDialog.Rejected:
			return None
		return selector.getConnection()
