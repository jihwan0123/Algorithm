# 23561. Young한 에너지는 부족하다.

import sys
input = sys.stdin.readline

n = int(input())
crews = sorted(list(map(int, input().split())))

x = crews[n:2*n]
print(x[-1] - x[0])
# n = 2
# 2, 3
# n = 3
# 3,4,5
# n = 4
# 1 2 3 4 5 6 7 8 9 10 11 12
# crews[n:2*n]
