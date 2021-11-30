# 23740. 버스 노선 개편하기

import sys
input = sys.stdin.readline

n = int(input())
buses = sorted([tuple(map(int, input().split())) for _ in range(n)])

left, right, val = buses[0]
ans = []
for i in range(1, n):
    if right < buses[i][0]:
        ans.append((left, right, val))
        left = buses[i][0]
        right = buses[i][1]
        val = buses[i][2]
    else:
        right = max(right, buses[i][1])
        val = min(val, buses[i][2])

ans.append((left, right, val))
print(len(ans))
for a in ans:
    print(*a)
