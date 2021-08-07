# 1300. K번째 수

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

ans = left = 1
right = k
while left <= right:  # left = right가 될때까지 반복
    mid = (left + right) // 2

    # mid 이하인 수의 갯수의 합
    cnt = sum([min(mid//i, n) for i in range(1, n+1)])

    if cnt < k:  # cnt가 k보다 작으면 오른쪽부분 탐색
        left = mid + 1
    else:  # 아니면 ans 저장해두고 왼쪽부분 탐색
        ans = mid
        right = mid - 1

print(ans)
