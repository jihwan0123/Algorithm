# 1954. 달팽이숫자

import sys

sys.stdin = open('swea_1954_달팽이숫자.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 우 하 좌 상 순서

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    result = [[0] * n for _ in range(n)]
    row = 0
    col = 0
    num = 1
    distance = n - 1
    if distance <= 0:
        distance = 1
    escape = False

    while True:
        for i in range(4):  # 4방향으로 한바퀴
            for j in range(distance):  # 거리만큼 이동
                result[row][col] = num
                num += 1
                if num > n ** 2:
                    escape = True
                    break
                dr, dc = dxy[i]
                row += dr
                col += dc
            if escape:
                break
        if escape:
            break

        # 한바퀴 돌고 다음 시작지점 설정 (+1, +1)
        row += 1
        col += 1
        # 거리 -2
        # n=4 3333 1111
        # n=5 4444 2222 1
        # n=6, 5555 3333 1111
        distance -= 2
        if distance <= 0:
            distance = 1

    print('#%d' % tc)
    for r in range(n):
        for c in range(n):
            print(result[r][c], end=' ')
        print()
