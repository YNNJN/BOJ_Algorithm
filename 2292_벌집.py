'''
궤도 최소거리

'''

n = int(input())
orbit = 1
while n > 1:
    n -= (6 * orbit)
    orbit += 1
print(orbit)