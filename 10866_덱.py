import sys
r = sys.stdin.readline

def push_front(n):
    d.insert(0, n)
def push_back(n):
    d.append(n)
def pop_front():
    if not d:
        print(-1)
    else:
        print(d[0])
        del(d[0])
def pop_back():
    if not d:
        print(-1)
    else:
        print(d[-1])
        del(d[-1])

def size():
    print(len(d))

def empty():
    if not d:
        print(1)
    else:
        print(0)

def front():
    if not d:
        print(-1)
    else:
        print(d[0])

def back():
    if not d:
        print(-1)
    else:
        print(d[-1])

n = int(r())
d = []

for _ in range(n):
    cmd = list(r().split())

    if cmd[0] == 'push_front':
        push_front(cmd[1])
    elif cmd[0] == 'push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()
