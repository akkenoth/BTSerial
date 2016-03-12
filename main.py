import sys
from PyQt5.QtWidgets import QApplication
from BTSerial import BTSerial

def main():
	app = QApplication(sys.argv)
	program = BTSerial()
	program.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
