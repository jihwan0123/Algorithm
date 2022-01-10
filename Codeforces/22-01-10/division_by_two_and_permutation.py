# C. Division by Two and Permutation

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    used = [0] * (n + 1)
    arr = sorted(list(map(int, input().split())), reverse=True)

    for i in range(n):
        while arr[i] > n:
            arr[i] //= 2
        while used[arr[i]] == 1:
            arr[i] //= 2
        while arr[i] > 0 and not used[arr[i]]:
            if arr[i] <= n and used[arr[i]] == 0:
                used[arr[i]] = 1
                arr[i] = 0
                break
            arr[i] //= 2
    chk = False
    for i in range(1, n + 1):
        if used[i] == 0:
            chk = True
            break
    if not chk:
        print("YES")
        continue
    print("NO")
