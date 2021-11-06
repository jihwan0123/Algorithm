# 14620. 꽃길

import sys
input = sys.stdin.readline

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
used = [[False] * n for _ in range(n)]
minV = sys.maxsize


def dfs(lev, total):  # DFS
    global minV
    # 현재 최솟값보다 크면 종료
    if total >= minV:
        return
    # 3개 심었으면 최솟값 갱신
    if lev == 3:
        minV = min(minV, total)
        return
    # 1,1 ~ n-1,n-1 까지 놓을 수 있음
    for i in range(1, n-1):
        for j in range(1, n-1):
            if used[i][j]:
                continue
            chk = False  # 4방향으로 꽃이 필 수 있는지 체크
            s = 0  # 4방향 비용 합
            # 4방향 돌면서
            for dx, dy in dxy:
                nx = i + dx
                ny = j + dy
                # 꽃이 핀 자리면 종료
                if used[nx][ny]:
                    chk = True
                    break
                s += arr[nx][ny]
            # 다음 자리에 놓는다.
            if chk:
                continue
            # 4방향 + 본인 방문처리
            for dx, dy in dxy:
                used[i+dx][j+dy] = True
            used[i][j] = True
            dfs(lev+1, total + s + arr[i][j])
            # 백트래킹
            for dx, dy in dxy:
                used[i+dx][j+dy] = False
            used[i][j] = False


dfs(0, 0)
print(minV)
