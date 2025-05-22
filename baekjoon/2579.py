import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

score = [0]*(n)

if n<= 2:
	print(sum(stairs))
else:
	score[0] = stairs[0]
	score[1] = stairs[0] + stairs[1]
	score[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
  for k in range(3,n):
      score[k] = max(score[k-1]+score[k-3]+stairs[k], score[k-2]+stairs[k])
        
print(score[n])
