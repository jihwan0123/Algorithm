# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

import sys

sys.stdin = open('swea_5250.txt')

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

'''
def dfs(x, y, s):
    global minV
    if s >= minV:
        return
    if x == N - 1 and y == N - 1:
        minV = min(minV, s)
        return

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if data[nx][ny] > data[x][y]:
                dfs(nx, ny, s + 1 + data[nx][ny])
            else:
                dfs(nx, ny, s + 1)


for tc in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    minV = float('inf')
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, minV))
    
'''

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dijkstra():
    D = [[float('inf')] * N for _ in range(N)]
    D[0][0] = 0
    queue = [(0, 0)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if data[nx][ny] > data[x][y]:
                    h = data[nx][ny] - data[x][y]
                else:
                    h = 0
                nD = D[x][y] + h + 1
                # 최솟값 교체한 경우만 추가
                if D[nx][ny] > nD:
                    D[nx][ny] = nD
                    queue.append((nx, ny))

    return D[N - 1][N - 1]


for tc in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, dijkstra()))
