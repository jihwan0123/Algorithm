# 1244. 최대 상금

import sys

sys.stdin = open('swea_1244.txt')


def dfs(count):
    global ans
    # 교환 횟수 다 사용했으면
    if not count:
        temp = int(''.join(nums))
        # 최댓값과 비교해서 저장
        if ans < temp:
            ans = temp
        return

    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            temp = int(''.join(nums))
            # (temp, count) : count번 남았을때 temp
            # 이미 있는 경우 제외해도 됨
            if visited.get((temp, count), 1):
                visited[(temp, count)] = 0
                # dfs 반복
                dfs(count - 1)
            # 다시 돌아가서 반복
            nums[i], nums[j] = nums[j], nums[i]


for tc in range(1, 1 + int(input())):
    num, cnt = input().split()
    nums = list(num)
    length = len(nums)
    visited = {}
    ans = 0
    dfs(int(cnt))
    # print(visited)
    print('#{} {}'.format(tc, ans))
