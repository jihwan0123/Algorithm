# 14003. 가장 긴 증가하는 부분 수열 5
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

temp = []  # LIS 저장
check = []  # 모든 문자에 대해 최장 길이 저장

# LIS 구하면서 각 문자에 대한 최장 길이 저장
for x in nums:
    if not temp or temp[-1] < x:
        temp.append(x)
        check.append(len(temp))
    else:
        idx = bisect_left(temp, x)
        temp[idx] = x
        check.append(idx+1)

length = len(temp)  # length = LIS 길이
print(length)
res = []
# check 배열 역방향으로 체크
for i in range(len(check)-1, -1, -1):
    # 최장길이부터 내려오면서 체크하면서 문자열 저장
    if check[i] == length:
        res.append(nums[i])
        length -= 1

    if length == 0:
        break
# 역순으로 출력
print(*res[::-1])

'''
4    
1 3 2 4
# 1 2 4

6 
4 5 6 1 2 3
# 1 2 3 or 4 5 6
'''
