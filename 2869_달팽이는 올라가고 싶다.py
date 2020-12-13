'''
시간초과 코드 개선하기

'''

a,b,v = map(int, input().split())
day = (v-b)/(a-b)
if day != int(day):
    day = int(day) + 1
print(int(day))