# 20159. 동작 그만, 밑장 빼기냐?

n = int(input())
x = n // 2
cards = list(map(int, input().split()))
me = [0] * (x+1)  # 정훈이 점수
you = [0] * (x+1)  # 상대방 점수
# 부분합 계산
for i in range(n):
    if i % 2:
        you[i//2+1] = you[i//2] + cards[i]
    else:
        me[i//2+1] = me[i//2] + cards[i]


ans = max(me[-1], you[-1])
for i in range(1,x):
    a = b = me[i]
    a += (you[-1] - you[i]) # 내차례에 밑장빼기
    b += (you[-2] - you[i-1]) # 상대차례에 밑장빼기
    ans = max(ans, a, b)
print(ans)
