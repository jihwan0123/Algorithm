# 13458. 시험 감독

import math

n = int(input())
A = list(map(int, input().split()))  # 응시자수
B, C = map(int, input().split())  # B : 총감독관, C: 부감독관
ans = n
for i in range(len(A)):
    A[i] -= B
    if A[i] > 0:
        ans += math.ceil(A[i]/C)


print(ans)
