import sys
input = sys.stdin.readline

n = int(input())
stack = []

while (n > 0):
    command = input().strip()

    if (command == 'pop'):
        if (len(stack) == 0):
            print('-1')
        else:
            tmp = stack.pop()
            print(tmp)

    elif (command == 'size'):
        print(len(stack))

    elif (command == 'empty'):
        print('1' if len(stack) == 0 else '0')

    elif (command == 'top'):
        print(stack[-1] if len(stack) > 0 else '-1')

    else:
        tmp, num = command.split()
        stack.append(int(num))

    n -= 1
