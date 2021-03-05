# 1204. 최빈수 구하기

num = int(input())

for i in range(num):  # 테스트 케이스 수만큼 반복
    case = int(input())  # 몇 번째 case인지
    test = input()  # 입력값
    # 입력 받은 값을 공백 단위로 쪼개서 int형으로 저장
    test_case = list(map(int, test.split()))
    grade = [0] * 101  # 0~100점 각각 0번씩 초기값 설정

    for i in test_case:  # test case 돌면서 0점부터 100점까지 일치하면 갯수 증가
        grade[i] += 1
        max_grade = max(grade)  # 가장 큰 값 max_grade에 저장

    for score in range(100, -1, -1):  # 100~0점 순으로 비교해서 같으면 출력
        if max_grade == grade[score]:
            print('#{} {}'.format(case, score))
            break
