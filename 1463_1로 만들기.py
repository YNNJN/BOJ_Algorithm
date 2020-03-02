#1로 만들기
'''
D[N] = N->1로 만드는 데 필요한 연산의 최소값
N+1 ->
1. D[N/3]
2. D[N/2]
3. D[N-1]
-> 0
따라서 D[N+1] = min(1, 2, 3)
'''

N = int(input())
min_cnt = [0 for _ in range(N+1)]

idx = 0
while True:
    if idx > N:
        break
    if idx <= 1:
        min_cnt[idx] = 0
    else:
        temp_min = N+1
        if idx % 3 == 0:
            temp_idx = idx//3
            temp_min = min(temp_min, min_cnt[temp_idx])
        if idx % 2 == 0:
            temp_idx = idx//2
            temp_min = min(temp_min, min_cnt[temp_idx])
        temp_min = min(temp_min, min_cnt[idx-1])
        min_cnt[idx] = temp_min + 1
    idx += 1
print(min_cnt[N])