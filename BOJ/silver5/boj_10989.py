# 수 정렬하기 3

import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
cnt = 0
for _ in range(n):
    arr[int(input())] += 1

for i in range(1, 10001):
    x = arr[i]
    while x:
        print(i)
        x -= 1
        cnt += 1
        if cnt == n:
            sys.exit()
