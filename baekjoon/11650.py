import sys

n = int(input())
points = []

for i in range(n):
	[x, y] = map(int, sys.stdin.readline().split())
	points.append([x,y])

points.sort(key = lambda x:(x[0], x[1]))

for point in points:
	print(f"{point[0]} {point[1]}")
