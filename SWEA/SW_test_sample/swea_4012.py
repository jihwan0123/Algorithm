# 4012. [모의 SW 역량테스트] 요리사

import sys

sys.stdin = open('swea_4012.txt')


# 음식 조합
def perm(idx, k):
    global result
    # n개의 조합이 완성됐으면,
    if idx == n:
        sel2 = [i for i in range(N) if visited[i]]
        # sel2 : n개를 뽑고 남은 나머지 n개의 list
        sum1 = sum2 = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                sum1 += S[sel[i]][sel[j]] + S[sel[j]][sel[i]]
                sum2 += S[sel2[i]][sel2[j]] + S[sel2[j]][sel2[i]]
        # food1, food2의 시너지의 합 계산
        x = abs(sum1 - sum2)
        # x : 시너지의 합의 차
        if x < result:
            result = x
            # 최솟값이면 result에 저장
        return

    # k 부터 N 까지 => k부터 하지 않으면 시간초과 발생!
    # k 앞부분은 이미 탐색했으므로 다시 돌 필요가 없다.
    for i in range(k, N):
        if visited[i]:
            sel[idx] = i
            visited[i] = 0
            perm(idx + 1, i + 1)
            visited[i] = 1


ans = []
for tc in range(1, 1 + int(input())):
    N = int(input())
    n = N // 2
    S = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] * N
    # 초기값을 1로 두고 방문했으면 0으로 바꿈
    result = 987654321
    sel = [0] * n
    perm(0, 0)

    ans.append(('#{} {}'.format(tc, result)))

print('\n'.join(ans))
