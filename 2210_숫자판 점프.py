import sys
r = sys.stdin.readline

def dfs(r,c,num):
    if len(num) == 6:
        if num not in ans:
            ans.append(num)
        return

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num + arr[nr][nc])

arr = [list(r().split()) for _ in range(5)]
ans = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(ans))