#원에서 사람들이 제거되는 순서를 (N,K)-요세푸스 순열이라고 함
import sys
r = sys.stdin.readline

n,k = map(int, r().split())
q = list(range(1, n+1))
l = []
i = k-1

while True:
    l.append(q.pop(i))
    if not q:
        break
    i = (i+k-1) % len(q)
print('<' + ', '.join(map(str, l)) + '>')
