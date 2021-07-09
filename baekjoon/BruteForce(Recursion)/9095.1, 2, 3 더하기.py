n = int(input())
case_li = [int(input()) for _ in range(n)]
result = 0


def go(target, current_num):
    global result

    if target == current_num:
        result += 1
        return
    if target < current_num:
        return

    for i in range(1, 4):
        go(target, current_num+i)


for case in case_li:
    go(case, 0)
    print(result)
    result = 0

