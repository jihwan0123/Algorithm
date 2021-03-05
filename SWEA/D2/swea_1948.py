# 1948. 날짜 계산기

import sys

sys.stdin = open('swea_1948.txt')

T = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, 1 + T):
    nums = list(map(int, input().split()))
    result = 0
    # nums[0], nums[2] : month
    # nums[1], nums[3] : day

    month = nums[2] - nums[0]

    if month == 0:
        result = nums[3] - nums[1] + 1

    else:
        for i in range(nums[0], nums[2]):
            result += days[i - 1]
        result += nums[3] - nums[1] + 1

    print('#{} {}'.format(tc, result))
