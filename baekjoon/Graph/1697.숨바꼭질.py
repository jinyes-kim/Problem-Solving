from collections import deque

limit = 200000
check = [False] * (limit+1)
dist = [-1] * (limit+1)
n, m = map(int, input().split())
check[n] = True
dist[n] = 0
q = deque()
q.append(n)

while q:
    current = q.popleft()
    for next_node in [current-1, current+1, current*2]:
        if 0 <= next_node <= limit and not check[next_node]:
            dist[next_node] = dist[current]+1
            check[next_node] = True
            q.append(next_node)

print(dist[m])
