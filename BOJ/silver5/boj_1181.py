# 1181. 단어 정렬

import sys
input = sys.stdin.readline

n = int(input())
arr = set(input().strip() for _ in range(n))
arr = sorted(arr, key=lambda x: (len(x), x))
for a in arr:
    print(a)
