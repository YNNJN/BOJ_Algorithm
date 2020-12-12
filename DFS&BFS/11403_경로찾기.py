def search(v):
    q = []
    q.append(v)
    visited = [0] * n
    visited[v] = 1

    while q:
        t = q.pop(0)
        for k in range(n):
            w = adj[t][k]
            if k != v and visited[k]: continue
            if w == 1:
                visited[k] = 1
                adj_copy[v][k] = 1
                q.append(k)
    return


n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
adj_copy = [[0] * n for _ in range(n)]

l = []
for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:
            search(i)

for row in adj_copy:
    print(' '.join(map(str, row)))
