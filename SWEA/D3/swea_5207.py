# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

import sys

sys.stdin = open('swea_5207.txt')

'''
def binary_search(left, right, x):
    global cnt, check

    m = (left + right) // 2
    mid = A[m]
    if mid == x:
        cnt += 1
        return
    elif left >= right:
        return
    elif mid > x:
        if check == 1:
            return
        check = 1
        binary_search(left, m - 1, x)
    else:
        if check == 2:
            return
        check = 2
        binary_search(m + 1, right, x)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        check = 0
        if A[0] <= num <= A[-1]:
            binary_search(0, N - 1, num)

    print('#%d %d' % (tc, cnt))
'''


def binary_search(left, right, x):
    global cnt, check

    while left <= right:
        m = (left + right) // 2
        if A[m] == x:
            cnt += 1
            return
        elif A[m] < x:
            if check == 1:
                return
            check = 1
            left = m + 1
        else:
            if check == -1:
                return
            check = -1
            right = m - 1
    return


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for num in B:
        check = 0
        binary_search(0, N - 1, num)

    print('#%d %d' % (tc, cnt))
