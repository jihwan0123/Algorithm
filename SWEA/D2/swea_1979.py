# 1979. 어디에 단어가 들어갈 수 있을까

import sys

sys.stdin = open('input.txt')


def count_location(puz, n):
    total = 0

    for i in range(len(puz)):
        cnt = 0
        for j in range(len(puz)):
            if int(puz[i][j]) == 1:
                cnt += 1
                if j == len(puz) - 1 and cnt == n:
                    total += 1
            else:
                if cnt == n:
                    total += 1
                cnt = 0

    for r in range(len(puz)):
        cnt = 0
        for c in range(len(puz)):
            if int(puz[c][r]) == 1:
                cnt += 1
                if c == len(puz) - 1 and cnt == n:
                    total += 1
            else:
                if cnt == n:
                    total += 1
                cnt = 0

    return total


T = int(input())

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    # N : 가로, 세로 길이, M : 단어의 길이
    puzzle = [input().split() for _ in range(N)]

    result = count_location(puzzle, K)

    print('#{} {}'.format(tc, result))
