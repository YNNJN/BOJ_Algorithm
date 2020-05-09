from sys import stdin
input = stdin.readline

def bfs(i,j):
    q = []
    q.append((i, j, 0))
    visited[i][j] = 1
    dist = 0

    while q:
        r, c, d = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr >= h or nc >= w or nr < 0 or nc < 0: continue
            if visited[nr][nc] == 0 and g[nr][nc] == 'L':
                q.append((nr, nc, d+1))
                visited[nr][nc] = 1
                dist = max(dist, d+1)
    return dist


h, w = map(int, input().split())
g = [list(input().strip()) for _ in range(h)]
visited = [[0] * w for _ in range(h)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

ans = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == 'L':
            visited = [[0] * w for _ in range(h)]
            ans = max(ans, bfs(i,j))
print(ans)
