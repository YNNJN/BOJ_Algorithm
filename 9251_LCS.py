#같다면 왼쪽 대각선 숫자에 +1한 값, 같지 않다면 왼쪽과 위를 비교해 큰 값 대입
m = list(input())
n = list(input())
d = [[0]*(len(n)+1) for i in range(len(m)+1)]
for i in range(len(m)):
    for j in range(len(n)):
        if m[i] == n[j]:
            d[i+1][j+1] = d[i][j] + 1
        else:
            d[i+1][j+1] = max(d[i][j+1], d[i+1][j])
print(d[len(m)][len(n)])