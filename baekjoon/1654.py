import sys

K, N = map(int, sys.stdin.readline().split())

LANs = []
for i in range(K):
    LANs.append(int(sys.stdin.readline()))

start, end = 1, max(LANs)
while start <= end :
    count = 0
    mid = (start + end) // 2
    
    for LAN in LANs:
        count += LAN // mid
    if count < N:
        end = mid -1
    elif count >= N:
        result = mid
        start = mid + 1
        
print(result)

