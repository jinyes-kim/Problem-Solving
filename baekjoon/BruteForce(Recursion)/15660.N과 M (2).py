n, m = map(int, input().split())
ans = [0] * m
check_li = [False] * (n+1)


def go(idx):
    if idx == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        if check_li[i]:
            continue

        if idx == 0:
            ans[idx] = i
        else:
            if ans[idx-1] < i:
                ans[idx] = i
            else:
                continue
                
        check_li[i] = True
        go(idx+1)
        check_li[i] = False

go(0)