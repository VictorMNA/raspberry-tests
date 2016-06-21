# Victor Navarro (victormna.developer@gmail.com)
# 
# very simple "game" to test basic hardware connection
# i.e. a couple of LEDs an switchs
#
# Green LED means Live
# Red LED means Die
#
# Switch 1 reset/start de game
# Switch 2 stop counter
#
# using RPi.GPIO needs to run as root (use sudo)

# libraries used
import RPi.GPIO as GPIO
from time import sleep

print("Starting...")

# select here your real ports used
# from the board pinout perspective
RedLed = 16
GreenLed = 18
Switch1 = 40
Switch2 = 38


#configure the system
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedLed, GPIO.OUT)
GPIO.setup(GreenLed, GPIO.OUT)
GPIO.setup(Switch1, GPIO.IN)
GPIO.setup(Switch2, GPIO.IN)


# setup variables 
BlinkFrequency = 10


# main loop handling the keyboard interrupt
try:

	print("Ready to play")
	print("Ctrl+C to quit")
	HalfPeriod = (1.0 / BlinkFrequency) / 2.0

	while True:
		# wait until Switch1 is pressed
		while True:
			GPIO.output(RedLed, True)
			GPIO.output(GreenLed, True)
			print("Tick")
			sleep(0.5)
			if GPIO.input(Switch1) == 0:
				break
			GPIO.output(RedLed, False)
			GPIO.output(GreenLed, False)
			print("Tack")
			sleep(0.5)
			if GPIO.input(Switch1) == 0:
				break;

		# start the game and wait until Switch2 is pressed for the result
		print("Press Switch2 to know your fate...")
		while True:
			GPIO.output(RedLed, True)
			GPIO.output(GreenLed, False)
			Alive = False
			sleep(HalfPeriod)
			if GPIO.input(Switch2) == 0:
				break
			GPIO.output(RedLed, False)
			GPIO.output(GreenLed, True)
			sleep(HalfPeriod) 
			Alive = True
			if GPIO.input(Switch2) == 0:
				break

		# print the result
		print("")
		if Alive == True:
			print("You live")
		else:
			print("You die")

		# keep result until a new game
		print("")
		print("Press Switch1 to a new game")
		while GPIO.input(Switch1) == 1:
			sleep(0.1)
		while GPIO.input(Switch1) == 0:
			sleep(0.1)		
		
# Ctrl+C stops the program
except KeyboardInterrupt:
	print("")
	print("Exiting game...")

finally:
	# finished
	GPIO.cleanup()
	print("end")
	print("")
