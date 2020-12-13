'''

'''

x = int(input())

orbit = 1
while x > orbit:
    x -= orbit
    orbit += 1
if orbit % 2 == 0:
    a = x
    b = orbit - x + 1
else:
    a = orbit - x + 1
    b = x
print('{}/{}'.format(a,b))