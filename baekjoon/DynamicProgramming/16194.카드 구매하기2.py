n = int(input())
pack_li = [0] + list(map(int, input().split()))
d = [-1]*(n+1)
d[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        if d[i] == -1 or d[i] > d[i-j] + pack_li[j]:
            d[i] = d[i-j] + pack_li[j]

print(d[n])

