import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dic = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in dic:
            dic[word] += 1

        else:
            dic[word] = 1
sorted_dic = sorted(dic.keys(), key=lambda x: (-dic[x], -len(x), x))

for word in sorted_dic:
    print(word)
