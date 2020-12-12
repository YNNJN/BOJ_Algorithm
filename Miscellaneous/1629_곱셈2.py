#조건문 + n진수 변환 방법
#분할정복법과 실행 시간, 메모리는 동일
import sys
r = sys.stdin.readline

def pow_custom(a,b,mod):
    ret = 1
    while b:
        if b % 2 == 1: ret = ret * a % mod
        a = a * a % mod
        b //= 2
    return ret

a, b, c = list(map(int, sys.stdin.readline().split()))
print(pow_custom(a, b, c))