'''
총 수입이 총 비용보다 많아지게 되는 지점 구하기

'''

# 총 수입: c * x
# 총 비용: a + b * x

a,b,c = map(int, input().split())
x = -1

if b >= c: print(x)
else:
    print(int(a//(c-b))+1)