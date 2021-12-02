# 1182. 부분수열의 합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

arr1 = [0] * (1 << n)
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            arr1[i] += arr[j]

ans = arr1.count(s)
if s == 0:
    ans -= 1
print(ans)
