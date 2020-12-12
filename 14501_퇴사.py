'''
상담은 동기로 수행
퇴사 전에 할 수 있는 상담의 최대 이익을 구하기

'''

def dfs(i, sum):
    # 종료조건
    if i == n+1:
        global ans
        ans = max(ans, sum)
        return
    # i번째 날 일하는 경우
    if i + t[i] <= n + 1:
        dfs(i + t[i], sum + p[i])
    # i번째 날 일하지 않는 경우
    if i + 1 <= n + 1:
         dfs(i+1, sum)

n = int(input())
t, p = [0], [0]
for _ in range(n):
    ti, pi = list(map(int, input().split()))
    t.append(ti)
    p.append(pi)

ans = 0
dfs(1, 0)
print(ans)

