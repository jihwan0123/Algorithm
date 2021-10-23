# 16564. 히오스 프로게이머

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
level = sorted([int(input()) for _ in range(n)])

left = level[0]  # 최소값
right = level[0] + k  # 답이 될 수 있는 최대값
ans = 0

while left <= right:
    mid = (left + right) // 2

    # k번으로 전부 mid 값을 만들 수 있는지 체크
    chk = False
    temp = 0
    for i in range(n):
        if mid > level[i]:
            temp += mid - level[i]
            if temp > k:
                chk = True
                break
        else:
            break

    if chk:  # temp > k면 mid 왼쪽 탐색
        right = mid - 1
    else:  # temp <= k면 mid 오른쪽 탐색
        ans = mid
        left = mid + 1

print(ans)
