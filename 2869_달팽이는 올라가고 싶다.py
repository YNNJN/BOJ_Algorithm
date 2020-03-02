a,b,v = map(int, input().split())
h, day = 0, 0

while h != v:
    h += a
    if h == v:
        pass
    else:
        h -= b
    day +=1
print(day)
