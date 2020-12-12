import sys
r = sys.stdin.readline
n = int(r())
a = list(map(int, r().split()))

#M1
# d = [0 for i in range(n)]
# for i in range(n):
#     s = []
#     for j in range(i):
#         if a[i] < a[j]:
#             s.append(d[j])
#     if not s:
#         continue
#     else:
#         d[i] += max(s)+1
# print(max(d)+1)

#M2
d = [0 for i in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))