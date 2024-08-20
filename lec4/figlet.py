from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) >= 2 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts:
    message = str(input("input a message: "))
    user_font = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(message))
    
elif len(sys.argv) == 1:
    message = str(input("input a message: "))
    user_font = random.choice(fonts)
    print(figlet.renderText(message))

else:
    sys.exit("invalid usage")
