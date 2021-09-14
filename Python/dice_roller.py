#Automatic Dice Roller
#Written by Max Sweet
import time
from random import randint
print ("Automatic Dice Roller")
x=0
roll_again = "i"
while roll_again != "x":
	x = randint(0,6)
	print (x)
	roll_again = input("Roll the dice again?")
else:
	print("Goodbye!")

