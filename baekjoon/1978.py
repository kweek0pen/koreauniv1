import sys
input = sys.stdin.readline
n = int(input())
numbers = []
primes = []

numbers = map(int, input().split())

for number in numbers: #numbers list 순회
    #print(number)
    if number == 2:
        primes.append(number)
    for k in range(2, number):
        #print(k, end = ' ')
        if number % (k) == 0: #number이 k로 나눠 떨어지면 break
            break
        if (k+1) == number:
            #print(f'{k+1} is the same as {number}\n')
            primes.append(number)

print(len(primes))
