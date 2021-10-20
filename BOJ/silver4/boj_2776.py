# 2776. 암기왕

from collections import Counter
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n1 = int(input())
    arr1 = Counter(map(int, input().split()))
    n2 = int(input())
    arr2 = map(int, input().split())
    for a in arr2:
        print(1 if arr1.get(a) else 0)