import bluetooth
import serial
import serial.tools.list_ports
import sdl2
import sdl2.ext
from ctypes import byref as getCPointer

import threading
import time
import sys

exitFlag = False

def main():
	window, joystick = initSDL()
	if window is None:
		print("Error initializing SDL window.")
		return
	if joystick is None:
		print("Error initializing Joystick.")
		quitSDL(window, joystick)
		return

	connectionType = "rfcomm"
	#connectionType = None
	connection = None
	try:
		connection = initConnection(connectionType)
	except Exception as e:
		print("Error initializing connection: " + str(e))
		quitSDL(window, joystick)
		return

	window.show()
	try:
		mainLoopThread = MainLoopThread(window, joystick, connection)
		keepAliveThread = KeepAliveThread(connection, 2)
		mainLoopThread.start()
		keepAliveThread.start()
		mainLoopThread.join()
		keepAliveThread.join()
	except Exception as e:
		print("An error occured in main loop: " + str(e))
	quitConnection(connection, connectionType)
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

def quitSDL(window, joystick):
	sdl2.ext.quit()

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

def initConnection(connectionType):
	if connectionType is "rfcomm":
		connection = initRFCOMM()
		if connection is None:
			raise Exception("error initializing rfcomm")
	elif connectionType is "serial":
		connection = initSerial()
		if connection is None:
			raise Exception("error initializing serial")
	else:
		return None

def quitConnection(connection, connectionType):
	if connection is not None:
		if connectionType == "rfcomm":
			quitRFCOMM(connection)
		elif connectionType == "serial":
			quitSerial(connection)

def sendCommand(connection, command):
	print("command: " + str(command))
	if connection is not None and command is not None:
		connection.send(command)

class MainLoopThread(threading.Thread):
	window = None
	joystick = None
	connection = None
	def __init__(self, window, joystick, connection):
		threading.Thread.__init__(self)
		self.window = window
		self.joystick = joystick
		self.connection = connection

	def run(self):
		global exitFlag
		joystickDisconnected = False
		joystickID = sdl2.joystick.SDL_JoystickInstanceID(self.joystick)
		turnSpd = mainSpd = 0
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
				joystickDisconnected = True
				print("Joystick disconnected!")
				continue
			elif event.type == sdl2.SDL_JOYDEVICEADDED:
				if joystickDisconnected is False:
					newJoy = sdl2.joystick.SDL_JoystickOpen(event.jdevice.which)
					newJoyID = sdl2.joystick.SDL_JoystickInstanceID(newJoy)
					if newJoyID == joystickID:
						continue
				print("Joystick connected: " + str(sdl2.joystick.SDL_JoystickNameForIndex(event.jdevice.which), "utf-8"))
				answer = input("Switch to connected joystick (y/n)?")
				if answer.lower() is 'y':
					self.joystick = sdl2.joystick.SDL_JoystickOpen(event.jdevice.which)
					joystickID = sdl2.joystick.SDL_JoystickInstanceID(self.joystick)
					joystickDisconnected = False
				else:
					continue
			elif event.type ==  sdl2.SDL_JOYAXISMOTION and event.jaxis.which == joystickID:
				if event.jaxis.axis is not 0 and event.jaxis.axis is not 2:
					continue
				# Restrict to -256:256
				value = int(event.jaxis.value) // 128
				#print("axis %d : val %d res %d" % (event.jaxis.axis, event.jaxis.value, value))

				# Controller mapping happens here
				# TODO: make it configurable
				if event.jaxis.axis == 0:
					turnSpd = value // 2
				elif event.jaxis.axis == 2:
					mainSpd = value

				signLeft = 0
				valLeft = turnSpd + mainSpd
				if valLeft < 0:
					signLeft = 1
				valLeft = abs(valLeft)
				if valLeft >= 256:
					valLeft = 255
				signRight = 0
				valRight = mainSpd - turnSpd
				if valRight < 0:
					signRight = 1
				valRight = abs(valRight)
				if valRight >= 256:
					valRight = 255
				#print("\tturn %d main %d left %d %d right %d %d" % (turnSpd, mainSpd, signLeft, valLeft, signRight, valRight))
				command = bytes((0x10, 0x00, signLeft, valLeft, 0x10, 0x01, signRight, valRight))
			elif event.type==sdl2.SDL_JOYBUTTONDOWN and event.jbutton.which == joystickID:
				#print("button down %d" % event.jbutton.button)
				command = bytes((0x12, event.jbutton.button, 1, 0))
			elif event.type==sdl2.SDL_JOYBUTTONUP and event.jbutton.which == joystickID:
				#print("button up   %d" % event.jbutton.button)
				command = bytes((0x12, event.jbutton.button, 0, 0))
			#elif event.type==sdl2.SDL_JOYHATMOTION and event.jhat.which == joystickID:
				#hat = event.jhat.hat
				#value = event.jhat.value
			else:
				continue

			sendCommand(self.connection, command)
		exitFlag = True
		print("ending mainLoopThread, exitFlag: " + str(exitFlag))

class KeepAliveThread(threading.Thread):
	connection = None
	interval = 3
	def __init__(self, connection, interval = 3):
		threading.Thread.__init__(self)
		self.connection = connection
		self.interval = interval

	def run(self):
		global exitFlag
		counter = 0
		time.sleep(self.interval)
		while exitFlag == False:
			try:
				keepalive = bytes((0x04, counter % 256, 0x00, 0x00))
				sendCommand(self.connection, keepalive)
			except Exception as e:
				print("keepAlive sending error: " + str(e))
				quitEvent = sdl2.SDL_Event()
				quitEvent.type = sdl2.SQL_QUIT
				sdl2.SDL_PushEvent(quitEvent)
				break
			time.sleep(self.interval)

if __name__ == '__main__':
	main()
