# 11906. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬

import sys

sys.stdin = open('swea_5205.txt')


def quick_sort(start, end):
    if start >= end:
        return
    left = start
    right = end
    pivot = A[(start + end) // 2]
    while left <= right:
        while A[left] < pivot:
            left += 1
        while A[right] > pivot:
            right -= 1
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1
    if start < right:
        quick_sort(start, right)
    if left < end:
        quick_sort(left, end)


for tc in range(1, 1 + int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print('#%d %d' % (tc, A[N // 2]))

'''
def quick_sort(left, right):
    if left >= right:
        return
    i = left
    for j in range(left, right):
        if A[j] <= A[right]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[right] = A[right], A[i]
    quick_sort(left, i - 1)
    quick_sort(i + 1, right)


for tc in range(1, 1 + int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print('#%d %d' % (tc, A[N // 2]))
'''
