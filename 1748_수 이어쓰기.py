import sys
r = sys.stdin.readline

# #메모리 115444kb, 시간 4740ms
# n = int(input())
# def solution(n):
#     return sum(map(lambda x: len(str(x)), range(1, n+1)))
# print(solution(n))


#메모리 114788kb, 시간 128ms
def solution(n):
    l,ret = len(str(n)), 0
    for i in range(1, l): ret += i * (10**i - 10**(i-1))
    ret += l * (n - 10**(l-1) + 1)
    return ret
n = int(input())
print(solution(n))