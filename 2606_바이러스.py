def dfs(v):
    s.append(v)
    visited[v] = 1
    for w in g[v]:
        if visited[w]: continue
        dfs(w)
    return

n = int(input())
e = int(input())
g = [[] for _ in range(n+1)]

for _ in range(e):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visited = [0] * (n + 1)
s = []
dfs(1)

print(len(s) - 1)