import sys

unit = sys.argv

if len(unit) == 2:
    if unit[1].endswith(".py"):
        try:
            with open(unit[1], "r") as file:
                lines = file.readlines()
                lineCount = 0
            for l in lines:
                if l.rstrip() and l.lstrip():
                    lineCount += 1
                if l.lstrip().startswith("#"):
                    lineCount -= 1
            print(lineCount)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

elif len(unit) > 2:
    sys.exit("Too many command-line arguments")
elif len(unit) <= 1:
    sys.exit("Too few command-line arguments")