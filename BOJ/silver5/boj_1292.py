# 1292. 쉽게 푸는 문제

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []
cur = 1
while True:
    for i in range(cur):
        arr.append(cur)
    cur += 1
    if cur == 46:
        break

print(sum(arr[a-1:b]))