# 지그재그 숫자
T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    result = 0
    for i in range(1, N + 1):
        if i % 2:  # 홀수면
            result += i
        else:
            result -= i

    print('#{} {}'.format(tc, result))
