# 4485. 녹색 옷 입은 애가 젤다지?

import sys
import heapq
input = sys.stdin.readline

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]

cnt = 1
while True:
    n = int(input().strip())
    if n == 0:
        break

    rupees = [list(map(int, input().strip().split())) for _ in range(n)]  # 루피
    result = [[float("inf")] * n for _ in range(n)]  # 결과 최댓값으로 초기화
    q = []
    heapq.heappush(q, (rupees[0][0], 0, 0))

    while q:
        w, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            break
        # 상하 좌우 1칸씩 이동
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            # 루피의 크기가 최소가 되는곳이면 이동
            if 0 <= nx < n and 0 <= ny < n and result[nx][ny] > w + rupees[nx][ny]:
                result[nx][ny] = w + rupees[nx][ny]
                heapq.heappush(q, (result[nx][ny], nx, ny))

    print(f'Problem {cnt}: {result[n-1][n-1]}')
    cnt += 1
