# #배열이 주어졌을 때 최대의 점수를 갖는 부분배열을 골라내는 프로그램 작성
# #네 당연히 시간 초과
# import sys
# r = sys.stdin.readline
# n = int(r())
# arr = list(map(int, r().split()))
# max_value = 0
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         ans = sum(arr[i:j+1]) * min(arr[i:j+1])
#         if max_value < ans:
#             max_value = ans
# print(max_value)


import sys
r = sys.stdin.readline

def find(s,e):
    if s == e:
        return arr[s]*arr[e]
    mid = (s+e)//2
    ans = max(find(s, mid), find(mid+1, e))

    left, right = mid, mid +1
    sum = arr[left] + arr[right]
    min_value = min(arr[left], arr[right])
    ans = max(ans, min_value * sum)

    while left > s or right < e:
        if right < e and (left == s or arr[left-1] < arr[right+1]):
            right += 1
            sum += arr[right]
            min_value = min(min_value, arr[right])
        else:
            left -= 1
            sum += arr[left]
            min_value = min(min_value, arr[left])
        ans = max(ans, min_value * sum)
    return ans

n = int(r())
arr = list(map(int, r().split()))
print(find(0, len(arr)-1))
