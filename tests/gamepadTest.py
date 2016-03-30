import bluetooth
import serial
import serial.tools.list_ports
import sdl2
import sdl2.ext
from ctypes import byref as getCPointer

import sys

def main():
	window, joystick = initSDL()
	if window is None:
		print("Error initializing SDL window.")
		return
	if joystick is None:
		print("Error initializing Joystick.")
		sdlQuit(window, joystick)
		return

	#connection = None
	connection = initRFCOMM()
	#connection = initSerial()
	if connection is None:
		print("Error initializing connection.")
		quitSDL(window, joystick)
		return

	window.show()
	try:
		mainLoop(window, joystick, connection)
	except Exception as e:
		print("An error occured in main loop: " + str(e))
	#quitSerial(connection)
	quitRFCOMM(connection)
	quitSDL(window, joystick)

def initSDL():
	if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_JOYSTICK) != 0:
		print(str(sdl2.SDL_GetError()))
		return None, None

	window = sdl2.ext.Window("Gamepad/Joystick test", size=(600, 600))

	numJoys = sdl2.joystick.SDL_NumJoysticks()
	index = -1
	if numJoys == 0:
		print("No controllers found.")
		return window, None
	elif numJoys == 1:
		print("Using the only joystick found: " + str(sdl2.joystick.SDL_JoystickNameForIndex(0), "utf-8"))
		index = 0
	else:
		for i in range(numJoys):
			joyName = sdl2.joystick.SDL_JoystickNameForIndex(i)
			print("%d: %s" % (i, str(joyName, "utf-8")))
		index = input("Enter target controller index: ")
		try:
			index = int(index)
			if index < 0 or index > numJoys:
				raise IndexError("No such controller!")
		except Exception as e:
			print("An error occured: " + str(e))
			return window, None

	joy = sdl2.joystick.SDL_JoystickOpen(index)

	return window, joy

def initSerial():
	ports = list(serial.tools.list_ports.comports())
	index = -1
	if len(ports) == 0:
		print("No serial ports found.")
		return None
	elif len(ports) == 1:
		print("Using the only serial port found: " + ports[0].description)
		index = 0
	else:
		for i in range(len(ports)):
			print("%d: %s" % (i, ports[i].description))
		index = input("Enter target serial port index: ")
		try:
			index = int(index)
			if index < 0 or index >= i:
				raise IndexError("No such port!")
		except Exception as e:
			print("An error occured: " + str(e))
			return None

	baudrate = 9600
	#baudrate = 112500
	#input("Enter target baudrate: ")

	try:
		connection = serial.Serial(port = ports[index].device, baudrate = baudrate)
		connection.open()
		if connection.is_open is False:
			raise Exception("Couldn't open connection!")
		return connection
	except Exception as e:
		print("An error occured: " + str(e))
		return None

def quitSerial(connection):
	if connection is not None:
		connection.close()

def initRFCOMM():
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

def quitRFCOMM(connection):
	if connection is not None:
		connection.close()

def quitSDL(window, joystick):
	sdl2.ext.quit()

def sendCommand(connection, command):
	print("command: " + str(command))
	if connection is not None and command is not None:
		connection.send(command)

def mainLoop(window, joystick, connection):
	joystickID = sdl2.joystick.SDL_JoystickInstanceID(joystick)
	lSpd = rSpd = mainSpd = 0
	event = sdl2.SDL_Event()
	while True:
		waitEventError = sdl2.SDL_WaitEvent(getCPointer(event))
		if waitEventError == 0:
			print("error waiting for event: " + str(sdl2.SDL_GetError()))
			continue

		command = None

		if event.type == sdl2.SDL_QUIT:
			print("QUIT!")
			break
		elif event.type == sdl2.SDL_KEYUP and event.key.keysym.sym == sdl2.SDLK_q:
			print("Exiting on user input.")
			break
		elif event.type == sdl2.SDL_JOYDEVICEREMOVED and event.jdevice.which == joystickID:
			print("Joystick disconnected!")
		elif event.type == sdl2.SDL_JOYDEVICEADDED:
			print("Joystick connected: " + str(sdl2.joystick.SDL_JoystickNameForIndex(event.jdevice.which), "utf-8"))
			answer = input("Switch to connected joystick (y/n)?")
			if answer.lower() is 'y':
				joystick = sdl2.joystick.SDL_JoystickOpen(event.jdevice.which)
				joystickID = sdl2.joystick.SDL_JoystickInstanceID(joystick)
		elif event.type==sdl2.SDL_JOYAXISMOTION and event.jaxis.which == joystickID:
			# Restrict to -128:128
			value = int(event.jaxis.value) // 256
			# Additionally, restrict to -64:64
			value = value // 3
			if event.jaxis.axis == 0:
				value = value // 2
				lSpd = value
				rSpd = -value
				#command = bytes((b'L', lSpd + mainSpd, 0, 0, b'R', rSpd + mainSpd, 0, 0))
				command = bytes((76, 128 + lSpd + mainSpd, 0, 0, 82, 128 + rSpd + mainSpd, 0, 0))
			elif event.jaxis.axis == 2:
				mainSpd = -value
				command = bytes((76, 128 + lSpd + mainSpd, 0, 0, 82, 128 + rSpd + mainSpd, 0, 0))
		#elif event.type==sdl2.SDL_JOYHATMOTION and event.jhat.which == joystickID:
			#hat = event.jhat.hat
			#value = event.jhat.value
		elif event.type==sdl2.SDL_JOYBUTTONDOWN and event.jbutton.which == joystickID:
			command = bytes((0x40 + event.jbutton.button, 1, 0, 0))
		elif event.type==sdl2.SDL_JOYBUTTONUP and event.jbutton.which == joystickID:
			command = bytes((0x40 + event.jbutton.button, 0, 0, 0))
		else:
			continue

		sendCommand(connection, command)

if __name__ == '__main__':
	main()
