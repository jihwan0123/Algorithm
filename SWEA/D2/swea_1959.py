# 1959. 두 개의 숫자열

import sys

sys.stdin = open('num_string.txt')

T = int(input())

for tc in range(1, 1 + T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_val = 0
    k = 0
    result = []
    if m < n:
        m, n = n, m
        a, b = b, a

    for i in range(m - n + 1):
        mul = 0
        for j in range(i, i + n):
            mul += a[k] * b[j]
            k += 1
            if k == n:
                k = 0

        if mul > max_val:
            max_val = mul

    print("#{} {}".format(tc, max_val))
