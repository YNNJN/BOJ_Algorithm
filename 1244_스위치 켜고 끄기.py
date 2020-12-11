nn = int(input())
state = [0] + list(map(int, input().split()))
n = int(input())
for _ in range(n):
    sex, num = map(int, input().split())
    # 남학생
    if sex == 1:
        while num <= nn:
            state[num] = abs(state[num] - 1)
            result = state
            num *= 2
    # 여학생
    else:
        i = 0
        while True:
            if num - i < 0 or num + i > nn:
                continue
            if state[num - i] == state[num + i]:
                i += 1
            else:
                idx = i - 1
                break
        temp = state[num - idx : num + idx + 1]
        for i in range(len(temp)):
            temp[i] = abs(temp[i] - 1)
        result = temp + state[num + idx + 1:]
print(result)