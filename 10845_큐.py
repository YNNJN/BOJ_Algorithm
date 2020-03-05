import sys
r = sys.stdin.readline

def push(n):
    q.append(n)

def pop():
    if not q:
        print(-1)
    else:
        print(q[0])
        del(q[0])

def size():
    print(len(q))

def empty():
    if not q:
        print(1)
    else:
        print(0)

def front():
    if not q:
        print(-1)
    else:
        print(q[0])

def back():
    if not q:
        print(-1)
    else:
        print(q[-1])

n = int(r())
q = []

for _ in range(n):
    cmd = list(r().split())

    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()
