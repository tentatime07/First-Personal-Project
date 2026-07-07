def add(x, y):
    return x + y

while True:
    try:
        first_input = float(input("type first number to add here: "))
        break
    except ValueError:
        print("please choose a number")
    
while True:
    try:
        second_input = float(input("type second number to add here: "))
        break
    except ValueError:
        print("please choose a number")

sum = add(first_input, second_input)
res = input("ready to see sum? type yes or no here: ")

if res == "yes":
    print(sum)
elif res == "no":
    print("u suck")
else:
    print("learn to follow instructions")
