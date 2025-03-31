N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

answer_0 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
answer_1 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

min_diff = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        diff_0 = 0
        diff_1 = 0
        for k in range(8):
            for l in range(8):
                if board[i + k][j + l] != answer_0[k][l]:
                    diff_0 += 1
                if board[i + k][j + l] != answer_1[k][l]:
                    diff_1 += 1
        min_diff = min(min_diff, diff_0, diff_1)

print(min_diff)
