# 1953. [모의 SW 역량테스트] 탈주범 검거

import sys

sys.stdin = open('swea_1953.txt')

# 터널 별로 이동할 수 있는 방향
move = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),  # 상하좌우
    2: ((1, 0), (-1, 0)),  # 상, 하
    3: ((0, 1), (0, -1)),  # 좌, 우
    4: ((-1, 0), (0, 1)),  # 상, 우
    5: ((1, 0), (0, 1)),  # 하, 우
    6: ((1, 0), (0, -1)),  # 하, 좌
    7: ((-1, 0), (0, -1))  # 상, 좌
}

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    # N : 가로, M : 세로
    # 맨홀뚜껑 (R,C), L: 탈출에 소요된 시간
    queue = [(R, C)]
    visited = [[0] * M for _ in range(N)]
    # 시작점 방문 1
    visited[R][C] = 1
    # BFS
    while queue:
        if L == 1:
            break
        x, y = queue.pop(0)
        for dx, dy in move[tunnel[x][y]]:
            nx = x + dx
            ny = y + dy
            # 시간 다 썼으면 이전으로 돌아가서 다른방향 검사
            if not 0 <= nx < N or not 0 <= ny < M:
                continue

            # 연결되어있는지 확인
            if (-dx, -dy) in move[tunnel[nx][ny]]:
                if not visited[nx][ny] and tunnel[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] == L:
                        continue
                    # 시간 남았으면 queue에 저장해서 BFS 계속
                    queue.append((nx, ny))

    # visited 칠해진 수가 방문한 장소 수
    res = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                res += 1

    print('#{} {}'.format(tc, res))
