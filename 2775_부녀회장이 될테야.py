'''
파스칼의 삼각형 리스트 만들고
n번째 수 출력

'''

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            arr[j] += arr[j-1]
    print(arr[n-1])