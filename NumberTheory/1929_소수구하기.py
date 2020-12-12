def is_prime(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return number

n,m = map(int, input().split())
l = []
for i in range(n,m+1):
    if is_prime(i):
        l.append(i)
for el in l:
    print(el)
