import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
givenList = list(map(int, sys.stdin.readline().split()))
A.sort()

for i in givenList :
    left = 0
    right = N-1
    isExist = False
    
    while left <= right :
        mid = (left + right) // 2
        if A[mid] == i :
            isExist = True
            print(1)
            break
        elif A[mid] < i :
            left = mid + 1
        else :
            right = mid - 1
    if not isExist :
        print(0)
