import sys
input = sys.stdin.readline

def change(amount, coin):
	global count
	if (amount // coin > 0):
	    count += (amount // coin)
	    return amount % coin
	return amount
	
paidAmount = int(input().strip())
amount = 1000 - paidAmount
count = 0
coins = [500, 100, 10, 5, 1]
for coin in coins:
	change(amount, coin)
	
print(count)
