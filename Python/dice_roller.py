#Automatic Dice Roller
#Written by Max Sweet
import time
from random import randint
print ("Automatic Dice Roller")
x=0
amount = 0
sides = 0
roll_again = "i"
while True:
	while sides == 0: #while the sides variable is unchanged:
		sides = int(input("How many sides would you like the dice to have?")) #sides var = input to the question in integer

	while amount == 0:
		amount = int(input("How many dice would you like to roll?"))

	while roll_again != "x": #when the response to the input of roll again doesnrt equal x
		print("Roll(s)")
		for i in range(0,amount): #repeat as many times as the amount
			x=randint(1, sides) #create a random number between 1 and the sides val
			print (x) #print the number
			i += 1 #add 1 to the amount in the loop
		if input("Change settings?? y for yes") == "y": #if the input for the prompt is y:
			amount = 0 #reset settings
			sides = 0
		while sides == 0: #same thing as before
			sides = int(input("Sides?"))
		while amount == 0:
			amount = int(input("Amount?"))
		roll_again = input("Roll the dice again?") #ask if you want to roll again
	else: #if the responce was "x"
		print("Goodbye!") #quit script
		break
