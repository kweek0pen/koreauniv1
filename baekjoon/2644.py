import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 그래프

visited = [0] * (n + 1)
result = []

def dfs(v, depth):
    depth += 1
    visited[v] = 1
    
    if v == b:
        result.append(depth)
        return
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, depth)
    
dfs(a, 0)

print(result[0] - 1 if result else -1)
