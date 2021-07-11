from collections import deque

limit = 200000
check = [False] * (limit+1)
dist = [-1] * (limit+1)
n, m = map(int, input().split())
check[n] = True
dist[n] = 0
q = deque()
next_q = deque()

q.append(n)

while q:
    current = q.popleft()
    if 0 <= current*2 <= limit and not check[current*2]:
        dist[current*2] = dist[current]
        check[current*2] = True
        q.append(current*2)

    for next_node in [current-1, current+1]:
        if 0 <= next_node <= limit and not check[next_node]:
            dist[next_node] = dist[current]+1
            check[next_node] = True
            next_q.append(next_node)

    if not q:
        q = next_q
        next_q = deque()

print(dist[m])

