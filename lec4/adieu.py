import inflect

p = inflect.engine()
adieu = []

while True:
    try:
        name = str(input('adieu to who? ')).capitalize().strip()
        adieu.append(name)

    except EOFError:
        goodbye = p.join((adieu))
        print("Adieu, adieu, to", goodbye)
        break
