import bluetooth
import curses

port = 3

def main():
	stdscr = curses.initscr()
	curses.cbreak()
	stdscr.keypad(1)
	stdscr.addstr("curses test!\n")
	stdscr.refresh()

	deviceAddr = getDevices(stdscr)
	if deviceAddr is None:
		curses.endwin()
		return

	mainLoop(stdscr, deviceAddr)

	curses.endwin()
	return

def getDevices(stdscr):
	stdscr.addstr("scanning for devices (5s)...\n")
	stdscr.refresh()
	devices = []
	try:
		devices = bluetooth.discover_devices(duration = 5, lookup_names = True)
	except Exception as e:
		stdscr.addstr("Error: " + str(e) + "\n")

	stdscr.addstr("Found %d devices!\n" % len(devices))
	i = 1
	for addr, name in devices:
		stdscr.addstr("%d: %s [ %s ]\n" % (i, name, addr))
	stdscr.refresh()

	key = stdscr.getch()
	if (key < ord('1')) or (key > ord(str(len(devices)))):
		stdscr.addstr("No such device!\n")
		stdscr.refresh()
		return None

	(deviceAddr, name) = devices[int(curses.keyname(key))]
	return deviceAddr

def mainLoop(stdscr, deviceAddr):
	#stdscr.addstr("Enter port number: ")
	#stdscr.refresh()
	#port = int(stdscr.getch() - 48)
	
	stdscr.addstr("Searching for services on device: %s\n" % deviceAddr)
	stdscr.refresh()

	services = bluetooth.find_service(address = deviceAddr)

	if len(services) is 0:
		stdscr.addstr("No services found!")
		stdscr.refresh()
		return

	port = services[0]["port"]

	stdscr.addstr("Connecting to device: %s\n" % deviceAddr)
	stdscr.refresh()

	robot = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	robot.connect((deviceAddr, port))

	nodelay(True)
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
