#같은 수 여러 번 골라도 됨

def sequence(index, n, m):
    if index == m:
        for i in result:
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1):
        result[index] = i
        sequence(index+1, n, m)

n,m = map(int, input().split())
result = [0 for _ in range(m)]
sequence(0,n,m)