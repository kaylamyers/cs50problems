def main():
    camel = str(input("input in camelCase plz: ")).strip()
    print(switch(camel))

def switch(camel):
    for letter in camel:
        if letter.isupper():
            camel = camel.replace(letter, f"_{letter.lower()}")
    return camel

main()

