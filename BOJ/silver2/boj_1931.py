# 1931. 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key = lambda x: (x[1], x[0]))
cur = cnt= 0
for s, e in times:
    if s >= cur:
        cnt += 1
        cur = e

print(cnt)