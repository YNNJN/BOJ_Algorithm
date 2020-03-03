import sys
r = sys.stdin.readline
n = int(r())
a = list(map(int, r().split()))

d = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))

