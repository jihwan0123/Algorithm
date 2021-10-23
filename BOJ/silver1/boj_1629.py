# 1629. 곱셈

import sys
input = sys.stdin.readline

a, b, c = list(map(int, input().split()))
print(pow(a,b,c))
# pow(a,b,c) = a의 b제곱을 c로 나눈 나머지