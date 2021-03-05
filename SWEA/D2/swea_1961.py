# 1961. 숫자 배열 회전

import sys

sys.stdin = open('swea_1961.txt')


def rotate(input_l):
    result = []
    for i in range(len(input_l)):
        result.append([])
    for i in range(3):
        rotate_list = []
        idx = 0
        for j in zip(*input_l):
            rotate_list.append(list(reversed(j)))
            result[idx].append(''.join(list(reversed(j))))
            idx += 1
        input_l = rotate_list

    for k in result:
        print(' '.join(k))


T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    input_list = []

    for _ in range(n):
        input_list.append(list(map(str, input().split())))

    print('#%d' % tc)
    rotate(input_list)
