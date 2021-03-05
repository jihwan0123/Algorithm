# 1225. 암호생성기

import sys

sys.stdin = open('swea_1225.txt')


def makePassword(nums):
    queue = list(nums)
    level = 0
    while True:
        level += 1
        a = queue.pop(0)
        if a - level <= 0:
            queue.append(0)
            return queue
        queue.append(a - level)
        if level >= 5:
            level = 0
    return


for tc in range(1, 11):
    n = int(input())
    password = list(map(int, input().split()))
    result = makePassword(password)
    print('#%d' % tc, *result)
