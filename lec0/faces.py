def main():
    mood = str(input("how are ya today? "))
    print(convert(mood))

def convert(mood):
    mood = mood.replace(":)", "🙂")
    mood = mood.replace(":(", "🙁")
    return mood

main()