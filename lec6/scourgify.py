import sys
import csv

unit = sys.argv
students = []

if len(unit) == 3:
    if unit[1].endswith(".csv") and unit[2].endswith(".csv"):
        try:
            with open(unit[1], "r") as before:
                reader = csv.DictReader(before)
                for row in reader:
                    last, first = row["name"].split(",")
                    first = first.strip()
                    last = last.strip()
                    house = row["house"].strip()
                    students.append({"first": first, "last": last, "house": house})

                with open(unit[2], "w") as after:
                    writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in students:
                        writer.writerow(row)

        except FileNotFoundError:
            sys.exit(f"Could not read {unit[1]}")
    else:
        sys.exit("Not a Python file")

elif len(unit) > 3:
    sys.exit("Too many command-line arguments")
elif len(unit) < 3:
    sys.exit("Too few command-line arguments")
    
