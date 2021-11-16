# Python Program - Double LED blink
#Written by Max Sweet
#11.16.21

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #this sets the pin numbering scheme as the BCM numbering scheme
#Variables for GPIO pin numbers:
LED1 = 21
LED2 = 26
#Tell the pi we are using BCM:
GPIO.setmode(GPIO.BCM)
#Set the GPIO pins as outputs:
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
#Loop to blink the leds
while True:
	GPIO.output(LED1, GPIO.HIGH)
	print("led 1 on")
	time.sleep(1)
	GPIO.output(LED1, GPIO.LOW)
	GPIO.output(LED2, GPIO.HIGH)
	print("led 2 on")
	time.sleep(1)
	GPIO.output(LED2, GPIO.LOW)

