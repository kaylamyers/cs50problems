def main():
    t = str(input("what time is it, homes? "))

    if convert(t) >= 7 and convert(t) <= 8:
        print("breakfast time")
    elif convert(t) >= 12 and convert(t) <= 13:
        print("lunch time")
    elif convert(t) >= 18 and convert(t) <= 19:
        print("dinner time")


def convert(time):
    split = time.partition(":")
    front = int(split[0])
    end = int(split[2])
    frac = float(end / 60)
    newTime = float(front + frac)
    return(newTime)


if __name__ == "__main__":
    main()

# try am & pm challenge