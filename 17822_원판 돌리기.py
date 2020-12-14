'''
원판을 회전시킨 후, 적힌 수의 합을 출력

# 회전 함수 실행
# 수가 남았는지 체크
# 중복되는 수가 있다면 인접인지 체크하고 -> 지움
# 중복되는 수가 없다면 -> 값을 계산하여 갱신함

'''

from collections import deque
from itertools import chain

# 인접한 숫자를 체크하기 위한 함수 작성
def bfs(graph, y, x):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    value = graph[y][x]
    queue.append((y, x))
    visited = set()
    while queue:
        y, x = queue.popleft()
        visited.add((y, x))
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if nx == m:
                nx = 0
            if nx < 0:
                nx = m - 1
            if 0 < ny < len(graph) and graph[ny][nx] == value and (ny, nx) not in visited:
                queue.append((ny, nx))
                visited.add((ny, nx))
    return visited

# 원판의 값을 계산하는 함수 작성
def get_value(graph):
    flag = False
    for y in range(1, len(graph)):
        for x in range(len(graph[0])):
            cur = graph[y][x]
            if cur == 0:
                continue
            # 인접하면서 같은 숫자 찾기
            adj = bfs(graph, y, x)
            # 존재할 경우
            if len(adj) > 1:
                flag = True
                for ny, nx in adj:
                    graph[ny][nx] = 0

    # 인접한 수가 없는 경우
    if not flag and [i for i in chain(*graph) if i != 0]:
        avg = sum(chain(*graph)) / len([i for i in chain(*graph) if i != 0])
        for y in range(1, len(graph)):
            for x in range(len(graph[0])):
                if graph[y][x] != 0:
                    if graph[y][x] > avg:
                        graph[y][x] -= 1
                    elif graph[y][x] < avg:
                        graph[y][x] += 1
    return

# 회전하는 함수 작성
def circle_rotate(graph, x, k):
    for i in range(1, len(graph)):
        if i % x == 0:
            graph[i].rotate(k)
    return

n,m,t = map(int, input().split()) # 원판 수, 판 당 원소 수, 회전수
# 입력 받을 때부터 deque으로 받을 것. 이후 조작을 쉽게 하기 위해서
graph = [[0] * m]

for _ in range(n):
    row = deque(map(int, input().split()))
    graph.append(row)

for _ in range(t):
    x, d, k = map(int, input().split())  # x의 배수인 원판을 d 방향으로 k칸 회전
    k = k if d == 0 else -k # 반시계방향일 경우에 대한 처리
    circle_rotate(graph, x, k)
    get_value(graph)
print(sum(chain(*graph)))