# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

import sys

sys.stdin = open('swea_5203.txt')

run_triplet = {
    '000': 1, '111': 1, '222': 1, '333': 1, '444': 1, '555': 1, '666': 1, '777': 1, '888': 1, '999': 1,
    '012': 1, '123': 1, '234': 1, '345': 1, '456': 1, '567': 1, '678': 1, '789': 1
}


def perm(idx, nums):
    global ans
    if ans:
        return

    if idx == N:
        x = ''.join(map(str, nums))
        if run_triplet.get(x[:3], 0):
            ans = 1
            return

    else:
        for i in range(idx, N):
            nums[idx], nums[i] = nums[i], nums[idx]
            perm(idx + 1, nums)
            nums[idx], nums[i] = nums[i], nums[idx]


for tc in range(1, 1 + int(input())):
    cards = list(map(int, input().split()))
    a = []
    b = []
    res = 0
    N = 0
    while cards:
        N += 1
        if N < 3:
            a.append(cards.pop(0))
            b.append(cards.pop(0))

        else:
            a.append(cards.pop(0))
            ans = 0
            perm(0, a)
            if ans:
                res = 1
                break

            b.append(cards.pop(0))
            ans = 0
            perm(0, b)
            if ans:
                res = 2
                break

    print('#%d %d' % (tc, res))
