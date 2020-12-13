'''
n킬로그램 배달
최대한 적은 봉지

'''
n = int(input())
a = n//3
b = n//5
def find(n):
    for y in range(b, -1, -1):
        for x in range(a, -1, -1):
            if x * 3 + y * 5 == n:
                return x+y
    return -1
print(find(n))