import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
diff = []

for i in range(n):
    board.append(input().strip())  

for i in range(n-7):
    for j in range(m-7):
        
        diff_0 = 0 #시작점 W
        
        for k in range(8):
            for l in range(8):
                if((k+l) % 2 == 0): #홀수번째 칸
                    if(ord(board[i+k][j+l]) % 2 == 0): #B일 때
                        diff_0 += 1

                else: #짝수번째 칸
                    if(ord(board[i+k][j+l]) % 2 == 1): #W일 때
                        diff_0 += 1

        diff.append(min(diff_0, 64 - diff_0))
diff.sort()      
print(diff[0])
