# 2960. 에라토스테네스의 체

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(range(n+1))
arr[1] = 0
cnt = 0

while True:
    for a in arr:
        if a:
            s = a
            break
    for i in range(s, n+1, s):
        if arr[i]:
            arr[i] = 0
            cnt += 1
            if cnt == k:
                print(i)
                sys.exit()