import sys
input = sys.stdin.readline

dic = []

n = int(input())
for i in range(n):
    dic.append(input().strip())
    
set_dic = set(dic)
dic = list(set_dic) 

dic.sort()
dic.sort(key=len)

for word in dic:
    print(word)
