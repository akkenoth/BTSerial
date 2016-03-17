import bluetooth
import sys
from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal

class BluetoothWorker(QThread):
	exiting = False
	mode = None

	message = pyqtSignal(str, str)
	deviceFound = pyqtSignal(list)

	def __init__(self, parent = None):
		QThread.__init__(self, parent)

	def __del__(self):
		print("BW: cleaning up & exiting...")
		sys.stdout.flush()
		self.exiting = True
		self.wait()

	def scanForDevices(self):
		self.mode = "scan"

	def run(self):
		while not self.exiting:
			if self.mode is "scan":
				self.message.emit("BW: scanning for devices...", "log")
				devices = bluetooth.discover_devices(duration = 2, lookup_names = True)
				self.message.emit("BW: found %d devices!" % len(devices), "log")
				for addr, name in devices:
					self.message.emit("BW: found %s (%s)" % (name, addr), "log")

				self.deviceFound.emit(devices)
				self.mode = None
			else:
				print("thread running!")
				sleep(1)
