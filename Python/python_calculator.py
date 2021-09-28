
# Calculator Python Script
# By Max Sweet
import math
print("Calculator")
a = "bruh" #resets vars
b = "bruh"
while True: #reset loop
    while a == "bruh": #while the var is 
        a = int(input("First variable?:")) #prompts for variation of a
    while b == "bruh":
        b = int(input("Second variable?:")) #rompts for variation of b
    def doMath (a, b, i): #defines function
        if i == 1:
            return str(a+b) #returns as string of a + b
        if i == 2:
            return str(a-b)
        if i == 3:
            return str(a*b)
        if i == 4:
            return str(a/b)
        if i == 5:
            return str(a%b)
        if i == 6:
            return str(math.factorial(a))
        if i == 7:
            return str(math.factorial(b))
    print("Sum:\t\t" + doMath(a,b,1))
    print("Difference:\t" + doMath(a,b,2))
    print("Product:\t" + doMath(a,b,3))
    print("Quotient:\t" + doMath(a,b,4))
    print("Modulo:\t\t" + doMath(a,b,5))
    print("Fact 1:\t\t" + doMath(a,b,6))
    print("Fact 2:\t\t" + doMath(a,b,7))
    if input("Respond x to break script") == "x": #if the responce the the prompt is "x" break the script
        break
    a = "bruh" #resets vars
    b = "bruh"
