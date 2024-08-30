import random

def main():
    global score
    score = 10

    level = get_level()

    for _ in range(10):
        generate_integer(level)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    tries = 0

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    while True:
        try:
            ans = x + y
            guess = int(input(f"{x} + {y} = "))
            if guess != ans:
                print("EEE")
                tries += 1
                if tries == 3:
                    print(ans)
                    global score 
                    score -= 1
                    break
            elif guess == ans:
                break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
