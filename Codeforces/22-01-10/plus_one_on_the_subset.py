# A. Plus One on the Subset

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max(arr) - min(arr))