import sys
r = sys.stdin.readline

def push(n):
    s.append(n)
def pop():
    if not s:
        print(-1)
    else:
        print(s[-1])
        del(s[-1])
def size():
    print(len(s))
def empty():
    if not s:
        print(1)
    else:
        print(0)
def top():
    if not s:
        print(-1)
    else:
        print(s[-1])

n = int(r())
s = []

for i in range(n):
    cmd = list(r().split())

    if cmd[0] == 'push':
        push(cmd[1])
    elif cmd[0] == 'pop':
        pop()
    elif cmd[0] == 'size':
        size()
    elif cmd[0] == 'empty':
        empty()
    elif cmd[0] == 'top':
        top()


