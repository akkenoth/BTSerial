import serial
import serial.tools.list_ports
import sdl2
import sdl2.ext
from ctypes import byref as getCPointer

import sys

def main():
	window, joystick = sdlInit()
	if window is None:
		print("Error initializing SDL window.")
		return
	if joystick is None:
		print("Error initializing Joystick.")
		sdlQuit(window, joystick)
		return
	
	connection = initSerial()
	if connection is None:
		print("Error initializing serial connection.")
		sdlQuit(window, joystick)
		return		

	window.show()
	try:
		mainLoop(window, joystick, connection)
	except Exception as e:
		print("An error occured in main loop: " + str(e))
	serialQuit(connection)
	sdlQuit(window, joystick)

def sdlInit():
	if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO | sdl2.SDL_INIT_JOYSTICK) != 0:
		print(str(sdl2.SDL_GetError()))
		return None, None
	
	window = sdl2.ext.Window("Gamepad/Joystick test", size=(300, 200))

	numJoys = sdl2.joystick.SDL_NumJoysticks()
	index = -1
	if numJoys == 0:
		print("No controllers found.")
		return window, None
	elif numJoys == 1:
		print("Using the only joystick found: " + str(sdl2.joystick.SDL_JoystickNameForIndex(0)))
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

def serialQuit(connection):
	connection.close()

def sdlQuit(window, joystick):
	sdl2.ext.quit()

def mainLoop(window, joystick, connection):
	joystickID = sdl2.joystick.SDL_JoystickInstanceID(joystick)
	lSpd = rSpd = 128
	event = sdl2.SDL_Event()
	while True:
		waitEventError = sdl2.SDL_WaitEvent(getCPointer(event))
		if waitEventError == 0:
			print("error waiting for event: " + str(sdl2.SDL_GetError()))
			continue

		if event.type == sdl2.SDL_QUIT:
			print("QUIT!")
			break
		elif event.type == sdl2.SDL_KEYUP and event.key.keysym.sym == sdl2.SDLK_q:
			print("Exiting on user input!")
			break
		elif event.type == sdl2.SDL_JOYDEVICEREMOVED and event.jdevice.which == joystickID:
			print("Joystick removed!")
			break
		elif event.type==sdl2.SDL_JOYAXISMOTION and event.jaxis.which == joystickID:
			print("AXIS MOTION: axis: %s, value: %s" % (str(event.jaxis.axis), str(event.jaxis.value)))
		elif event.type==sdl2.SDL_JOYHATMOTION and event.jhat.which == joystickID:
			print("HAT MOTION: hat: %s, value: %s" % (str(event.jhat.hat), str(event.jhat.value)))
		elif event.type==sdl2.SDL_JOYBUTTONDOWN and event.jbutton.which == joystickID:
			print("BUTTON DOWN: button: %s" % str(event.jbutton.button))
		elif event.type==sdl2.SDL_JOYBUTTONUP and event.jbutton.which == joystickID:
			print("BUTTON UP: button: %s" % str(event.jbutton.button))
		else:
			continue
		sys.stdout.flush()

		#bytearray()

if __name__ == '__main__':
	main()
