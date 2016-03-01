
def give_change(amount):
    coins = [200,100,50,20,10,5]
    change = []


    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)

    if amount >= 3:
        change.append(5)
        return change
    else:
        return change

print give_change(13)





