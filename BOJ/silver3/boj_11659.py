# 11659: 구간 합 구하기4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

mid_sum = [0] * (n+1)
for n in range(1, n+1):
    mid_sum[n] = (mid_sum[n-1] + nums[n-1])

for _ in range(m):
    i, j = map(int, input().split())
    print(mid_sum[j]-mid_sum[i-1])
