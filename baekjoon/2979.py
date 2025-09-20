time = [0] * 100

A, B, C = map(int, input().split())
for i in range(3):
    arrival, leave = map(int, input().split())
    for j in range(arrival, leave):
        time[j] += 1

cost = 0    
for i in time:
    if i == 1:
        cost += A
    elif i == 2:
        cost += B * 2
    elif i == 3:
        cost += C * 3
        
print(cost)
