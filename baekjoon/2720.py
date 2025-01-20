import sys
input = sys.stdin.readline

def change(amount):
    global quarter, nickel, dime, penny
    quarter, nickel, dime, penny = 0, 0, 0, 0
    
    if(amount >= 25):
        quarter = amount // 25
        amount= amount % 25
    if(amount >= 10):
        dime = amount // 10
        amount = amount % 10
    if(amount >= 5):
        nickel = amount // 5
        amount = amount % 5
    if(amount >= 1):
        penny = amount
        
T = int(input())

for i in range(T):
    C = int(input())
    change(C)
    print(f'{quarter} {dime} {nickel} {penny}')
