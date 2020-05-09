def comb(d, s): #depth, start
    if s == 6:
        for i in range(6):
            print('{}'.format(ans[i]), end=' ')
        print()
        return
    for i in range(d, k):
        ans[s] = a[i]
        comb(i+1, s+1)

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    a = arr[1:]
    ans = [0 for _ in range(k)]
    comb(0, 0)
    print()
