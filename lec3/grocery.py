list = {}   # food: quantity

while True:
    try:
        item = str(input('')).upper().strip()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

    except EOFError:
        for item in sorted(list):
            print(list[item], item)
        break
