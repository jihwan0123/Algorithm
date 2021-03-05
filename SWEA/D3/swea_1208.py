# 1208. Flatten

import sys

sys.stdin = open('flatten.txt')

for tc in range(1, 11):
    dump = int(input())
    nums = list(map(int, input().split()))
    result = [0] * 100
    max_val, min_val = 0, 0

    for i in range(len(nums)):
        a = nums[i]
        result[a - 1] += 1

    for j in range(dump):
        # dump번 만큼 반복
        for k in range(len(nums) - 1):
            if result[-1 - k]:
                result[-1 - k] -= 1
                result[-1 - k - 1] += 1
                for d in range(len(nums) - 1):
                    if result[d]:
                        result[d] -= 1
                        result[d + 1] += 1
                        break
                break

    for a in range(len(result) - 1, -1, -1):
        if result[a]:
            max_val = a
            break

    for b in range(len(result) - 1):
        if result[b]:
            min_val = b
            break

    data = max_val - min_val
    print('#{} {}'.format(tc, data))
