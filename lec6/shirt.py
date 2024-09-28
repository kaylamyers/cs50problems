import sys
import os
from PIL import Image, ImageOps

formats = [".jpg", ".jpeg", ".png"]

if len(sys.argv) == 3 :
    arg1 = sys.argv[1].lower()
    arg1 = os.path.splitext(arg1)
    arg2 = sys.argv[2].lower()
    arg2 = os.path.splitext(arg2)

    if (arg1[1] in formats) and (arg2[1] in formats):
        if arg1[1] == arg2[1]:
            try:
                photo = Image.open(sys.argv[1])
                with Image.open("shirt.png") as tshirt:
                    dimensions = tshirt.size
                    resize = ImageOps.fit(photo, dimensions)
                    resize.paste(tshirt, tshirt)
                    resize.save(sys.argv[2])

            except FileNotFoundError:
                sys.exit("Input does not exist")
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

