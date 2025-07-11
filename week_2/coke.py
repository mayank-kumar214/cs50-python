cost = 50
coins = [5, 10, 25]

while cost > 0:
    print("Amount Due:", cost)
    insert = int(input("Insert Coin: "))
    
    if insert in coins:
        cost -= insert
    else:
        print("Invalid coin. Please insert 5, 10, or 25 cents.")

if cost < 0:
    print("Change Owed:", abs(cost))
else:
    print("Change Owed: 0")
