from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()


def bfs(start):
    check = [False for _ in range(n+1)]
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        node = q.popleft()
        print(node, end=' ')
        for next_node in graph[node]:
            if not check[next_node]:
                q.append(next_node)
                check[next_node] = True


check = [False for _ in range(n+1)]


def dfs(start):
    global check
    check[start] = True
    print(start, end=' ')
    for next_node in graph[start]:
        if not check[next_node]:
            dfs(next_node)

dfs(start)
print()
bfs(start)
print()