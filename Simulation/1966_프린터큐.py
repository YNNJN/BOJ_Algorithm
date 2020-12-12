tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split()) # 문서 개수, 인쇄 순서가 궁금한 문서
    priority = list(map(int, input().split()))
    result = list(range(n))
    result[m] = 'target'

    idx = 0

    while True:
        if priority[0] == max(priority):
            idx += 1

            if result[0] == 'target':
                print(idx)
                break
            else:
                priority.pop(0)
                result.pop(0)
        else:
            priority.append(priority.pop(0))
            result.append(result.pop(0))