# 13019. A를 B로

import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

# A, B의 문자열 원소가 다르면 -1
if sorted(A) != sorted(B):
    print(-1)
    sys.exit()

ans = len(A)
# 뒤에서부터 한 칸씩 이동하면서 연속된 개수 체크
i = j = len(A)-1
while i >= 0 and j >= 0:
    if A[i] == B[j]:  # 같으면
        # 한 칸 앞 체크
        ans -= 1
        i -= 1
        j -= 1
    else:  # 다르면
        # A만 앞으로 이동 후 체크
        i -= 1

# 나머지만 움직이면 된다.
print(ans)
