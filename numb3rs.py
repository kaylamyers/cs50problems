import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.match(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        if matches:
            g1 = int(matches.group(1))
            g2 = int(matches.group(2))
            g3 = int(matches.group(3))
            g4 = int(matches.group(4))

        if (0 <= g1 <= 255) and (0 <= g2 <= 255) and (0 <= g3 <= 255) and (0 <= g4 <= 255):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()