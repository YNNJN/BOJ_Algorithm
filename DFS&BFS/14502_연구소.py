'''
벽의 개수 3개 세우고 -> 안전 영역의 크기를 계산함 (dfs/bfs)
조합 구해서 그에 대해서만 계산도 가능

'''

n,m = map(int, input().split())

# 초기 맵 데이터
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 벽 설치 후의 맵 데이터
temp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 바이러스 퍼뜨리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전영역 계산하기
def get_area():
    area = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0: area += 1
    return area

# 벽 설치 & 안전영역 계산
def dfs(cnt):
    global result
    # 벽 3개 설치 완료
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                # 벽 설치한 맵 데이터 이전
                temp[i][j] = graph[i][j]

        # 바이러스 위치에서 전파 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전영역의 최대값 계산
        result = max(result, get_area())
        return

    # 벽 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                graph[i][j] = 0
                cnt -= 1
dfs(0)
print(result)

