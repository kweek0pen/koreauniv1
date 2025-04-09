a, b = map(int, input().split())

#a, b 중 작은 수를 min에 저장
min = a if a < b else b

for i in range(1, a+1):
	if (a % i == 0):
		if (b % i == 0):
			g = i #g에는 최대공약수가 저장됨
		else: continue
	else: continue

l = int((a / g) * (b / g) * g)
print(f"{g}\n{l}")
