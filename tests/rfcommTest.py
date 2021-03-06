import bluetooth
import curses

port = 3

def main():
	robot = connect()
	if robot is None:
		input("Press any key to close...")
		return

	stdscr = setupCurses()
	try:
		mainLoop(robot, stdscr)
	except Exception as e:
		curses.endwin()
		print("An error occured in main loop: " + str(e))
	curses.endwin()
	robot.close()

def connect():
	print("Scanning for devices (3s)...")
	devices = []
	try:
		devices = bluetooth.discover_devices(duration = 3, lookup_names = True)
	except Exception as e:
		print("Error: %s\n" % str(e))
		return None

	devicesLength = len(devices)

	print("Found %d devices!" % devicesLength)
	if len(devices) is 0:
		return None
	i = 0
	for addr, name in devices:
		print("%d: %s [%s]" % (i, name, addr))
		i+=1

	key = input("Enter index of device to connect to: ")
	try:
		key = int(key)
	except Exception as e:
		print("Bad input!")
		return None
	if (key < 0) or (key > devicesLength):
		print("Bad input!")
		return None

	(deviceAddr, deviceName) = devices[key]
	print("Searching for services on device: %s [%s]" % (deviceName, deviceAddr))
	services = bluetooth.find_service(address = deviceAddr)

	port = None
	if len(services) is 0:
		key = input("No services found, input port number: ")
		try:
			port = int(key)
		except Exception as e:
			print("Bad input!")
			return None
	else:
		for i in range(len(services)):
			print("%d: %s - Port: %s" % (i, services[i]["name"], services[i]["port"]))
		key = input("Enter index of service to conect to: ")
		try:
			key = int(key)
		except Exception as e:
			print("Bad input!")
			return None
		port = services[key]["port"]

	print("Connecting...")
	robot = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	robot.connect((deviceAddr, port))
	return robot

def setupCurses():
	stdscr = curses.initscr()
	curses.cbreak()
	curses.noecho()
	stdscr.keypad(1)
	stdscr.nodelay(True)
	return stdscr

def mainLoop(robot, stdscr):
	keyUp = keyDown = keyLeft = keyRight = False
	state = 's'
	while True:
		curses.napms(150)
		curses.flushinp()
		curses.napms(50)
		key = stdscr.getch()
		if key is ord('q'):
			break
		elif key is -1:
			if state is 's':
				continue
			state = 's'
			stdscr.addstr(0, 0, "ROBOT STOP     ")
			robot.send('L' + chr(128) + chr(0) + chr(0))
			robot.send('R' + chr(128) + chr(0) + chr(0))
		elif key is ord('w'):
			if state is 'f':
				continue
			state = 'f'
			stdscr.addstr(0, 0, "ROBOT FORWARD  ")
			robot.send('L' + chr(159) + chr(0) + chr(0))
			robot.send('R' + chr(159) + chr(0) + chr(0))
		elif key is ord('s'):
			if state is 'b':
				continue
			state = 'b'
			stdscr.addstr(0, 0, "ROBOT BACKWARD ")
			robot.send('L' + chr(97) + chr(0) + chr(0))
			robot.send('R' + chr(97) + chr(0) + chr(0))
		elif key is ord('a'):
			if state is 'l':
				continue
			state = 'l'
			stdscr.addstr(0, 0, "ROBOT LEFT     ")
			robot.send('L' + chr(97) + chr(0) + chr(0))
			robot.send('R' + chr(159) + chr(0) + chr(0))
		elif key is ord('d'):
			if state is 'r':
				continue
			state = 'r'
			stdscr.addstr(0, 0, "ROBOT RIGHT    ")
			robot.send('L' + chr(159) + chr(0) + chr(0))
			robot.send('R' + chr(97) + chr(0) + chr(0))

if __name__ == '__main__':
	main()
