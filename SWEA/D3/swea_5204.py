# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬

import sys

sys.stdin = open('swea_5204.txt')

'''
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    print(mid, arr)
    # 분할
    a = merge_sort(arr[:mid])  # arr, brr 은 정렬된 두개의 배열
    b = merge_sort(arr[mid:])
    print(a, b)
    c = []  # arr, brr 을 합쳐서 하나의 정렬된 배열
    ai = bi = 0
    while ai < len(a) and bi < len(b):
        if a[ai] >= b[bi]:
            c.append(b[bi])
            bi += 1
        else:
            c.append(a[ai])
            ai += 1

    c.extend(a[ai:])
    c.extend(b[bi:])

    return c
'''


def merge(left, right):
    global cnt
    sorted_list = []
    i = j = 0
    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    if j < len(left):
        sorted_list.extend(right[j:len(right)])
    if i < len(right):
        sorted_list.extend(left[i:len(left)])

    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return merge(left, right)


for tc in range(1, 1 + int(input())):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    cnt = 0
    res = merge_sort(A)

    print('#{} {} {}'.format(tc, res[N // 2], cnt))
