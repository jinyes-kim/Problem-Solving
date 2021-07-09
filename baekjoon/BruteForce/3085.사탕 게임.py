"""
1. 2차원 배열 순차 탐색
2. 행, 열 교환 가능 여부 체크
3. 변경하면 변경했을 때의 최대 값 체크
"""

# input
n = int(input())
board = [list(input()) for _ in range(n)]


# check function
def check(board, st_row, ed_row, st_col, ed_col):
    result = 1
    length = len(board)

    for row in range(st_row, ed_row+1):
        tmp_row = 1
        for i in range(1, length):
            if board[row][i] == board[row][i-1]:
                tmp_row += 1
                if tmp_row > result:
                    result = tmp_row
            else:
                tmp_row = 1

    for col in range(st_col, ed_col+1):
        tmp_col = 1
        for i in range(1, length):
            if board[i][col] == board[i-1][col]:
                tmp_col += 1
                if tmp_col > result:
                    result = tmp_col
            else:
                tmp_col = 1

    return result

# brute force
result = 0
for row in range(n):
    for col in range(n):
        if row+1 < n:
            board[row][col], board[row+1][col] = board[row+1][col], board[row][col]
            tmp = check(board, row, row+1, col, col)
            if tmp > result:
                result = tmp
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]

        if col+1 < n:
            board[row][col], board[row][col+1] = board[row][col+1], board[row][col]
            tmp = check(board, row, row, col, col+1)
            if tmp > result:
                result = tmp
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]

print(result)