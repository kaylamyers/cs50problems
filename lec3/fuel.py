def main():
    f = math()
    print(f"your tank: {f}")

def math():
    while True:
        try:
            frac = input("please provide fraction: ")
            num_dem = frac.split("/")
            x = int(num_dem[0])
            y = int(num_dem[1])
            f = round((x / y)*100)
            if x <= y:
                break
            elif y <= x:
                print("numerator must be less than denominator")
        except ValueError:
            print("please provide an integer for the numerator and denominator")
        except ZeroDivisionError:
            print("cannot divide by zero")

    if f >= 99:
        return ("F")
    elif f <= 1:
        return ("E")
    else:
        return (f"{f}%")

main()

