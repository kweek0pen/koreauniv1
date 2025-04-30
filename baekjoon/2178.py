
from collections import deque

def find_shortest_path(N, M, maze):
    queue = deque([(0, 0, 1)])  # (행, 열, 거리)를 저장하는 큐
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, distance = queue.popleft()

        if x == N - 1 and y == M - 1: #목적지 칸
            return distance

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #최단경로의 일부라면
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

shortest_distance = find_shortest_path(N, M, maze)
print(shortest_distance)
