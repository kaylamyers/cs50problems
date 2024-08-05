math = input("type a math problem: ")

parts = math.split(" ", 2) # splitting user input into 3 sections

x = float(parts[0])
y = float(parts[2])

if parts[1] == "+":
    z = round(x + y, 1)
    print(z)
elif parts[1] == "-":
    z = round(x - y, 1)
    print(z)
elif parts[1] == "*":
    z = round(x * y, 1)
    print(z)
elif parts[1] == "/":
    z = round(x / y, 1)
    print(z)
