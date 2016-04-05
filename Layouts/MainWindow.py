# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BTSerialMainWindow(object):
	def setupUi(self, BTSerialMainWindow):
		BTSerialMainWindow.setObjectName("BTSerialMainWindow")
		BTSerialMainWindow.resize(891, 388)
		self.centralwidget = QtWidgets.QWidget(BTSerialMainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.verticalLayoutCommands = QtWidgets.QVBoxLayout()
		self.verticalLayoutCommands.setObjectName("verticalLayoutCommands")
		self.labelCommandList = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("Cambria")
		font.setPointSize(12)
		self.labelCommandList.setFont(font)
		self.labelCommandList.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.labelCommandList.setAlignment(QtCore.Qt.AlignCenter)
		self.labelCommandList.setObjectName("labelCommandList")
		self.verticalLayoutCommands.addWidget(self.labelCommandList)
		self.listWidgetCommands = QtWidgets.QListWidget(self.centralwidget)
		self.listWidgetCommands.setObjectName("listWidgetCommands")
		self.verticalLayoutCommands.addWidget(self.listWidgetCommands)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pushButtonAddCommandType = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonAddCommandType.setObjectName("pushButtonAddCommandType")
		self.horizontalLayout_2.addWidget(self.pushButtonAddCommandType)
		self.pushButtonEditCommandType = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonEditCommandType.setObjectName("pushButtonEditCommandType")
		self.horizontalLayout_2.addWidget(self.pushButtonEditCommandType)
		self.pushButtonDeleteCommandType = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonDeleteCommandType.setObjectName("pushButtonDeleteCommandType")
		self.horizontalLayout_2.addWidget(self.pushButtonDeleteCommandType)
		self.verticalLayoutCommands.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.pushButtonAddDelay = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonAddDelay.setObjectName("pushButtonAddDelay")
		self.horizontalLayout_5.addWidget(self.pushButtonAddDelay)
		self.pushButtonAddToQueue = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonAddToQueue.setObjectName("pushButtonAddToQueue")
		self.horizontalLayout_5.addWidget(self.pushButtonAddToQueue)
		self.verticalLayoutCommands.addLayout(self.horizontalLayout_5)
		self.horizontalLayout.addLayout(self.verticalLayoutCommands)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.horizontalLayout.addWidget(self.line)
		self.verticalLayoutQueue = QtWidgets.QVBoxLayout()
		self.verticalLayoutQueue.setObjectName("verticalLayoutQueue")
		self.labelQueue = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("Cambria")
		font.setPointSize(12)
		self.labelQueue.setFont(font)
		self.labelQueue.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.labelQueue.setAlignment(QtCore.Qt.AlignCenter)
		self.labelQueue.setObjectName("labelQueue")
		self.verticalLayoutQueue.addWidget(self.labelQueue)
		self.listWidgetQueue = QtWidgets.QListWidget(self.centralwidget)
		self.listWidgetQueue.setObjectName("listWidgetQueue")
		self.verticalLayoutQueue.addWidget(self.listWidgetQueue)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.pushButtonMoveCommandItemUp = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonMoveCommandItemUp.setObjectName("pushButtonMoveCommandItemUp")
		self.horizontalLayout_3.addWidget(self.pushButtonMoveCommandItemUp)
		self.pushButtonMoveCommandItemDown = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonMoveCommandItemDown.setObjectName("pushButtonMoveCommandItemDown")
		self.horizontalLayout_3.addWidget(self.pushButtonMoveCommandItemDown)
		self.pushButtonDeleteCommandItem = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonDeleteCommandItem.setObjectName("pushButtonDeleteCommandItem")
		self.horizontalLayout_3.addWidget(self.pushButtonDeleteCommandItem)
		self.verticalLayoutQueue.addLayout(self.horizontalLayout_3)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.pushButtonExecute = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonExecute.setObjectName("pushButtonExecute")
		self.horizontalLayout_4.addWidget(self.pushButtonExecute)
		self.verticalLayoutQueue.addLayout(self.horizontalLayout_4)
		self.horizontalLayout.addLayout(self.verticalLayoutQueue)
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.horizontalLayout.addWidget(self.line_2)
		self.verticalLayoutLog = QtWidgets.QVBoxLayout()
		self.verticalLayoutLog.setObjectName("verticalLayoutLog")
		self.labelLog = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("Cambria")
		font.setPointSize(12)
		self.labelLog.setFont(font)
		self.labelLog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.labelLog.setAlignment(QtCore.Qt.AlignCenter)
		self.labelLog.setObjectName("labelLog")
		self.verticalLayoutLog.addWidget(self.labelLog)
		self.listWidgetLog = QtWidgets.QListWidget(self.centralwidget)
		self.listWidgetLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.listWidgetLog.setDragEnabled(True)
		self.listWidgetLog.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
		self.listWidgetLog.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.listWidgetLog.setSelectionRectVisible(True)
		self.listWidgetLog.setObjectName("listWidgetLog")
		item = QtWidgets.QListWidgetItem()
		item.setText("<<< Incoming message")
		font = QtGui.QFont()
		font.setFamily("Monospace")
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
		brush.setStyle(QtCore.Qt.NoBrush)
		item.setForeground(brush)
		self.listWidgetLog.addItem(item)
		item = QtWidgets.QListWidgetItem()
		item.setText("--- Informational message")
		font = QtGui.QFont()
		font.setFamily("Monospace")
		font.setItalic(False)
		item.setFont(font)
		self.listWidgetLog.addItem(item)
		item = QtWidgets.QListWidgetItem()
		item.setText(">>> Outcoming command")
		font = QtGui.QFont()
		font.setFamily("Monospace")
		font.setBold(True)
		font.setItalic(False)
		font.setWeight(75)
		item.setFont(font)
		brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
		brush.setStyle(QtCore.Qt.NoBrush)
		item.setForeground(brush)
		self.listWidgetLog.addItem(item)
		self.verticalLayoutLog.addWidget(self.listWidgetLog)
		self.horizontalLayoutLogFilters = QtWidgets.QHBoxLayout()
		self.horizontalLayoutLogFilters.setObjectName("horizontalLayoutLogFilters")
		self.checkBoxIncomingFilter = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxIncomingFilter.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.checkBoxIncomingFilter.setChecked(True)
		self.checkBoxIncomingFilter.setObjectName("checkBoxIncomingFilter")
		self.horizontalLayoutLogFilters.addWidget(self.checkBoxIncomingFilter)
		self.checkBoxOutgoingFilter = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxOutgoingFilter.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.checkBoxOutgoingFilter.setChecked(True)
		self.checkBoxOutgoingFilter.setObjectName("checkBoxOutgoingFilter")
		self.horizontalLayoutLogFilters.addWidget(self.checkBoxOutgoingFilter)
		self.checkBoxLogFilter = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBoxLogFilter.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
		self.checkBoxLogFilter.setChecked(True)
		self.checkBoxLogFilter.setObjectName("checkBoxLogFilter")
		self.horizontalLayoutLogFilters.addWidget(self.checkBoxLogFilter)
		self.verticalLayoutLog.addLayout(self.horizontalLayoutLogFilters)
		self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.pushButtonOpenGamepadControl = QtWidgets.QPushButton(self.centralwidget)
		self.pushButtonOpenGamepadControl.setObjectName("pushButtonOpenGamepadControl")
		self.horizontalLayout_6.addWidget(self.pushButtonOpenGamepadControl)
		self.verticalLayoutLog.addLayout(self.horizontalLayout_6)
		self.horizontalLayout.addLayout(self.verticalLayoutLog)
		BTSerialMainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(BTSerialMainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 19))
		self.menubar.setObjectName("menubar")
		self.menuProgram = QtWidgets.QMenu(self.menubar)
		self.menuProgram.setObjectName("menuProgram")
		self.menuCommands = QtWidgets.QMenu(self.menubar)
		self.menuCommands.setObjectName("menuCommands")
		BTSerialMainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(BTSerialMainWindow)
		self.statusbar.setObjectName("statusbar")
		BTSerialMainWindow.setStatusBar(self.statusbar)
		self.actionLoadQueue = QtWidgets.QAction(BTSerialMainWindow)
		self.actionLoadQueue.setObjectName("actionLoadQueue")
		self.actionSaveQueue = QtWidgets.QAction(BTSerialMainWindow)
		self.actionSaveQueue.setObjectName("actionSaveQueue")
		self.actionLoadTypes = QtWidgets.QAction(BTSerialMainWindow)
		self.actionLoadTypes.setObjectName("actionLoadTypes")
		self.actionConnect = QtWidgets.QAction(BTSerialMainWindow)
		self.actionConnect.setObjectName("actionConnect")
		self.actionDisconnect = QtWidgets.QAction(BTSerialMainWindow)
		self.actionDisconnect.setObjectName("actionDisconnect")
		self.actionQuit = QtWidgets.QAction(BTSerialMainWindow)
		self.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
		self.actionQuit.setObjectName("actionQuit")
		self.actionSettings = QtWidgets.QAction(BTSerialMainWindow)
		self.actionSettings.setObjectName("actionSettings")
		self.actionSaveTypes = QtWidgets.QAction(BTSerialMainWindow)
		self.actionSaveTypes.setObjectName("actionSaveTypes")
		self.menuProgram.addAction(self.actionConnect)
		self.menuProgram.addAction(self.actionDisconnect)
		self.menuProgram.addSeparator()
		self.menuProgram.addAction(self.actionSettings)
		self.menuProgram.addAction(self.actionQuit)
		self.menuCommands.addAction(self.actionLoadQueue)
		self.menuCommands.addAction(self.actionSaveQueue)
		self.menuCommands.addSeparator()
		self.menuCommands.addAction(self.actionLoadTypes)
		self.menuCommands.addAction(self.actionSaveTypes)
		self.menubar.addAction(self.menuProgram.menuAction())
		self.menubar.addAction(self.menuCommands.menuAction())

		self.retranslateUi(BTSerialMainWindow)
		QtCore.QMetaObject.connectSlotsByName(BTSerialMainWindow)

	def retranslateUi(self, BTSerialMainWindow):
		_translate = QtCore.QCoreApplication.translate
		BTSerialMainWindow.setWindowTitle(_translate("BTSerialMainWindow", "BTSerial"))
		self.labelCommandList.setText(_translate("BTSerialMainWindow", "Available commands"))
		self.listWidgetCommands.setSortingEnabled(True)
		self.pushButtonAddCommandType.setText(_translate("BTSerialMainWindow", "New..."))
		self.pushButtonEditCommandType.setText(_translate("BTSerialMainWindow", "Edit..."))
		self.pushButtonDeleteCommandType.setText(_translate("BTSerialMainWindow", "Delete"))
		self.pushButtonAddDelay.setText(_translate("BTSerialMainWindow", "Add delay"))
		self.pushButtonAddToQueue.setText(_translate("BTSerialMainWindow", "Add to queue"))
		self.labelQueue.setText(_translate("BTSerialMainWindow", "Command queue"))
		self.pushButtonMoveCommandItemUp.setText(_translate("BTSerialMainWindow", "Move up"))
		self.pushButtonMoveCommandItemDown.setText(_translate("BTSerialMainWindow", "Move down"))
		self.pushButtonDeleteCommandItem.setText(_translate("BTSerialMainWindow", "Delete"))
		self.pushButtonExecute.setText(_translate("BTSerialMainWindow", "Execute"))
		self.labelLog.setText(_translate("BTSerialMainWindow", "Log"))
		__sortingEnabled = self.listWidgetLog.isSortingEnabled()
		self.listWidgetLog.setSortingEnabled(False)
		self.listWidgetLog.setSortingEnabled(__sortingEnabled)
		self.checkBoxIncomingFilter.setText(_translate("BTSerialMainWindow", "Incoming"))
		self.checkBoxOutgoingFilter.setText(_translate("BTSerialMainWindow", "Outgoing"))
		self.checkBoxLogFilter.setText(_translate("BTSerialMainWindow", "Log"))
		self.pushButtonOpenGamepadControl.setText(_translate("BTSerialMainWindow", "Gamepad Control..."))
		self.menuProgram.setTitle(_translate("BTSerialMainWindow", "Program"))
		self.menuCommands.setTitle(_translate("BTSerialMainWindow", "Commands"))
		self.actionLoadQueue.setText(_translate("BTSerialMainWindow", "Load queue"))
		self.actionLoadQueue.setShortcut(_translate("BTSerialMainWindow", "Ctrl+L"))
		self.actionSaveQueue.setText(_translate("BTSerialMainWindow", "Save queue"))
		self.actionSaveQueue.setShortcut(_translate("BTSerialMainWindow", "Ctrl+S"))
		self.actionLoadTypes.setText(_translate("BTSerialMainWindow", "Load list"))
		self.actionLoadTypes.setShortcut(_translate("BTSerialMainWindow", "Ctrl+Shift+L"))
		self.actionConnect.setText(_translate("BTSerialMainWindow", "Connect..."))
		self.actionDisconnect.setText(_translate("BTSerialMainWindow", "Disconnect"))
		self.actionQuit.setText(_translate("BTSerialMainWindow", "Quit"))
		self.actionQuit.setShortcut(_translate("BTSerialMainWindow", "Ctrl+Q"))
		self.actionSettings.setText(_translate("BTSerialMainWindow", "Settings"))
		self.actionSaveTypes.setText(_translate("BTSerialMainWindow", "Save list"))
		self.actionSaveTypes.setShortcut(_translate("BTSerialMainWindow", "Ctrl+Shift+S"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	BTSerialMainWindow = QtWidgets.QMainWindow()
	ui = Ui_BTSerialMainWindow()
	ui.setupUi(BTSerialMainWindow)
	BTSerialMainWindow.show()
	sys.exit(app.exec_())

