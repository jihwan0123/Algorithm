# 23830. 제기차기

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
p, q, r, s = map(int, input().split())
MAX = arr[-1]
total = sum(arr)
ans = -1

# 1부터 최대값까지 탐색
for k in range(1, MAX + 2):
    # k보다 작은 수, k+r보다 큰수 갯수 체크 후 계산
    x = bisect_left(arr, k)
    y = bisect_left(arr, k + r + 1)
    temp = total + (q * x) - (p * (n - y))
    # s보다 크거나 같으면 종료
    if temp >= s:
        ans = k
        break

print(ans)
