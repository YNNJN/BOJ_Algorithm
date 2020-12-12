import sys
r = sys.stdin.readline

n = int(r())
a = list(map(int, r().split()))
d1 = [0 for i in range(n)]
d2 = [0 for i in range(n)]
d3 = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d1[i] < d1[j]:
            d1[i] = d1[j]
    d1[i] += 1
for i in range(n-1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and d2[i] < d2[j]:
            d2[i] = d2[j]
    d2[i] += 1
for i in range(n):
    d3[i] = d1[i] + d2[i] - 1
print(max(d3))