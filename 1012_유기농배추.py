dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    stack = []
    stack.append([r, c])
    arr[r][c] = 0  # 현재위치의 배추 없애기
    while stack:
        cur = stack.pop()
        for k in range(4):
            nr, nc = cur[0] + dr[k], cur[1] + dc[k]
            if arr[nr][nc] == 1:
                arr[nr][nc] = 0
                stack.append([nr, nc])

T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M + 2)] for _ in range(N + 2)]  # 맵의 테두리를 0으로 채우기위해
    for _ in range(K):
        x, y = map(int, input().split())  # 배추위치 읽어서
        arr[y + 1][x + 1] = 1  # 배추위치에 1로 표시
    cnt = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if arr[i][j] == 1:  # 배추가 있으면
                dfs(i, j)
                cnt += 1
    print(cnt)