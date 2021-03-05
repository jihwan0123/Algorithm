# 2001. 파리퇴치

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N, M 입력
    flies = []  # 파리 리스트 담을곳
    for i in range(N):  # N * N 이므로
        fly = list(map(int, input().split()))
        flies.append(fly)
        # list로 바꿔서 flies 리스트에 넣는다.

    result = 0  # 최종값 초기화

    for a in range(N - M + 1):  # 0,0부터 n-m+1, n-m+1 까지 돌면서 합계 계산
        for b in range(N - M + 1):
            fly_sum = 0
            for j in range(a, a + M):  # 0,0 부터 M,M / a,b부터 a+m,b+m 까지 계산해서
                for k in range(b, b + M):
                    fly_sum += flies[j][k]  # fly_sum에 저장

            if fly_sum > result:  # fly_sum이 최대값보다 크면
                result = fly_sum  # 최대값에저장
    # 반복문 끝나면 출력 후 tc 반복
    print('#{} {}'.format(tc, result))
