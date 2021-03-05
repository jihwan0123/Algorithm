# 1288. 새로운 불면증 치료법

# N의 배수 번호인 양 세기
# 1번째는 N번양, 2번째는 2N번양 ...
# 0 ~ 9 까지 다 세는데 걸리는 횟수

T = int(input())  # T = 5

for tc in range(1, 1 + T):  # tc = 1,2,3,4,5
    N = int(input())  # N = 11
    num = N
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    cnt = 1
    while result:
        N = num * cnt  # N  = 11,22,33,44,55,66,77,88,99,110 ...
        for i in str(N):
            if int(i) in result:
                result.remove(int(i))
                # print(result)
            else:
                pass
        cnt += 1  # cnt = 1,2,3,4,5,6,7,8,9,10
        # print(cnt)

    print('#{} {}'.format(tc, N))

    # N = 11, 22, 33 ,44, 55, 66, 77, 88, 99, 00
