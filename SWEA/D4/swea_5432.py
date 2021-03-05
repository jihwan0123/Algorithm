# 5432. 쇠막대기 자르기

import sys

sys.stdin = open('swea_5432.txt')

T = int(input())

for tc in range(1, 1 + T):
    laser = input().replace('()', '*').strip('*')
    # '()'를 *로 대체하고 양쪽 끝에 있는건 필요없으므로 제거

    cnt, total = 0, 0
    # cnt: 이어지고있는 쇠막대기 갯수
    # total: 쇠막대기 자른 총 갯수
    for i in laser:
        # laser 반복 tc1: (((**)(*)*))(*)
        if i == '(':
            # '(' 면 막대기 생성
            cnt += 1

        elif i == '*':
            # laser 만나면 막대기만큼 왼쪽에 잘림
            total += cnt

        elif i == ')':
            # ')' 만나면 자르고 남은 오른쪽 부분이므로 total + 1 해주고 막대기 갯수 cnt  - 1
            total += 1
            cnt -= 1

    print('#{} {}'.format(tc, total))
