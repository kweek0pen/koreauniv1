t = int(input())
for i in range(t):
    n = int(input())
    zero = [1, 0]
    one = [0, 1]
    if n > 1:
        for j in range(n-1):
            zero.append(one[-1])
            one.append(zero[-2] + one[-1])

    print(zero[n], one[n])

