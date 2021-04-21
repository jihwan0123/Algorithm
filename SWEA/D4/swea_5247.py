# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

import sys

sys.stdin = open('swea_5247.txt')

from collections import deque

calc = {0: (lambda a: a + 1),
        1: (lambda a: a - 1),
        2: (lambda a: a * 2),
        3: (lambda a: a - 10)
        }


def bfs(a, b):
    queue = deque()
    queue.append(a)
    # queue = [a]
    visited = [0] * 1000001
    visited[a] = 1
    while queue:
        x = queue.popleft()
        # x = queue.pop(0)
        for i in range(4):
            nx = calc[i](x)
            if nx == b:
                return visited[x]
            if 0 < nx <= 1000000 and not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x] + 1


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, bfs(N, M)))
