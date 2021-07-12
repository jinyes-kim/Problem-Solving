def rotate(board, x1, y1, x2, y2):
    """
    1. 행렬에서 회전해야하는 부분 1차원 배열로 뽑아내기
    2. 1차원 배열 우측 한 칸 이동 및 최솟값 체크
    3. 1차원 배열 이용해서 행렬에 변수 할당
    """

    # x1,y1 -> x1, y2 / top-row
    # x2,y1 -> x2, y2 / right-col
    # x1,y1 -> x2, y1 / bot-row (reverse)
    # x2,y1 -> x2, y2 / left-col (reverse)
    
    # input option
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    
    # one dimension list
    value_list = []

    # top-row
    for i in range(y1, y2+1):
        value_list.append(board[x1][i])
    # right-col
    for j in range(x1 + 1, x2):
        value_list.append(board[j][y2])
    # bot-row (reverse)
    for i in range(y2, y1-1, -1):
        value_list.append(board[x2][i])
    # left-col (reverse)
    for j in range(x2-1, x1, -1):
        value_list.append(board[j][y1])

    # 1차원 배열에서 시계 방향으로 한 칸씩 이동
    start = value_list.pop()
    value_list.insert(0, start)
    
    # 최소값 체크
    minimum = min(value_list)

    
    # 회전한 1차원 배열로 행렬 재할당
    idx = 0
    # top-row
    for i in range(y1, y2+1):
        board[x1][i] = value_list[idx]
        idx += 1
    # right-col
    for j in range(x1 + 1, x2):
        board[j][y2] = value_list[idx]
        idx += 1
    # bot-row
    for i in range(y2, y1-1, -1):
        board[x2][i] = value_list[idx]
        idx += 1
    # left-col
    for j in range(x2-1, x1, -1):
        board[j][y1] = value_list[idx]
        idx += 1

    return board, minimum


def solution(rows, columns, queries):
    answer = []
    start = 1
    board = []
    for i in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(start)
            start += 1
        board.append(tmp)

    for query in queries:
        x1, y1, x2, y2 = query
        board, minium = rotate(board, x1, y1, x2, y2)
        answer.append(minium)

    return answer


