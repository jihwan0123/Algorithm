# 11315. 오목판정

import sys

sys.stdin = open('swea_11315.txt')

# def is_omok(stone, n):
#     # 가로 검사
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if stone[i][j] == 'o':
#                 cnt += 1
#                 if cnt >= 5:
#                     return True
#             else:
#                 cnt = 0
#     # 세로 검사
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if stone[j][i] == 'o':
#                 cnt += 1
#                 if cnt >= 5:
#                     return True
#             else:
#                 cnt = 0
#
#     # 대각 x + 1, y + 1
#     for c in range(n):
#         r = 0
#         cnt = 0
#         while r < n and c < n:
#             if stone[c][r] == 'o':
#                 cnt += 1
#                 c += 1
#                 r += 1
#                 if cnt >= 5:
#                     return True
#             else:
#                 cnt = 0
#                 c += 1
#                 r += 1
#
#     for r in range(n - 1, -1, -1):
#         c = 0
#         cnt = 0
#         while r < n and c < n:
#             if stone[c][r] == 'o':
#                 cnt += 1
#                 c += 1
#                 r += 1
#                 if cnt >= 5:
#                     return True
#             else:
#                 cnt = 0
#                 c += 1
#                 r += 1
#
#     #  대각 x - 1, y + 1
#     for c in range(n):
#         cnt = 0
#         r = n - 1
#         while r >= 0 and c < n:
#             if stone[c][r] == 'o':
#                 cnt += 1
#                 c += 1
#                 r -= 1
#                 if cnt >= 5:
#                     return True
#             else:
#                 cnt = 0
#                 c += 1
#                 r -= 1
#
#     for r in range(n - 1, -1, -1):
#         cnt = 0
#         c = 0
#         while r >= 0 and c < n:
#             if stone[c][r] == 'o':
#                 cnt += 1
#                 c += 1
#                 r -= 1
#                 if cnt >= 5:
#                     return True
#             else:
#                 cnt = 0
#                 c += 1
#                 r -= 1
#     return False


##### 델타이동으로 풀기 ####


# 오른쪽, 오른대각, 아래, 왼쪽대각
# c, r 기준으로 돌면서 확인
dxy = [[0, 1], [1, 1], [1, 0], [1, -1]]


def is_omok(stone, n):
    for r in range(n):
        for c in range(n):
            for dc, dr in dxy:
                cnt = 0
                row = r
                col = c
                while 0 <= row < n and 0 <= col < n and stone[col][row] == 'o':
                    cnt += 1
                    if cnt == 5:
                        return 'YES'
                    row += dr
                    col += dc

    return 'NO'


for tc in range(1, 1 + int(input())):
    N = int(input())
    stones = [input() for _ in range(N)]

    print('#{} {}'.format(tc, is_omok(stones, N)))
