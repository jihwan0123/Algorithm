# 1699. 제곱수의 합

import sys
input = sys.stdin.readline


def chk(n):  # four-squares
    temp = int(n**0.5)
    # 제곱인 경우 체크 (1인 경우)
    for i in range(temp, 0, -1):
        if i**2 == n:
            return 1

    # 제곱인거 빼고 제곱수로 되는지 체크 (2인 경우)
    for i in range(temp, 0, -1):
        n2 = n - i**2
        if n2 == int(n2**0.5) ** 2:
            return 2

    # 3인경우 체크
    for i in range(1, 224):
        for j in range(i, 224):
            # 제곱수 2개 뺀값
            n3 = n - i**2 - j**2
            if n3 < 0:
                break
            if n3 == int(n3**0.5) ** 2:
                return 3
    return 4


print(chk(int(input())))
