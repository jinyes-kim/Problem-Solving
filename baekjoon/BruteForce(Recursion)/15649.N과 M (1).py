n, m = map(int, input().split())
check_li = [False] * (n+1)
ans = [0] * m


def go(idx):
    if idx == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        if check_li[i]:
            continue
        ans[idx] = i
        check_li[i] = True
        go(idx+1)
        check_li[i] = False


go(0)
