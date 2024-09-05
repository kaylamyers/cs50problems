## names
name = input("What's your name? ")

file = open("names.txt", "a") # could also do "w" for write, "a" means append
file.write(f"{name}\n")
file.close()

    # can also do this...
name = input("What's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
# using with gets rid of close line, so that process is more automated after indentation

    # to read the file back, we use "r"
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())  # rstrip() take away extra strip because we added \n earlier

    # another way
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
    
    # sorting names before printing
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

    # sorting more simply
with open("names.txt") as file:
    for line in sorted(file):   # can add , reverse=True to make list from Z to A
        print(f"hello,", line.rstrip())

# csv files are commonly used for Excel or Google Spreadsheets
## students
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

    # what if we did this as a dictionary
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        # can also do this to make above 3 lines more concise
        # student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students):
    print(f"{student["name"]} is in {student["house"]}")

    # tell sorted function to specify what you want to sort by
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student["name"]} is in {student["house"]}")
# here we are passing the get_name function as an argument into another function
# passing in get_name to sorted as a value of the key parameter
# this is telling the function how to sort the list of dictionaries

    # another way to do this without creating a function
    # arguably better designed
    # lambda is an anonymous function
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

sortBy = 'name'
for student in sorted(students, key=lambda student: student[sortBy]):
    print(f"{student["name"]} is in {student["house"]}")

# changing approach to account for rows that have a column with a comma
# eg. Harry, "Four, Privet Dr" -- how do we deal w this case?
# eg. Malfoy, Malfoy Manor -- normal case here 
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    # the purpose of reader is to identify potential corner cases for you
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]}")

# can bake into csv file that name is first and home is second so there is no guessing
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    # the purpose of DictReader is to return dictionaries one at a time
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
        # students.append(row) -- this gives the same thing

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is in {student["house"]}")

# allowing user to input data to be stored in csv file
import csv

name = input("What's your name? ")
home = input("where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# doing same thing but in a dictionary
import csv

name = input("What's your name? ")
home = input("where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  # fieldnames goes hand in hand with DictWriter to associate names with columns
    writer.writerow({"name": name, "home": home})

## costume gif
# take as input 2 or more image files to create a gif
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

image[0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
