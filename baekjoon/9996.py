import sys

def check_pattern(string, start, end):
    if len(string) >= len(start) + len(end) and string.startswith(start) and string.endswith(end):
        return "DA"
    return "NE"

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    pattern = sys.stdin.readline().strip()
    start, end = pattern.split('*')
    filename = []
    for _ in range(N):
        filename.append(sys.stdin.readline().strip())
    for name in filename:
        print(check_pattern(name, start, end))
