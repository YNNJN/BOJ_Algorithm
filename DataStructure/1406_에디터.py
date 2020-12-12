#커서의 명령어 l, d, b, p, 명령어 수행 전 커서는 문장의 맨 뒤에 위치함
#왼쪽 스택/오른쪽 스택 나눠서 풀이
#모든 명령어 수행 후 입력된 문자열 구하는 프로그램 작성

import sys
r = sys.stdin.readline

ls = list(r()[:-1])
rs = list()

for _ in range(int(r())):
    cmd = r()
    if cmd[0] == 'L' and ls:
        rs.append(ls.pop())
    elif cmd[0] == 'D' and rs:
        ls.append(rs.pop())
    elif cmd[0] == 'B' and ls:
        ls.pop()
    elif cmd[0] == 'P':
        ls.append(cmd[2])
print(''.join(ls+rs[::-1]))