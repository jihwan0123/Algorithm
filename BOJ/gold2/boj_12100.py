# 12100. 2048(Easy)

from itertools import product
import copy
import sys
input = sys.stdin.readline


def move_block(direction, boards):  # 블록 이동
    if direction == 0:  # 오른쪽 방향으로 가면 (n-1, i) 부터 시작
        for a in range(n):
            temp = []
            for b in range(n-1, -1, -1):
                if boards[a][b] == 0:
                    continue
                temp.append((boards[a][b], True))
                boards[a][b] = 0
                if len(temp) >= 2 and (temp[-1] == temp[-2]) and temp[-1][1]:
                    temp.pop()
                    tmp = temp.pop()
                    temp.append((tmp[0]*2, False))

            for c in range(len(temp)):
                boards[a][n-1-c] = temp[c][0]

    elif direction == 1:  # 아래로 가면 (i, n-1) 부터 시작
        for a in range(n):
            temp = []
            for b in range(n-1, -1, -1):
                if boards[b][a] == 0:
                    continue
                temp.append((boards[b][a], True))
                boards[b][a] = 0
                if len(temp) >= 2 and (temp[-1] == temp[-2]) and temp[-1][1]:
                    temp.pop()
                    tmp = temp.pop()
                    temp.append((tmp[0]*2, False))

            for c in range(len(temp)):
                boards[n-1-c][a] = temp[c][0]

    elif direction == 2:  # 왼쪽으로 가면 (0, i) 부터
        for a in range(n):
            temp = []
            for b in range(n):
                if boards[a][b] == 0:
                    continue
                temp.append((boards[a][b], True))
                boards[a][b] = 0
                if len(temp) >= 2 and (temp[-1] == temp[-2]) and temp[-1][1]:
                    temp.pop()
                    tmp = temp.pop()
                    temp.append((tmp[0]*2, False))

            for c in range(len(temp)):
                boards[a][c] = temp[c][0]

    elif direction == 3:  # 위로 가면 (i, 0) 부터
        for a in range(n):
            temp = []
            for b in range(n):
                if boards[b][a] == 0:
                    continue
                temp.append((boards[b][a], True))
                boards[b][a] = 0
                if len(temp) >= 2 and (temp[-1] == temp[-2]) and temp[-1][1]:
                    temp.pop()
                    tmp = temp.pop()
                    temp.append((tmp[0]*2, False))

            for c in range(len(temp)):
                boards[c][a] = temp[c][0]

    return boards


dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 오른, 아래, 왼, 위
n = int(input())
blocks = [list(map(int, input().split())) for _ in range(n)]
maxV = 0
nums = list(range(4))
products = list(product(nums, repeat=5))
for p in products:
    blocks_copy = copy.deepcopy(blocks)
    for i in range(5):
        move_block(p[i], blocks_copy)

    for b in blocks_copy:
        maxV = max(maxV, max(b))

print(maxV)