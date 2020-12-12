dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [0] * 7
move = list(map(int, input().split()))
# 1:동 2:서 3:북 4:남

for i in move:
    i -= 1
    # 0:동 1:서 2:북 3:남
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if i == 0: # 동
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
    elif i == 1: # 서
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
    elif i == 2: # 남
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
    else: # 북
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp

    x, y = nx, ny
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0

    print(dice[1])