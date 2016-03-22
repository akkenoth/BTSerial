import bluetooth
import curses

port = 3

def main():

	(deviceAddr, deviceName) = getDevices()
	if deviceAddr is None:
		input("Press any key to close...")
		return

	mainLoop(deviceAddr, deviceName)

	return

def getDevices():
	print("Scanning for devices (3s)...")
	devices = []
	try:
		devices = bluetooth.discover_devices(duration = 3, lookup_names = True)
	except Exception as e:
		print("Error: %s\n" % str(e))
		return (None, None)

	devicesLength = len(devices)

	print("Found %d devices!" % devicesLength)
	if len(devices) is 0:
		return (None, None)
	i = 0
	for addr, name in devices:
		print("%d: %s [%s]" % (i, name, addr))
		i+=1

	key = input("Enter index of device to connect to: ")
	try:
		key = int(key)
	except Exception as e:
		print("Bad input!")
		return (None, None)
	if (key < 0) or (key > devicesLength):
		print("Bad input!")
		return (None, None)

	return devices[key]
def mainLoop(deviceAddr, deviceName):
	print("Searching for services on device: %s [%s]" % (deviceName, deviceAddr))

	services = bluetooth.find_service(address = deviceAddr)

	port = None
	if len(services) is 0:
		key = input("No services found, input port number: ")
		try:
			port = int(key)
		except Exception as e:
			print("Bad input!")
			return
	else:
		for i in range(len(services)):
			print("%d: %s - Port: %s" % (i, services[i]["name"], services[i]["port"]))
		key = input("Enter index of service to conect to: ")
		try:
			key = int(key)
		except Exception as e:
			print("Bad input!")
			return
		port = services[key]["port"]

	print("Connecting...")
	robot = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	robot.connect((deviceAddr, port))

	stdscr = curses.initscr()
	curses.cbreak()
	stdscr.keypad(1)
	stdscr.nodelay(True)

	keyUp = keyDown = keyLeft = keyRight = False
	while True:
		key = stdscr.getch()
		if key is ord('q'):
			break
		elif key is -1:
			robot.send(chr('L') + chr(0) + chr(0) + chr(0))
			robot.send(chr('R') + chr(0) + chr(0) + chr(0))
		elif key is ord('w'):
			robot.send(chr('L') + chr(191) + chr(0) + chr(0))
			robot.send(chr('R') + chr(191) + chr(0) + chr(0))
		elif key is ord('s'):
			robot.send(chr('L') + chr(64) + chr(0) + chr(0))
			robot.send(chr('R') + chr(64) + chr(0) + chr(0))
		elif key is ord('a'):
			robot.send(chr('L') + chr(64) + chr(0) + chr(0))
			robot.send(chr('R') + chr(191) + chr(0) + chr(0))
		elif key is ord('d'):
			robot.send(chr('L') + chr(191) + chr(0) + chr(0))
			robot.send(chr('R') + chr(64) + chr(0) + chr(0))
	robot.close()


if __name__ == '__main__':
	main()
