n, m, x, y, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0]*7
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for k in order:
    k -= 1
    nx, ny = x+dx[k], y+dy[k]
    if not (0 <= nx < n) or not (0 <= ny < m):
        continue
    if k == 0: # 동
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp
    elif k == 1: # 서
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
    elif k == 2: #북
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
    else: #남
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp

    x, y = nx, ny
    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0
    print(dice[1])
