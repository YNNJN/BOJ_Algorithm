import sys
r = sys.stdin.readline

t = int(r())
for i in range(t):
    d = []
    n = int(r())
    for k in range(2):
        d.append(list(map(int, r().split())))
    d[0][1] += d[1][0]
    d[1][1] += d[0][0]
    for s in range(2, n):
        d[0][s] += max(d[1][s-1], d[1][s-2])
        d[1][s] += max(d[0][s-1], d[0][s-2])
    print(max(d[0][n-1], d[1][n-1]))