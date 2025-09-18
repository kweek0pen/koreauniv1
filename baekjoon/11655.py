import sys

S = sys.stdin.readline().rstrip()


for idx in range(len(S)):
    if 65 <= ord(S[idx]) <= 90:
        tmp = ord(S[idx]) + 13
        if tmp > 90:
            tmp = tmp - 26
        print(chr(tmp), end="")
        continue

    if 97 <= ord(S[idx]) <= 122:
        tmp = ord(S[idx]) + 13
        if tmp > 122:
            tmp = tmp - 26
        print(chr(tmp), end="")
        continue

    else: 
        print(S[idx], end="")
