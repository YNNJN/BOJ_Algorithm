import sys
r = sys.stdin.readline

# def bfs(v):
#     visited[v] = 1
#     q = [v]
#     while q:
#         v = q.pop(0)
#         for e in adj[v]:
#             if not visited[e]:
#                 visited[e] = -1 * visited[v]
#                 q.append(e)
#             elif visited[e] == visited[v]:
#                 return 1
#     return 0
#
# k = int(r())
# while k:
#     v,e = map(int, r().split())
#     adj = [[] for _ in range(v+1)]
#     visited = [0]*(v+1)
#
#     for _ in range(e):
#         e_info = list(map(int, r().split()))
#         adj[e_info[0]].append(e_info[1])
#         adj[e_info[1]].append(e_info[0])
#
#     ans = 0
#     for i in range(1, len(visited)):
#         if not visited[i]:
#             ans = bfs(i)
#             if ans == 1:
#                 break
#     print(adj)
#     if ans == 0:
#         print('YES')
#     else:
#         print('NO')
#     k -= 1

def dfs(v,c):
    color[v] = c
    for i in range(len(adj[v])):
        next = adj[v][i]
        if not color[next]:
            dfs(next, 3-c) # 1->2, 2->1, 따라서 c->3-c

k = int(input())
for tc in range(k):
    v,e = map(int, input().split())
    adj = [[] for _ in range(v+1)]
    color = [0]*(v+1)

    for _ in range(e):
        e_info = list(map(int, input().split()))
        adj[e_info[0]].append(e_info[1])
        adj[e_info[1]].append(e_info[0])
    dfs(1,1)

    ans = 0
    for i in range(1, v+1):
        for p in range(len(adj[i])):
            j = adj[i][p]
            if color[i] == color[j]:
                ans = 1
    if ans == 0:
        print('YES')
    else:
        print('NO')