import bluetooth
import pygame
import time
import pprint

port = 1

def main():
	robot = connect()
	if robot is None:
		input("Press any key to close...")
		return

	try:
		mainLoop(robot)
	except Exception as e:
		print("An error occured in main loop: " + str(e))
	pygame.quit()
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

def mainLoop(robot):
	pygame.init()
	window = pygame.display.set_mode((800, 600), 0, 32)
	window.fill((0, 0, 0))

	lSpd = rSpd = 128
	while True:
		event = pygame.event.wait()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				return
			elif event.key == pygame.K_UP:
				lSpd += 20
				rSpd += 20
			elif event.key == pygame.K_DOWN:
				lSpd -= 20
				rSpd -= 20
			elif event.key == pygame.K_LEFT:
				lSpd -= 20
				rSpd += 20
			elif event.key == pygame.K_RIGHT:
				lSpd += 20
				rSpd -= 20
			else:
				continue
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				lSpd -= 20
				rSpd -= 20
			elif event.key == pygame.K_DOWN:
				lSpd += 20
				rSpd += 20
			elif event.key == pygame.K_LEFT:
				lSpd += 20
				rSpd -= 20
			elif event.key == pygame.K_RIGHT:
				lSpd -= 20
				rSpd += 20
			else:
				continue
		else:
			continue

		lCommand = 'L' + chr(lSpd) + chr(0) + chr(0)
		rCommand = 'R' + chr(rSpd) + chr(0) + chr(0)

		print(lCommand.encode('latin1'))
		print(rCommand.encode('latin1'))
		robot.send(lCommand.encode('latin1'))
		robot.send(rCommand.encode('latin1'))

if __name__ == '__main__':
	main()
