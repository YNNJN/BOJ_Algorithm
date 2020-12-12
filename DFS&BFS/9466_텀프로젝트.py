#어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산
import sys
sys.setrecursionlimit(100000)
r = sys.stdin.readline

def dfs(v, ans):
    visited[v] = 1
    cycle.append(v)
    num = nums[v]

    if visited[num]:
        if num in cycle:
            ans += cycle[cycle.index(num):]
        return
    else:
        dfs(num, ans)

t = int(r())
for tc in range(t):
    n = int(r())
    nums = [0] + list(map(int, r().split()))
    visited = [0]*(n+1)
    ans = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i, ans)

    print(n - len(ans))