import sys
input = sys.stdin.readline

N, K = map(int, input().split())
choices = []
for _ in range(N):
    choices.append(int(input()))
visited = []

def dfs(choices, start, visited):

    if start == K:
        return len(visited)

    if start in visited:
        return -1

    visited.append(start)
    return dfs(choices, choices[start], visited)

print(dfs(choices, 0, visited))
