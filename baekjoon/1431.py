import sys
input = sys.stdin.readline

N = int(input())
serials = {}
for _ in range(N):
    sNumber = input().rstrip()
    serials[sNumber] = 0
    for i in sNumber:
        if i.isdigit():
            serials[sNumber] += int(i)
sorted_serials = sorted(serials.keys(), key=lambda x: (len(x), serials[x], x))

for j in sorted_serials:
    print(j)
