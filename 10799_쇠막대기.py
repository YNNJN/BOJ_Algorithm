import sys
r = sys.stdin.readline

data = list(r().strip())
s = []
ans = 0

for i in range(len(data)):
    if data[i] == '(':
        s.append('(')
    else:
        if data[i-1] == '(':
            s.pop()
            ans += len(s) #()일 경우 스택에 들어있는 ( 수만큼 답에 더해줌
        else:
            s.pop()
            ans += 1
print(ans)
