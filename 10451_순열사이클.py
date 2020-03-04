import sys
r = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    next = s[v]
    if not visited[next]:
        dfs(next)

t = int(r())
for tc in range(t):
    n = int(r())
    s = [0] + list(map(int, r().split()))
    visited = [0]*(n+1)
    ans = 0

    for i in range(1, len(visited)):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)