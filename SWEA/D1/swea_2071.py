T = int(input())  # test case 갯수 입력

for i in range(1, T + 1):
    tc = input()  # test case 번호
    test_case = list(map(int, tc.split()))  # int 형으로 변환해서 list형으로 저장
    total = 0  # 총합 초기화
    for j in test_case:
        total += j
    print(f'#{i} {round(total / len(test_case))}')
