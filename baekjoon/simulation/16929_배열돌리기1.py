# 범위 구하기
# 1차원 배열로 분해
# 이동하고 2차원 배열로 재조립

n, m, r = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
group_n = min(n, m)//2
groups = []

# 1차원으로 분해
for k in range(group_n):
    group = []
    for j in range(k, m-k): # top
        group.append(arr[k][j])
    for i in range(k+1, n-1-k): # right
        group.append(arr[i][m-1-k])
    for j in range(m-k-1, k, -1):   # bot
        group.append(arr[n-1-k][j])
    for i in range(n-k-1, k, -1):   # left
        group.append(arr[i][k])
    groups.append(group)

# 인덱스 이동 및 2차원 재조립
for k in range(group_n):
    group = groups[k]
    length = len(group)
    idx = r % length
    for j in range(k, m-k):
        arr[k][j] = group[idx]
        idx = (idx+1) % length
    for i in range(k+1, n-k-1):
        arr[i][m-1-k] = group[idx]
        idx = (idx+1) % length
    for j in range(m-k-1, k, -1):
        arr[n-1-k][j] = group[idx]
        idx = (idx+1) % length
    for i in range(n-k-1, k, -1):
        arr[i][k] = group[idx]
        idx = (idx+1) % length

for row in arr:
    print(' '.join(map(str, row)))
    