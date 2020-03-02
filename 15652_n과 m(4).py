#자연수 n과 m이 주어졌을 때, 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램
#같은 수 여러번 골라도 되고, 고른 수열은 비내림차순

def sequence(index, n, m):
    if index == m:
        for i in result:
            print(i,end=' ')
        print()
        return
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        result[index] = i
        for j in range(i): #i보다 작은 수 모두 visited
            visited[j] = 1
        sequence(index+1, n, m)
        for j in range(1, n+1): #visited 초기화
            visited[j] = 0

n,m = map(int, input().split())
visited = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]
sequence(0,n,m)