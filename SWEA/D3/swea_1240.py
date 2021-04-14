# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

import sys

sys.stdin = open('swea_1240.txt')

password = {
    '0001101': 1,
    '0011001': 2,
    '0010011': 3,
    '0111101': 4,
    '0100011': 5,
    '0110001': 6,
    '0101111': 7,
    '0111011': 8,
    '0110111': 9,
    '0001011': 10
}

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    for i in code:
        if '1' in i:
            x = i.strip('0').zfill(56)
            break
    j = 0
    res = []
    # 암호 7자리씩 0~9 값으로 바꾸기
    while j < len(x):
        if password.get(x[j:j + 7]):
            res.append(password.get(x[j:j + 7]) - 1)
        j += 7

    sum_code = 0
    for k in range(0, len(res), 2):
        sum_code += res[k] * 3
        sum_code += res[k + 1]

    if sum_code % 10 == 0:
        print('#%d %d' % (tc, sum(res)))
    else:
        print('#%d 0' % tc)
