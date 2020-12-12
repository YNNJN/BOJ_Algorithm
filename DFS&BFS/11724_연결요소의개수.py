import sys
r = sys.stdin.readline

# #dfs풀이
# def dfs(v):
#     visited[v] = 1
#     for e in adj[v]:
#         if not visited[e]:
#             dfs(e)
#
# n,m = map(int, r().split())
# adj = [[] for _ in range(n+1)]
# visited = [0]*(n+1)
# cnt = 0
#
# for i in range(m):
#     data = list(map(int, r().split()))
#     adj[data[0]].append(data[1])
#     adj[data[1]].append(data[0])
#
# for i in range(1, len(visited)):
#     if not visited[i]:
#         cnt += 1
#         dfs(i)
# print(cnt)

# #bfs풀이
# #오호 시간초과
# def bfs(v):
#     q = [v]
#     while q:
#         v = q.pop(0)
#         if not visited[v]:
#             visited[v] = 1
#             for e in adj[v]:
#                 if not visited[e]:
#                     q.append(e)

#retry
def bfs(v):
    visited[v] = 1
    q = [v]
    while q:
        v = q.pop(0)
        for i in range(len(adj[v])):
            e = adj[v][i]
            if not visited[e]:
                visited[e] = 1
                q.append(e)

n, m = map(int, r().split())
adj = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):
    u,v = list(map(int, r().split()))
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, len(visited)):
    if not visited[i]:
        cnt += 1
        bfs(i)
print(cnt)
