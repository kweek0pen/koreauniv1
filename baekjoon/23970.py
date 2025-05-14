import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def bubble_sort(a, b):
    if a == b:
        return 1
    for i in range(n - 1):
            swap = False
            for j in range(n - 1 - i):
                if (a[j] > a[j + 1]):
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swap = True
                    if (a[j+1] == b[j+1]): #필터링하는 것이 중요!
                        if a == b:
                            return 1
            if not swap:
                break
    return 0

print(bubble_sort(a, b))
