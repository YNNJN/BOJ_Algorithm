#백트래킹을 이용해 비어있는 리스트에서 시작해 수를 하나씩 추가하면서 길이가 m인 수열을 만들면 해당 수열을 출력
#1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
#이 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램

def sequence(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i],end=' ')
        print()
        return

    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        result[index] = i
        visited[i] = 1
        sequence(index+1, n,m)
        visited[i] = 0 #다음 수로 넘어가기 전에 초기화

n,m = map(int, input().split())
visited = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]
sequence(0,n,m)