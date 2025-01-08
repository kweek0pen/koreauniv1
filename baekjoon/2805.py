N, M = map(int, input().split())
treeHeight = list(map(int, input().split()))

start, end = 1, max(treeHeight)
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in treeHeight:
        if i > mid:
            total += i - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)
