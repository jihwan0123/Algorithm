# 10580. 전봇대

import sys

sys.stdin = open('swea_10580.txt')

for tc in range(1, 1 + int(input())):
    N = int(input())
    # N : 전선의 갯수
    wire = [tuple(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 첫번째 와이어부터 마지막 와이어까지 비교
    for i in range(N):
        a, b = wire[i]
        for j in range(N):
            if i == j:
                continue
            c, d = wire[j]
            # 겹치는경우: 시작점이 더 위에있고, 도착점이 더 아래이거나 반대이거나
            if (a < c and b > d) or (a > c and b < d):
                cnt += 1
    # 접점 하나당 2번씩 cnt 되었으므로 2로 나눠준다.
    print('#{} {}'.format(tc, cnt // 2))
