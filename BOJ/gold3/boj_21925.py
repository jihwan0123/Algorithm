# 21925. 짝수 팰린드롬

from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 숫자 짝이 안맞으면 -1
x = Counter(nums)
for i in x:
    if x.get(i) & 1:
        print(-1)
        sys.exit()

# 2칸 간격으로 팰린드롬인지 체크
s, e = 0, 2
cnt = 0
chk = False
while e <= n:
    temp = nums[s:e]
    # 팰린드롬이면
    if temp == temp[::-1]:
        # e부터 2칸간격으로 다시 체크
        chk = True
        s = e
        e += 2
        cnt += 1
    else:
        # 마지막에 팰린드롬 아니면 chk=False
        chk = False
        e += 2

print(cnt if chk else -1)
