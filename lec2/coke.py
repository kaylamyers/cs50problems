coke = 50  # price of a coke
coins = [5, 10, 25]

while coke > 0:
    print(f"Amount Due: {coke}")
    money = int(input("Insert Coin: "))
    if money in coins:
        coke -= money
        if coke <= 0:
            print(f"Change Owed: {abs(coke)}")

