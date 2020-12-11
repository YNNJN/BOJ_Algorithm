'''
경사로 부적합 케이스

# 높이 차이가 1이 아닌 경우
# 경사로를 바닥과 접하게 놓지 않은 경우
# 겹쳐 놓은 경우
# 기울여서 놓은 경우

'''

def go(row, l):
    n = len(row)
    c = [0] * n
    for i in range(1, n):
        if row[i-1] != row[i]: # 높이가 같지 않은 경우
            diff = abs(row[i] - row[i-1])
            if diff != 1:
                return False
            # 높이 차가 1인 경우
            # 오른쪽이 더 높은 경우
            if row[i-1] < row[i]:
                for j in range(1, l+1): # 경사로의 길이만큼 반복
                    # 범위 초과
                    if i - j < 0:
                        return False
                    # 낮은 지점의 칸 높이가 동일하지 않거나, L만큼 연속되지 않은 경우
                    if row[i-1] != row[i-j]:
                        return False
                    # 겹쳐 놓은 경우
                    if c[i-j]:
                        return False
                    c[i-j] = True
            # 왼쪽이 더 높은 경우
            else:
                for j in range(l):
                    if i + j >= n:
                        return False
                    if row[i] != row[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 행 탐방
for i in range(n):
    d = graph[i]
    # print('행', d)
    if go(d, l):
        ans += 1

# 열 탐방
for j in range(n):
    d = [graph[i][j] for i in range(n)]
    # print('열', d)
    if go(d, l):
        ans += 1
print(ans)