import sys

s = sys.stdin.readline()
for i in range(26):
    print(s.count(chr(97 + i)), end=' ')
