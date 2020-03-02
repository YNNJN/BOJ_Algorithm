# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if numbers[i] < numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#     return numbers
#
# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# print('\n'.join(map(str, bubble_sort(numbers))))
#
#
#
# n = int(input())
# numbers = [int(input()) for i in range(n)]
# print('\n'.join(map(str, sorted(numbers))))


def counting_sort(numbers):
    cnt = [0] * (max(numbers)+1)
    for i in numbers:
        cnt[i] += 1
    ndx = 0
    for i in range(len(cnt)):
        while 0 < cnt[i]:
            numbers[ndx] = i
            ndx += 1
            cnt[i] -= 1
    return numbers

n = int(input())
numbers = [int(input()) for i in range(n)]
print('\n'.join(map(str, counting_sort(numbers))))
