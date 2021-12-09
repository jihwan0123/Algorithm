# 23742. Player-based Team Distribution

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

plus = []
minus = []
total = total_minus = 0
for num in nums:
    if num >= 0:
        plus.append(num)
        total += num
    else:
        minus.append(num)
        total_minus += num

minus.sort(reverse=True)

for i in range(len(minus)):
    # minus를 plus 팀으로 옮길 수 있는지 체크
    if total * len(plus) + total_minus < (total + minus[i]) * (len(plus) + 1) + (total_minus - minus[i]):
        # 옮김
        total += minus[i]
        total_minus -= minus[i]
        plus.append(minus[i])
        minus[i] = 0
    else:  # 안되면 종료
        break

ans = total * len(plus) + total_minus
print(ans)
