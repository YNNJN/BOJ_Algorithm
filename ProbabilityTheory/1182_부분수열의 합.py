# #이터툴로 모든 조합을 구한 뒤 조건에 맞는 경우의 수를 셈
# from itertools import combinations as cb
# import sys
# r = sys.stdin.readline
#
# n,s = map(int, r().split())
# arr = list(map(int, r().split()))
# cnt = 0
#
# for i in range(1, n+1):
#     for combination in cb(arr, i):
#         if sum(combination) == s:
#             cnt += 1
# print(cnt)

import sys
r = sys.stdin.readline

def combination(arr, comb, s):
    cnt = 0
    for front in arr:
        for end in list(comb): #깊은 복사
            comb.append(front+end)
            # print(comb)
            if comb[-1] == s:
                cnt += 1
    return cnt

n,s = map(int, r().split())
arr = list(map(int, r().split()))
comb = [0]
cnt = combination(arr, comb, s)
print(cnt)