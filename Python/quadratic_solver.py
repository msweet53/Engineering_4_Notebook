#Quadratic Solver
#Scripted by Max Sweet
#9.21.21
import math
print ("Quadratic Solving Script")
a = "bruh" #sets coefficient vars to a string (string isnt relevantw)
b = "bruh"
c = "bruh"

def quadratic_solver(a, b, c): #definies the function
    if b ** 2 - 4*a*c < 0: #discriminant check for no real roots
        return str("No real roots found.") #returns as no real roots
    if b ** 2 - 4*a*c >= 0: #discrimminant check for real roots
        roots = [(-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 *a), (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 *a)] #quadratic formula (i hate parentheses)
        return roots #returns array of roots

while True:   
    while a == "bruh": #checks to see if ther variables need to be set with irrelevant string
        a = int(input("a value?"))
    while b == "bruh":
        b = int(input("b value?"))
    while c == "bruh":
        c = int(input("c value?"))
    while input("solve? return x to cancel") != "x": #if the answer to the prompt isnt "x"
        print(quadratic_solver(a, b, c)) #run the function and print the return
        a = "bruh" #reset vars to irrelevant string
        b = "bruh"
        c = "bruh"
        while a == "bruh": #same as above
            a = int(input("a value?"))
        while b == "bruh":
            b = int(input("b value?"))
        while c == "bruh":
            c = int(input("c value?"))
    else: #if the response was "x"
        break #breaks the script
