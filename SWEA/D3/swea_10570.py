# 10570. 제곱 펠린드롬 수

import sys

sys.stdin = open('swea_10570.txt')


def is_pallindrome(num):
    str_num = str(num)
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[-1 - i]:
            return False
    return True


for tc in range(1, 1 + int(input())):
    A, B = map(int, input().split())
    cnt = 0
    for n in range(A, B + 1):
        if n ** 0.5 == int(n ** 0.5):
            if is_pallindrome(n) and is_pallindrome(int(n ** 0.5)):
                cnt += 1

    print('#{} {}'.format(tc, cnt))
