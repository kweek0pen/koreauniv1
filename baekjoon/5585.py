paid = int(input())
amount = 1000 - paid
count = 0
coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    count += (amount // coin)
    amount %= coin
    
print(count)
