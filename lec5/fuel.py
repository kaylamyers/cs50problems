def main():
    while True:
        try:
            frac = input("please provide fraction: ")
            numdem = convert(frac)
            percent = gauge(numdem)
            break
        except ValueError:
            print("please provide an integer for the numerator and denominator")
        except ZeroDivisionError:
            print("cannot divide by zero")

    print(percent)


def convert(fraction):
    num_dem = fraction.split("/")
    x = int(num_dem[0])
    y = int(num_dem[1])
    frac = round((x / y)*100)
    if x <= y:
        return frac
    elif y <= x:
        print("numerator must be less than denominator")


def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()