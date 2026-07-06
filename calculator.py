def add(x, y):
    return x + y

hi = input("type first number to add here: ")
if not hi.isnumeric():
    raise KeyError()
hi2 = input("type second number to add here: ")

if not hi2.isnumeric():
    raise KeyError()


sum = float(hi) + float(hi2)
res = input("ready to see sum? type yes or no here: ")

if res == "yes":
    print(sum)
elif res == "no":
    print("u suck")
else:
    print("learn to follow instructions")
