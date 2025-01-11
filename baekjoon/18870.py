import sys
input = sys.stdin.readline

N = int(input())
inputArray = list(map(int, input().split()))

sortedArray = sorted(list(set(inputArray)))

dic = {sortedArray[i] : i for i in range(len(sortedArray))}
for i in inputArray:
    print(dic[i], end=' ')
