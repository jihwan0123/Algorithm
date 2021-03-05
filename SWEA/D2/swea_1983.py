# 1983. 조교의 성적 매기기

T = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# 학점을 출력해야함
# N=10이면 등수대로
# N=20이면 N/10=2    1,2=0  3,4=1  5,6=2  7,8=3 ...
# N=30이면 N/10=3    1,2,3=0    4,5,6=1   7,8,9=2 ...

for tc in range(1, 1 + T):
    N, K = map(int, input().split())  # N = 학생수, K = 학생 번호
    score = {}  # 학생 환산 점수 순서별로 넣어둠
    for i in range(1, N + 1):
        scores = list(map(int, input().split()))
        score[i] = scores[0] * 0.35 + scores[1] * 0.45 + scores[2] * 0.20
        # score dict에 i번째 = 환산점수

    # score 정렬하면서 학생 정렬
    result = sorted(score, key=lambda k: score[k], reverse=True)
    cnt = 0
    # print(result)

    for j in result:
        if j == K:
            # print(cnt)
            print('#{} {}'.format(tc, grade[int(cnt // (N / 10))]))  # cnt를 N/10으로 나눈 몫에 int형 하므로
        else:
            cnt += 1
