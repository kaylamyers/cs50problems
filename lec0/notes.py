name = input("what's ur name homie? ").strip().capitalize().title()  # ask user for their name
# strip removes excess user input white space
# captializes only applies to first letter, not if you have multiple words
# title capitalizes first letter of all words (dont need capitalize funtion if u have this)

print(f"hello, {name}")

"""
yoooo what up 
i love block comments
toungue sticky out face eeehhhhhh
"""

# split users name into first and last
name = input("what's ur name homie? ").strip().title()  # ask user for their name
first, last = name.split(" ")

# calculator 
x = float(input("x? "))
y = float(input("y? "))
z = round(x + y)

print(f"{z:,}") # having the :, after z allows for there to be a comma every 3 digits

# creating a function
def main():
    x = int(input("whats x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()

