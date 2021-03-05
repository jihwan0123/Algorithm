# 11387. 몬스터사냥

T = int(input())

for tc in range(1, 1 + T):
    D, L, N = map(int, input().split())
    total = 0
    for i in range(N):
        damage = D * (1 + i * L / 100)
        total += damage

    print('#{} {}'.format(tc, int(total)))
