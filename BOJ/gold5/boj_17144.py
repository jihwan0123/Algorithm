# 17144. 미세먼지 안녕!

import sys
import copy
input = sys.stdin.readline

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 위, 오른쪽,아래쪽,왼쪽 : 위에 공기청정기 루트
dxy1 = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 아래, 오른쪽, 위쪽, 왼쪽 : 아래 공기청정기 루트
r, c, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]
B = copy.deepcopy(A)


def find_cleaner():  # 공기청정기 좌표 확인
    for i in range(r):
        if A[i][0] == -1:
            return i


def run(cleaner):
    # 1. 미세먼지 확산
    global A
    for x in range(r):
        for y in range(c):
            if A[x][y] >= 5:
                dust = A[x][y] // 5
                for dx, dy in dxy:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c and A[nx][ny] != -1:
                        B[x][y] -= dust
                        B[nx][ny] += dust

    # 2. 공기청정기 작동
    # 위에꺼
    a, b = cleaner, 0
    for da, db in dxy:
        while 0 <= a+da < cleaner+1 and 0 <= b+db < c:
            B[a][b] = B[a+da][b+db]
            a = a + da
            b = b + db
        B[cleaner][0] = 0  # 공기청정기 0으로 바꿔서 영향없도록 설정
    # 아래꺼
    a, b = cleaner+1, 0
    for da, db in dxy1:
        while cleaner+1 <= a+da < r and 0 <= b+db < c:
            B[a][b] = B[a+da][b+db]
            a = a + da
            b = b + db
        B[cleaner+1][0] = 0

    # 3. 1회 실행 이후 A 갱신
    A = copy.deepcopy(B)


air_cleaner = find_cleaner()

for _ in range(t):  # t번 실행
    run(air_cleaner)

ans = 0
for i in B:  # 전체 미세먼지 합 계산
    ans += sum(i)

print(ans)
