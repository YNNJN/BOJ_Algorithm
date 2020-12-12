'''
연결 요소 개수 세기

'''

from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    # 8방 탐색 - 상/우상/우/우하/하/좌하/좌/좌상
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    queue = deque()
    ans = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                # 육지를 큐에 넣음
                queue.append((i,j))
                # 방문표시
                graph[i][j] = 2

                while queue:
                    cx, cy = queue.popleft()
                    for k in range(8):
                        nx = cx + dx[k]
                        ny = cy + dy[k]

                        # 범위체크
                        if 0 <= nx < h and 0 <= ny < w:
                            if graph[nx][ny] == 1:
                                # 육지를 큐에 넣음
                                queue.append((nx, ny))
                                # 방문표시
                                graph[nx][ny] = 2
                ans += 1
    print(ans)