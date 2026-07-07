def add(x, y):
    return x + y

def choosenumber(prompt):
    while True:
        try: 
            number = float(input(prompt))
            break
        except ValueError:
            print("not a valid number, try again")
    return number


print("Welcome to Tommy's calculator.")

def start():
    To start, choose an operator. Type add, subtract, multiply, or divide: ")


print(add(choosenumber("choose first number to add: "), choosenumber("choose second number to add: ")))



