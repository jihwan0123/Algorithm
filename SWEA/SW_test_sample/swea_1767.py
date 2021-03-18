import sys

sys.stdin = open('swea_1767.txt')

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def find_core():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if processor[i][j] == 1:
                check = True
                for dx, dy in dxy:
                    if processor[i + dx][j + dy] == 2:
                        visited[i][j] = 1
                        check = False
                        break
                if check:
                    cores.append((i, j))


def dfs(idx, x, y, length, cor):
    global min_core
    global res
    if idx >= len(cores) - 1 or cor == len(cores):
        if r[cor] >= length:
            r[cor] = length

        return

    for dx, dy in dxy:
        while True:
            nx = cores[idx][0] + dx
            ny = cores[idx][1] + dy
            print(idx, nx, ny, length)

            # power 만났으면
            if processor[nx][ny] == 2:
                print(nx,ny)
                dfs(idx + 1, cores[idx + 1][0], cores[idx + 1][1], length, cor + 1)
                x = cores[idx][0]
                y = cores[idx][1]
                break

            else:
                # 이미 전선 있으면 다음 방향으로
                if processor[nx][ny] == 1 or visited[nx][ny] == 1:
                    # core 만날때까지 지금까지 왔던거 돌아가면서 방문제거
                    while cores[idx][0] == nx - dx and cores[idx][1] == ny - dy:
                        length -= 1
                        nx -= dx
                        ny -= dy

                        visited[nx + dx][ny + dy] = 0
                    x = cores[idx][0]
                    y = cores[idx][1]
                    length += 1
                    visited[x][y] = 1
                    break

                # 방문 안했으면
                elif processor[nx][ny] == 0 and visited[nx][ny] == 0:
                    # 방문표시 한 방향으로 계속
                    length += 1
                    visited[nx][ny] = 1
                    x = nx
                    y = ny

    dfs(idx + 1, cores[idx + 1][0], cores[idx + 1][1], length, cor)
    return


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    processor = [[2] + list(map(int, input().split())) + [2] for _ in range(N)]
    # 0: cell, 1: 렉시노스, 2: 파워
    processor.insert(0, [2] * (N + 2))
    processor.append([2] * (N + 2))
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    # visited = list(processor)
    cores = []
    min_core = 0
    find_core()
    _max = -float('inf')
    _min = float('inf')
    res = 12 ** 2
    result = []
    r = [float('inf')] * len(cores)
    print(cores)
    dfs(0, cores[0][0], cores[0][1], 0, 0)
    print('#{} {}'.format(tc, r))
