# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeviceSelectorWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeviceSelectorDialog(object):
	def setupUi(self, DeviceSelectorDialog):
		DeviceSelectorDialog.setObjectName("DeviceSelectorDialog")
		DeviceSelectorDialog.resize(369, 536)
		self.verticalLayout = QtWidgets.QVBoxLayout(DeviceSelectorDialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButtonScan = QtWidgets.QPushButton(DeviceSelectorDialog)
		self.pushButtonScan.setObjectName("pushButtonScan")
		self.verticalLayout.addWidget(self.pushButtonScan)
		self.groupBoxDevices = QtWidgets.QGroupBox(DeviceSelectorDialog)
		self.groupBoxDevices.setEnabled(True)
		self.groupBoxDevices.setObjectName("groupBoxDevices")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxDevices)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.labelScanningDevices = QtWidgets.QLabel(self.groupBoxDevices)
		self.labelScanningDevices.setObjectName("labelScanningDevices")
		self.verticalLayout_2.addWidget(self.labelScanningDevices)
		self.listWidgetDevices = QtWidgets.QListWidget(self.groupBoxDevices)
		self.listWidgetDevices.setEnabled(False)
		self.listWidgetDevices.setObjectName("listWidgetDevices")
		self.verticalLayout_2.addWidget(self.listWidgetDevices)
		self.buttonBoxDevices = QtWidgets.QDialogButtonBox(self.groupBoxDevices)
		self.buttonBoxDevices.setEnabled(False)
		self.buttonBoxDevices.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBoxDevices.setObjectName("buttonBoxDevices")
		self.verticalLayout_2.addWidget(self.buttonBoxDevices)
		self.verticalLayout.addWidget(self.groupBoxDevices)
		self.groupBoxService = QtWidgets.QGroupBox(DeviceSelectorDialog)
		self.groupBoxService.setEnabled(True)
		self.groupBoxService.setObjectName("groupBoxService")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxService)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.labelScanningServices = QtWidgets.QLabel(self.groupBoxService)
		self.labelScanningServices.setEnabled(True)
		self.labelScanningServices.setObjectName("labelScanningServices")
		self.verticalLayout_3.addWidget(self.labelScanningServices)
		self.listWidgetServices = QtWidgets.QListWidget(self.groupBoxService)
		self.listWidgetServices.setEnabled(False)
		self.listWidgetServices.setObjectName("listWidgetServices")
		self.verticalLayout_3.addWidget(self.listWidgetServices)
		self.lineEditPort = QtWidgets.QLineEdit(self.groupBoxService)
		self.lineEditPort.setEnabled(False)
		self.lineEditPort.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.lineEditPort.setText("")
		self.lineEditPort.setObjectName("lineEditPort")
		self.verticalLayout_3.addWidget(self.lineEditPort)
		self.buttonBoxService = QtWidgets.QDialogButtonBox(self.groupBoxService)
		self.buttonBoxService.setEnabled(False)
		self.buttonBoxService.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBoxService.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBoxService.setObjectName("buttonBoxService")
		self.verticalLayout_3.addWidget(self.buttonBoxService)
		self.verticalLayout.addWidget(self.groupBoxService)

		self.retranslateUi(DeviceSelectorDialog)
		self.buttonBoxService.accepted.connect(DeviceSelectorDialog.accept)
		self.buttonBoxService.rejected.connect(DeviceSelectorDialog.reject)
		QtCore.QMetaObject.connectSlotsByName(DeviceSelectorDialog)

	def retranslateUi(self, DeviceSelectorDialog):
		_translate = QtCore.QCoreApplication.translate
		DeviceSelectorDialog.setWindowTitle(_translate("DeviceSelectorDialog", "Dialog"))
		self.pushButtonScan.setText(_translate("DeviceSelectorDialog", "Scan"))
		self.groupBoxDevices.setTitle(_translate("DeviceSelectorDialog", "Device"))
		self.labelScanningDevices.setText(_translate("DeviceSelectorDialog", "Scanning for devices..."))
		self.groupBoxService.setTitle(_translate("DeviceSelectorDialog", "Service"))
		self.labelScanningServices.setText(_translate("DeviceSelectorDialog", "Scanning for services..."))
		self.lineEditPort.setPlaceholderText(_translate("DeviceSelectorDialog", "Enter port number"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	DeviceSelectorDialog = QtWidgets.QDialog()
	ui = Ui_DeviceSelectorDialog()
	ui.setupUi(DeviceSelectorDialog)
	DeviceSelectorDialog.show()
	sys.exit(app.exec_())

