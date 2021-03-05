# 10965. 제곱수 만들기

import sys

sys.stdin = open('swea_10965.txt')

prime = [2]
for i in range(3, int(10000000 ** (1 / 2)), 2):
    for p in prime:
        if not i % p:
            break
    else:
        prime.append(i)

result = []
T = int(input())
for tc in range(1, T + 1):
    A = int(input())
    res = 1
    if A ** 0.5 != int(A ** 0.5):
        for p in prime:
            cnt = 0
            while not A % p:
                A //= p
                cnt += 1
            if cnt % 2:
                res *= p
            if p >= A:
                break
        if A > 1:
            res *= A
    result.append('#{} {}'.format(tc, res))
    # result에 결과를 담아놓고 한번에 출력해야 시간을 줄일 수 있다.
print('\n'.join(result))
