def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print(plate)
        print("Valid")
    else:
        print(plate)
        print("Invalid")


def is_valid(plate):
    if start(plate) and length(plate) and nums(plate) and noPunc(plate):
        return True
    else:
        return False

def length(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False

def start(plate):
    for value in plate[0:2]:
        if value.isalpha():
            plate += value
        else:
            return False
    return plate
    
def nums(plate):
    values = list(plate)
    for val in values[0:len(values)-1]:
        pos = values.index(val)
        if val.isalpha():
            if values[pos + 1] == '0':
                return False
        elif val.isdigit():
            if values[pos + 1].isalpha():
                return False
    return plate

def noPunc(plate):
    if plate.isalnum():
        return True
    else:
        return False


if __name__ == "__main__":
    main()