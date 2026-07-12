import operations

OPERATIONS = {
    "+": operations.add,
    "-": operations.subtract,
    "*": operations.multiply,
    "/": operations.divide,
    "^": operations.exponent,
    "%": operations.modulo,
}

def get_name():
        return input("What's your name?: ")

def get_operation(prompt):
    while True:
        symbol = input(prompt).strip()
        if symbol in OPERATIONS:
            return symbol, OPERATIONS[symbol]
        else:
            print("Not a valid operation, try again")

def get_number(prompt, allow_zero, allow_ans, ans):
    while True:
        res = input(prompt).strip().lower()
        if res == "ans":
            if allow_ans:
                return ans
            else:
                print("No previous ans available yet")
                continue
        else: 
            try:
                number = float(res)
            except ValueError:
                print("Not a valid number, try again")
                continue
        if not allow_zero and number == 0:
            print("cannot divide/mod by zero")
        else:
            return number

def get_next_action(prompt, history, name):
    while True:
        res = input(prompt).strip().lower()
        if res == "e":
            print(f"Goodbye! See you {name}.")
            return "exit"
        elif res == "v":
            print_history(history)
        elif res == "c":
            history.clear()
            print("history cleared!")
        elif res == "a":
            return 
        else: 
            print("not a valid input")

def print_history(history):
    if not history:
        print("History is empty!")
        return
    print("\nCalculation history:")
    for calculation in history:
        print(calculation)
    
def start():
    history = []
    first = True
    result = 0

    print("Welcome to Tommy's calculator.")
    name = get_name()

    while True:
        if first:
            prompt = f"Hi {name}. To start, choose an operator. Type +, -, *, /, ^, or %: "
        else:
            prompt = f"Sure {name}. To start, choose an operator. Type +, -, *, /, ^, or %: "

        symbol, operation_func = get_operation(prompt)

        if first:
            number1 = get_number("Now, choose your first number: ", True, False, result)
            number2 = get_number("Now, choose your second number: ", symbol not in ("/", "%"), False, result)
        else:
            number1 = get_number(f"Now, choose your first number, or type ans (ans = {result}): ", True, True, result)
            number2 = get_number(f"Now, choose your second number, or type ans (ans = {result}): ", symbol not in ("/", "%"), True, result)

        result = operation_func(number1, number2)
        calculation = f"{number1} {symbol} {number2} = {result}"

        print(calculation)
        history.append(calculation)
        print("Calculation history updated!")

        action = get_next_action("\nv for view history\nc for clear history\na for another calculation\ne for exit (history will not save)\n", history, name)
        if action == "exit":
            break
        first = False

start()




















