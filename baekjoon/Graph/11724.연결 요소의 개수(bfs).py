# pypy3 

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    result = []
    check = [False for _ in range(n+1)]
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        node = q.popleft()
        result.append(node)
        for next_node in graph[node]:
            if not check[next_node]:
                q.append(next_node)
                check[next_node] = True

    return result


answer = 0
check = [False for _ in range(n+1)]
for i in range(1, n+1):
    if not check[i]:
        used_li = bfs(i)
        answer += 1

    for used in used_li:
        check[used] = True

print(answer)