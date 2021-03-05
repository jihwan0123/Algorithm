# 1966. 숫자를 정렬하자

def bubble_sort(num):
    for i in range(len(num) - 1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]


T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    nums = list(map(int, input().split()))

    bubble_sort(nums)

    print("#%d" % tc, end=' ')
    print(*nums)
