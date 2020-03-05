import sys
r = sys.stdin.readline

# #스택 이용
def find(data):
    s = []
    for b in data:
        if len(s) == 0 and b == ')':
            return 'NO'
        if b == '(':
            s.append(b)
        else:
            if s[-1] == '(':
                s.pop()
            else:
                return 'NO'
    if len(s) == 0:
        return 'YES'
    return 'NO'

for tc in range(int(r())):
    data = r().strip()
    print(find(data))



# #sum을 이용한 다른 사람 풀이
# for tc in range(int(r())):
#     data = r().strip()
#     s = list(data)
#     sum = 0
#
#     for i in s:
#         if i == '(':
#             sum += 1
#         elif i == ')':
#             sum -= 1
#         if sum < 0:
#             print('NO')
#             break
#     if sum > 0:
#         print('NO')
#     elif sum == 0:
#         print('YES')
