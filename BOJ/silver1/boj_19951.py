# 19951. 태상이의 훈련소 생활

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
heights = [0] * (n+1)
for _ in range(m):
    a, b, k = map(int, input().split())
    heights[a-1] += k
    heights[b] -= k

prefix_sum = 0
for i in range(n):
    prefix_sum += heights[i]
    h[i] += prefix_sum

print(*h)
