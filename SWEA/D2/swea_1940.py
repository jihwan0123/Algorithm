# swea_1940 가랏! RC카!

import sys

sys.stdin = open('swea_1940.txt')

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    # n : command의 수
    distance = 0
    a = 0
    speed = 0
    # v = v0 + at

    for i in range(n):
        # command 입력
        cmd = list(map(int, input().split()))

        # cmd[0] 이 0이면 이전 속도 유지
        if cmd[0] == 0:
            distance += speed

        elif cmd[0] == 1:
            a = cmd[1]
            # 가속도 최댓값 = 2
            speed += a
            distance += speed

        elif cmd[0] == 2:
            if speed < cmd[1]:
                speed = 0
            else:
                speed -= cmd[1]
            distance += speed

    print('#{} {}'.format(tc, distance))
