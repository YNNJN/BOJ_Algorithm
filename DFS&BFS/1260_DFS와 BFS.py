def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for e in adj[v]:
        if not visited[e]:
            dfs(e)

def bfs(v):
    q = [v]
    visited = [0]*(n+1)

    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    link = input().split()
    adj[int(link[0])].append(int(link[1]))
    adj[int(link[1])].append(int(link[0]))

for e in adj:
    e.sort() #방문할 수 있는 정점이 여러개일 경우 정점 번호가 작은 것을 먼저 방문해야

dfs(v)
print()
bfs(v)