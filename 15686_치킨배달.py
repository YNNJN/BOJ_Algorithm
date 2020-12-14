from itertools import combinations

# 도시의 치킨거리 계산 함수 작성
def get_dist(candidate):
    ans = 0
    for hx, hy in house:
        min_value = 1e9
        for cx, cy in candidate:
            min_value = min(min_value, abs(hx - cx) + abs(hy - cy))
        ans += min_value
    return ans

n,m = map(int, input().split())
chicken, house = [], []

# 도시 맵 데이터 입력 받아서, 치킨집과 집의 위치를 저장
for r in range(n):
    row = list(map(int, input().split()))
    for c in range(n):
        if row[c] == 2:
            chicken.append((r,c))
        elif row[c] == 1:
            house.append((r,c))

# m개를 선택하는 모든 조합
candidates = list(combinations(chicken, m))

# 조합 중 최소 도시의 치킨거리 값을 출력
ans = 1e9
for candidate in candidates:
    ans = min(ans, get_dist(candidate))
print(ans)