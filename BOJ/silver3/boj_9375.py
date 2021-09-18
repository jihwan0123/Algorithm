# 9375. 패션왕 신해빈

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    clothes = {}
    for _ in range(n):
        item, classification = input().split()
        if clothes.get(classification):
            clothes[classification] += 1
        else:
            clothes[classification] = 1
    ans = 1
    for i in clothes.values():
        ans *= (i+1)
    
    print(ans-1)
