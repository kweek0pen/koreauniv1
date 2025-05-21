import sys
import math
input = sys.stdin.readline

n = int(input())
#행렬 입력받아 m에 저장
m = [list(map(int, input().split()))for _ in range(n)]

print((math.factorial(2 * n) // (math.factorial(n) ** 2))%1000000007,n**2)
