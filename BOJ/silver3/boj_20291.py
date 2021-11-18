# 20291. 파일 정리
import sys
input = sys.stdin.readline

n = int(input())
arr = {}
for _ in range(n):
    temp = input().strip().split('.')
    arr[temp[1]] = arr.get(temp[1], 0) + 1

sorted_arr = sorted(arr)
for a in sorted_arr:
    print(a, arr[a])
