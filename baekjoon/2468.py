import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    global count
    queue = deque()
    queue.append((i, j))
    sink[i][j] = True
    count += 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if sink[nx][ny] == False:
                sink[nx][ny] == True
                queue.append((nx, ny))


N = int(input())
for _ in range(N):
    area = [list(map(int, input().split()))]
rains = max(map(max, area))

counts = []
for depth in range(rains):
    count = 0
    sink = [[False for _ in range(N)]for i in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] <= depth:
                sink[i][j] = True
        for i in range(N):
            for j in range(N):
                if sink[i][j] == False:
                    bfs(i, j)
        counts.append(count)
        
print(max(counts))
