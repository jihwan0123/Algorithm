# 2567 : 사이클

import sys
input = sys.stdin.readline

n, p = map(int, input().split())
x = n
k = 0
nums = []
res = set()
while True:
    x = x*n - p * (x*n // p)
    if x not in nums:
        nums.append(x)
    else:
        length = len(res)
        res.add(x)
        after_length = len(res)
        if length == after_length:
            print(len(res))
            break