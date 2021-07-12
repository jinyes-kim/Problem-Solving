def go(board, l):
    n = len(board)
    check = [False] * n

    for i in range(1, n):
        if board[i-1] != board[i]:
            diff = abs(board[i] - board[i-1])
            if diff != 1:
                return False

            # left
            if board[i-1] < board[i]:
                for j in range(1, l+1):
                    if i-j < 0:
                        return False
                    if board[i-1] != board[i-j]:
                        return False
                    if check[i-j]:
                        return False
                    check[i-j] = True

            # right
            else:
                for j in range(l):
                    if i+j >= n:
                        return False
                    if board[i] != board[i+j]:
                        return False
                    if check[i+j]:
                        return False
                    check[i+j] = True

    return True


n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# row
for row in board:
    if go(row, l):
        answer += 1

# col
for i in range(n):
    col = [board[j][i] for j in range(n)]
    if go(col, l):
        answer += 1

print(answer)