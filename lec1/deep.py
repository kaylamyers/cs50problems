life = input("what is the answer to the great question of life? ").lower().strip()

match life:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")
