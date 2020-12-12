'''
첫 조합의 여집합은 마지막 조합임
즉 team[i]는 team[-i-1]와 완전히 반대임

'''

from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
combs = []

# 팀을 나누는 모든 조합 구하기
for comb in list(combinations([i for i in range(n)], n//2)):
    combs.append(comb)

min_value = 1000000
# 각 조합의 팀 점수 계산하기
for i in range(len(combs)//2):
    # 조합
    team = combs[i]
    score_a = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            score_a += graph[member][k]
    # 조합의 여집합
    team = combs[-i-1]
    score_b = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            score_b += graph[member][k]

    min_value = min(min_value, abs(score_a - score_b))
print(min_value)