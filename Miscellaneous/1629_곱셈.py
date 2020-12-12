# #이것도 시간초과라니
# import sys
# def mul(a, b):
#     if b % 2 == 0:
#         new_b = b//2
#         return (a**new_b) ** 2
#     else:
#         new_b = (b - 1)//2
#         return a * (a**new_b) ** 2
#
# a, b, c = list(map(int, sys.stdin.readline().split()))
# print(mul(a, b) % c)

#b가 짝수일 때까지 쪼갬
import sys
def div(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2:
        return div(a, b-1)*a
    else:
        ans = div(a,b//2)
        ans %= c
        return ans**2 % c
a, b, c = list(map(int, sys.stdin.readline().split()))
print(div(a,b) % c)