# 1284. 수도 요금 경쟁

# A사 : 1리터당 P원의 돈을 내야 한다.
# B사 : 기본 요금 Q원, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
# 한달간 사용하는 수도의 양: W (L)

T = int(input())

for i in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    B = 0
    A = W * P  # A 요금

    # B 요금
    if W <= R:
        B = Q

    elif W > R:
        B = (W - R) * S + Q

    # A와 B 요금 비교해서 작은값 = result

    if A >= B:
        result = B

    else:
        result = A

    print('#{} {}'.format(i, result))
