import sys
input = sys.stdin.readline

N = int(input())
durations = list(map(int, input().split()))
time = 0
total = 0

durations.sort()

for duration in durations:
    time += duration
    total += time
    
print(total)
