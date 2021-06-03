# 10202. 문자열 동화

import sys

sys.stdin = open('swea_10202.txt')

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    a = input()  # 길이가 n인 문자열 a,b,c
    b = input()
    c = input()

    counter = 0
    # n번째 자리까지 비교하면서
    for i in range(n):
        # 같으면 교환 x
        if a[i] == b[i] == c[i]:
            continue
        # 다른게 있으면
        else:
            # set으로 체크해서 중복 제거
            same = {a[i], b[i], c[i]}
            # 같은게 생겼다면 len = 2가 되므로 1개만 바꾸면 됨
            if len(same) == 2:
                counter += 1
            # 아니면 2자리 다 바꾸기
            else:
                counter += 2
                
    print('#{} {}'.format(tc, counter))
