# 1490: 다음 조합(next combination)

import sys
input = sys.stdin.readline


def combination(lev, k, s):
    if lev == k:
        arr.append(visited.copy())
        return

    for x in range(s, len(nums)):
        visited[lev] = x
        combination(lev+1, k, x+1)
        visited[lev] = x


n, k = map(int, input().split())
combi = list(map(int, input().split()))
nums = list(range(n+1))
visited = [0] * k
arr = []
combination(0, k, 1)
for i in range(len(arr)):
    if arr[i] == combi and i == (len(arr)-1):
        print('NONE')
        break
    if arr[i] == combi and i != (len(arr)-1):
        print(*arr[i+1])