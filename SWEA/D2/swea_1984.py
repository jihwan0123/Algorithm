# 1984. 중간 평균값 구하기

T = int(input())

for tc in range(1, 1 + T):
    nums = list(map(int, input().split()))
    max_num = max(nums)
    min_num = min(nums)

    avg = round((sum(nums) - max_num - min_num) / (len(nums) - 2))
    print('#{} {}'.format(tc, avg))
