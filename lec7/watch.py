import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    matches = re.search(r"^(<iframe).+?(src=\"https?://)(www.)?(youtube\.com/embed/)([\w].+)\".+$", s, re.IGNORECASE)
    
    if matches:
        return ("https://youtu.be/" + matches.group(5))


if __name__ == "__main__":
    main()
