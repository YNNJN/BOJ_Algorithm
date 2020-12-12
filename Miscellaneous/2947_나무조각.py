numbers = list(map(int, input().split()))
while numbers != [1, 2, 3, 4, 5]:
    for i in range(5):
        if i+1 < 5:
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                print(' '.join(map(str, numbers)))
