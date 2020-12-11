'''
모든 간선 비용이 동일하므로 bfs를 이용해 최단거리 구함

'''

from collections import deque


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
dist = [-1] * (n + 1)
dist[x] = 0

# bfs
queue = deque([x])
while queue:
    now = queue.popleft()
    # 이동 가능한 모든 도시를 확인
    for next_node in graph[now]:
        if dist[next_node] == -1:
            # 다음 노드가 방문하지 않은 도시라면 최단거리 갱신
            dist[next_node] = dist[now] + 1
            queue.append(next_node)

# 최단거리 k인 것 셀렉
flag = False
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)
