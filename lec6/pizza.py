import sys
import csv
from tabulate import tabulate

unit = sys.argv
menu = []

if len(unit) == 2:
    if unit[1].endswith(".csv"):
        try:
            with open(unit[1]) as file:
                #reader = csv.DictReader(file)
                for line in file:
                    pz, sm, lg = line.rstrip().split(",")
                    prices = {"pizza": pz, "small": sm, "large": lg}
                    menu.append(prices)
                print(tabulate(menu, headers="firstrow" ,tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

elif len(unit) > 2:
    sys.exit("Too many command-line arguments")
elif len(unit) <= 1:
    sys.exit("Too few command-line arguments")
    