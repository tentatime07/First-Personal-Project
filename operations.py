def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return x/y

def exponent(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return x%y



    

