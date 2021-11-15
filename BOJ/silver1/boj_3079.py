# 3079. 입국심사
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

ans = 0
left = 1
right = max(times)*m+1
# 0 ~ max 시간 중에서 최솟값 찾기
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    # 가능한 cnt 인원 세기
    for time in times:
        cnt += mid//time
    # cnt가 m명보다 크면 왼쪽탐색
    if cnt >= m:
        ans = mid
        right = mid - 1
    # 작으면 오른쪽 탐색
    else:
        left = mid + 1

print(ans)
