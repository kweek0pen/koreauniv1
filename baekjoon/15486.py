import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []

for _ in range(n):
    tmp = input().split()
    t.append(int(tmp[0]))
    p.append(int(tmp[1]))

dp = [0] * (n+1) #idx+1날부터 얻을 수 있는 가장 큰 수익 기록
#dp[n]은 0으로 초기화되어 있음

for day in range(n-1, -1, -1):
    if(day+t[day] <= n):
        dp[day] = max(p[day] + dp[day+t[day]], dp[day+1]) #스킵하거나 그날 들어온 환자 상담하거나
    else:
        dp[day] = dp[day+1]
print(dp[0])
