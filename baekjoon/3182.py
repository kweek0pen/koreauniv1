import sys
input = sys.stdin.readline

N = int(input())
info = [0]
for i in range(N):
    info.append(int(input()))

ask = [0] * (N+1)
for i in range(1, N+1):
    visited = [False] * (N + 1)
    j = i
    while not visited[j]:
        visited[j] = True
        ask[i] += 1
        j = info[j]

print(ask.index(max(ask)))
