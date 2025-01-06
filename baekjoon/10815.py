import sys

input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))

M = int(input())
givenList = list(map(int, input().split()))

dictionary = {}
for i in range(N):
    dictionary[card[i]] = -1
    
for i in givenList:
    if i in dictionary:
        print(1, end=" ")
    else:
        print(0, end=" ")
