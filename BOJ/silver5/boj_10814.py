# 10814. 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
arr = [input().split() for _ in range(n)]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if int(left[0][0]) <= int(right[0][0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left + right
    return result


ans = merge_sort(arr)
for a in ans:
    print(*a)
