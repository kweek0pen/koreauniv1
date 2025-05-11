import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def bubble_sort(a, k):
    count = 0
    for last in range(n-1, 0, -1):
        for i in range(0, last):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                count += 1
                if (count == k):
                    print(f'{a[i]} {a[i+1]}')
                    return
    if (count < k):
        print("-1")
bubble_sort(a, k)
