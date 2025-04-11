import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort()
sum = 0

for i in range(n-2):
    for k in range(i+1, n-1):
            for j in range(k+1, n):
                if (((cards[i]+cards[j]+cards[k]) <= m) & ((cards[i]+cards[j]+cards[k]) > sum)):
                    sum = cards[i]+cards[j]+cards[k]
                else: continue

print(sum)
