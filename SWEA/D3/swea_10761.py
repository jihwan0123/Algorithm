# 10761. 신뢰

import sys

sys.stdin = open('swea_10761.txt')

for tc in range(1, 1 + int(input())):
    command = input().split()
    n = int(command.pop(0))
    Blue = []
    Orange = []
    for i in range(n):
        # 입력 command가 B면
        if command[2 * i] == 'B':
            Blue.append(int(command[2 * i + 1]))

        else:
            Orange.append(int(command[2 * i + 1]))

    B_idx, O_idx, time = 0, 0, 0

    # Blue, Orange 둘 다 끝나면 반복종료
    while len(Blue) != 0 or len(Orange) != 0:
        # 파란색일 때,
        if command[0] == 'B':

            # 현재 위치와 목표 값의 크기를 비교해서 이동
            if int(command[1]) - 1 > B_idx:
                B_idx += 1

            elif int(command[1]) - 1 < B_idx:
                B_idx -= 1

            # 버튼 index에 도착하면, command, Blue 값 제거
            else:
                command.pop(0)
                command.pop(0)
                Blue.pop(0)

            # 오렌지 버튼 남아 있으면 오렌지도 이동
            if len(Orange) != 0:
                if O_idx > Orange[0] - 1:
                    O_idx -= 1

                elif O_idx < Orange[0] - 1:
                    O_idx += 1

        # 파란색일때
        else:
            if int(command[1]) - 1 > O_idx:
                O_idx += 1

            elif int(command[1]) - 1 < O_idx:
                O_idx -= 1

            else:
                command.pop(0)
                command.pop(0)
                Orange.pop(0)

            if len(Blue) != 0:
                if B_idx > Blue[0] - 1:
                    B_idx -= 1

                elif B_idx < Blue[0] - 1:
                    B_idx += 1

        time += 1

    print('#{} {}'.format(tc, time))
