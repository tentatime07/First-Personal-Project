from operations import *

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

def getname():
    return input("What's your name?: ")

def getoperation(prompt):
    while True:
        operation = input(prompt)
        if operation in operations:
            return [operations[operation], operation]
        else:
            print("not a valid operation, try again")
            
def getnumber(prompt):
    while True:
        try: 
            number = float(input(prompt))
            return number
        except ValueError:
            print("not a valid number, try again")

def getnumberdiv(prompt):
    while True:
        try: 
            number = float(input(prompt))
            if number == 0:
                print("cannot divide by zero, try again")
            else:
                return number
        except ValueError:
            print("not a valid number, try again")
        
def getrestart(prompt):
    while True:
        res = input(prompt).strip().lower()
        if res == "y":
            return True
        elif res == "n":
            return False
    
    
def start():
    first = True
    print("Welcome to Tommy's calculator.")
    name = getname()
    while True:
        if first:
            operation = getoperation("Hi " + name + ". To start, choose an operator. Type +, -, *, or /: ")
        else:
            operation = getoperation("Sure " + name + ". To start, choose an operator. Type +, -, *, or /: ")
        number1 = getnumber("Now, choose your first number: ")
        if operation[1] == "/":
            number2 = getnumberdiv("Now, choose your second number: ")
        else:
            number2 = getnumber("Now, choose your second number: ")
        print(str(number1) + " " + operation[1] + " " + str(number2) + " = " + str(operation[0](number1, number2)))
        res = getrestart("Would you like to do another calculation? y or n: ")
        first = False
        if not res:
            print("Goodbye! See you " + name + ".")
            break

start()



















