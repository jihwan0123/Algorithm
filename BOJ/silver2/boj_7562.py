# 7562. 나이트의 이동


import sys

sys.stdin = open('boj_7562.txt')

# 나이트가 이동할수 있는 8가지 방향
dxy = [[1, 2], [2, 1], [-1, 2], [2, -1], [-2, 1], [1, -2], [-1, -2], [-2, -1]]


# BFS 이용
def bfs_knight(start, end):
    queue = [start]
    if start == end:
        return 0

    while queue:
        row, col = queue.pop(0)
        level = visited[row][col]
        for dx, dy in dxy:
            r = row + dx
            c = col + dy
            if (r, c) == end:
                return level
            if r < 0 or r >= n or c < 0 or c >= n:
                continue
            elif visited[r][c] == 0:
                visited[r][c] = level + 1
                queue.append((r, c))


T = int(sys.stdin.readline())

for tc in range(T):
    n = int(sys.stdin.readline())
    x1, y1 = map(int, sys.stdin.readline().strip().split())
    x2, y2 = map(int, sys.stdin.readline().strip().split())

    knight = (x1, y1)
    pawn = (x2, y2)
    visited = [[0] * n for _ in range(n)]
    visited[x1][y1] = 1
    print(bfs_knight(knight, pawn))
