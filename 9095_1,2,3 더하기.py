import sys
r = sys.stdin.readline

t = int(r())
d = [1, 2, 4]
for i in range(3, 10):
    d.append(d[i-3] + d[i-2] + d[i-1])
for i in range(t):
    n = int(r())
    print(d[n-1])