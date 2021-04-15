# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

import sys

sys.stdin = open('swea_5189.txt')

'''
def perm(idx):
    global res
    if idx == N - 1:
        ans = data[nums[-1]][nums[0]]
        for i in range(N - 1):
            ans += data[nums[i]][nums[i + 1]]
        res = min(res, ans)
        return

    else:
        for i in range(idx, N - 1):
            nums[idx], nums[i] = nums[i], nums[idx]
            perm(idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]


for tc in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))
    res = 987654321
    perm(0)
    print('#%d %d' % (tc, res))
'''


def perm(idx, total):
    global res
    if idx == N:
        res = total
        return

    else:
        for i in range(idx, N - 1):
            nums[idx], nums[i] = nums[i], nums[idx]
            perm(idx + 1, total + data[nums[i]][[nums[idx]]])
            nums[idx], nums[i] = nums[i], nums[idx]


for tc in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(N))
    res = 0
    perm(0, res)
    print('#%d %d' % (tc, res))
