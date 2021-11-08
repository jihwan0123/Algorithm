# 2751. 수 정렬하기 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
nums = [int(input()) for _ in range(n)]


def merge_sort(arr):  # 분할
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):  # 병합
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result


ans = merge_sort(nums)
print('\n'.join(map(str, ans)))
