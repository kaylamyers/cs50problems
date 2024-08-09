menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = (0)
    while True:
        try:
            order = str(input("what would you like to order? ")).title() 
            if menu[order]:
                total += menu[order]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break # this error catches user input of cntrl-d to exit code
        except KeyError:
            print("that is not a menu item")


main()