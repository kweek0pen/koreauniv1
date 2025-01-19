import sys
input = sys.stdin.readline

def dfs(depth, index):
    if (depth == 6):
        print(*tmp_list) #print(' '.join(map(str, tmp_list)))을 통해 속도 줄일 수
        return
    
    for i in range(index, k):
        tmp_list.append(S[i])
        dfs(depth+1, i + 1)
        tmp_list.pop()
        
while True:
    arr = list(map(int,input().split()))
    k = arr[0]
    S = arr[1:]
    tmp_list = []
    dfs(0, 0)
    if(k == 0):
        exit()
    print()
