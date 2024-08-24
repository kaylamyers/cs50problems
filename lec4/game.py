import random

def main():
    num = level()
    prompt(num)

def level():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return n
        except ValueError:
            print("please input an integer")


def prompt(n):
    win = random.randrange(1, n)
    while True:
        try:
            g = int(input("Guess: "))
            if g < win:
                print("Too small!")
            elif g > win:
                print("Too large!")
            elif g == win:
                print("Just right!")
                exit()
        except ValueError:
            print("please input an integer")


main()
