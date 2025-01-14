import sys
input = sys.stdin.readline
N, M = map(int, input().split())

tmpList = []
def dfs():
    if len(tmpList) == M : 
        for i in range(M):
            print(tmpList[i], end = ' ')
            return
        for i in range(1, N+1):
            tmpList.append(i)
            dfs()
            tmpList.pop()
            
dfs()
