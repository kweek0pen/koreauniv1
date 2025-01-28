import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

#네트워크 저장할 행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
	a,b = map(int, input().strip().split())
	graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited = [0]*(N+1)

#dfs 함수 만들기
def dfs(V):
	visited[V] = 1 #방문처리
	for i in range(1, N+1):
		if graph[V][i] == 1 and visited[i] == 0:
			dfs(i)
	
dfs(1)		
print(visited.count(1) - 1)
