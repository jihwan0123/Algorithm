# 2580. 스도쿠
import sys
input = sys.stdin.readline


def check(x, y, value):  # (x,y)에 value를 넣을 수 있는지 체크
    for i in range(9):  # 가로, 세로 검사
        if (boards[x][i] == value) or (boards[i][y] == value):
            return False

    m, n = 3*(x//3), 3*(y//3)
    for j in range(m, m+3):  # 3*3 검사
        for k in range(n, n+3):
            if boards[j][k] == value:
                return False
    return True


def dfs(cnt):
    if cnt == len(blanks):  # 0을 모두 채울 수 있으면 출력하고 dfs종료
        for board in boards:
            print(' '.join(map(str, board)))
        return True

    # cnt번째 빈칸의 좌표 (x,y)
    x = blanks[cnt][0]
    y = blanks[cnt][1]
    for v in range(1, 10):  # (x,y)에 1 ~ 9까지 넣어본다.
        if check(x, y, v):  # 넣을 수 있으면
            boards[x][y] = v  # 넣고
            if dfs(cnt+1): return True  # 0을 모두 채웠으면 dfs 완전 종료
            boards[x][y] = 0  # 0을 모두 채울 수 없으면 백트래킹


boards = [list(map(int, input().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if boards[i][j] == 0] # 0인 빈칸의 좌표들 집합

dfs(0)
