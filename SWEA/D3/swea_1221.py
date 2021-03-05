# 1221. GNS

import sys

sys.stdin = open('GNS_test_input.txt')

alpha_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]


def counting_sort(num_list):
    result = [0 for _ in range(10)]

    for i in range(len(num_list)):
        idx = 0
        for j in alpha_num:
            if num_list[i] == alpha_num[idx]:
                result[idx] += 1
                idx += 1
                break
            else:
                idx += 1
    return result


T = int(input())

for t in range(1, 1 + T):
    tc, n = input().split()
    nums = list(input().split())

    res = counting_sort(nums)

    print('{}'.format(tc))
    for c in range(len(res)):
        print('{}'.format((alpha_num[c] + ' ') * res[c]))
