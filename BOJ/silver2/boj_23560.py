# 23560. 약

import sys
input = sys.stdin.readline

n = int(input())

# ABAABAABA : 앞에 먹고 시작 OR 뒤에 먹고 시작 = 2
# BAABAABA
# ABAABAAB
# 앞에서 3개 먹는 경우, 뒤에서 3개 먹는 경우, 양쪽 먹고 하나 먹는 경우 = 3 ** (N-1)
# 1개만 남았을때는 1가지
print(2 * 3**(n-1))
