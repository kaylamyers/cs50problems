def main():
    tweet = str(input("mm whatcha say: "))
    print(cons(tweet))

def cons(tweet):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in tweet:
        if letter in vowels:
            tweet = tweet.replace(letter, '')
    return tweet


main()

