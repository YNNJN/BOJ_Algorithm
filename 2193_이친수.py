import sys
r = sys.stdin.readline

n = int(r())
d = [0, 1, 1]
for i in range(3, 91):
    d.append(d[i-1]+d[i-2])
print(d[n])