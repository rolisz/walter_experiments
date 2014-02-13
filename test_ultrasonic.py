from Arduino import Arduino
from time import sleep

#trigPin = 2
echoPin = 4

board = Arduino('9600', port = "COM9") #plugged in via USB, serial com at rate 9600

def readDistance():
	duration = board.pulseIn_set(echoPin, "HIGH")

	#Calculate the distance (in cm) based on the speed of sound.
	distance = duration/58.2;
	print distance

	#sleep(0.05)

while True:
	readDistance()