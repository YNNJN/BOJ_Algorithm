import sys
r = sys.stdin.readline

a,p = map(int, r().split())
d = [a]

while True:
    s = d[-1]
    val = 0
    while s:
        val += ((s%10)**p)
        s = s//10
    if val in d:
        print(d.index(val))
        break
    else:
        d.append(val)
