import sys
input = sys.stdin.readline

def find_palindrome(word):
    reversed_word = ''.join(reversed(word))
    if reversed_word == word:
        print('yes')
    else:
        print('no')

def main():
    inputs = []
    while True:
        s = input().strip()
        if s == '0':
            break
        inputs.append(s)

    for word in inputs:
        find_palindrome(word)

if __name__ == '__main__':
    main()
