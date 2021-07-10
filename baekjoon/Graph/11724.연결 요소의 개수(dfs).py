# pypy3

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


def dfs(start):
    global check
    check[start] = True

    for next_node in graph[start]:
        if not check[next_node]:
            dfs(next_node)


answer = 0
for i in range(1, n+1):
    if not check[i]:
        dfs(i)
        answer += 1

print(answer)