# 4615. 재미있는 오셀로게임

import sys

sys.stdin = open('swea_4615.txt')

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    # N : 한변의 길이, M : 돌을 놓는 횟수
    # 1이면 흑, 2면 백돌
    stones = [tuple(map(int, input().split())) for _ in range(M)]

    area = [[0] * N for _ in range(N)]
    r = N // 2
    c = N // 2
    area[c][r] = 2
    area[c - 1][r - 1] = 2
    area[c - 1][r] = 1
    area[c][r - 1] = 1

    for i in stones:
        r = i[0] - 1
        c = i[1] - 1
        color = i[2]
        area[c][r] = color
        for dr, dc in dxy:
            r = i[0] - 1
            c = i[1] - 1
            # 8방향 탐색
            cnt = 0
            a = 0
            while 0 <= c < N and 0 <= r < N:
                if area[c][r] == color:
                    # 같은 색을 만나면 cnt += 1
                    cnt += 1
                    a += 1
                elif area[c][r] == 0:
                    # 빈칸을 만나면 종료
                    break
                else:
                    a += 1

                if cnt == 2:
                    # 자기자신 + 같은돌 : cnt = 2 가 되면
                    while a > 1:
                        # a 처음값이 1 이었으므로 1될떄까지
                        r -= dr
                        c -= dc
                        a -= 1
                        area[c][r] = color
                        # 탐색했던거 돌아가면서 돌 뒤집기
                        if area[c][r] == color:
                            cnt -= 1
                    break

                c += dc
                r += dr

    white = 0
    black = 0

    for i in area:
        white += i.count(2)
        black += i.count(1)

    print('#{} {} {}'.format(tc, black, white))
