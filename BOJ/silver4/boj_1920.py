# 1920. 수 찾기

'''
5
4 1 5 2 3
5
1 3 7 9 5
'''

'''
1
1
0
0
1
'''
def binary_search(arr,target):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right)//2
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0

    
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int,input().split()))

for i in nums:
    print(binary_search(A, i))