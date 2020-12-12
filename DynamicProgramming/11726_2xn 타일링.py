# #시간초과
# #재귀
# import sys
# r = sys.stdin.readline
#
# def d(n):
#     if n == 1: return 1
#     if n == 2: return 2
#     else:
#         return d(n-1) + d(n-2)
# n = int(r())
# print(d(n))


import sys
r = sys.stdin.readline

d = [0, 1, 2]
for i in range(3, 1001):
    d.append(d[i-2] + d[i-1])
n = int(r())
print(d[n] % 10007)

