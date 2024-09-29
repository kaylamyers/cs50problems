import re


def main():
    print(count(input("Text: ")))


def count(s):
    umCount = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(umCount)


if __name__ == "__main__":
    main()