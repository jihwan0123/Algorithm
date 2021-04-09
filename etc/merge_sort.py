# merge sort

def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    print(mid, a)
    # 분할
    arr = merge_sort(a[:mid])  # arr, brr 은 정렬된 두개의 배열
    brr = merge_sort(a[mid:])
    print(arr, brr)
    temp = []  # arr, brr 을 합쳐서 하나의 정렬된 배열
    ai = bi = 0
    while ai < len(arr) and bi < len(brr):
        if arr[ai] >= brr[bi]:
            temp.append(brr[bi])
            bi += 1
        else:
            temp.append(arr[ai])
            ai += 1

    temp.extend(arr[ai:])
    temp.extend(brr[bi:])

    return temp


nums = [5, 1, 9, 6, 8, 4, 2, 3, 10]
print(merge_sort(nums))
