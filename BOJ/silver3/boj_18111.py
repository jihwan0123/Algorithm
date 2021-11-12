# 18111. 마인크래프트

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

# dict에 몇번 나왔는지 저장
nums = dict()
for _ in range(n):
    arr = list(map(int, input().split()))
    for a in arr:
        nums[a] = nums.get(a, 0)+1

ans = 0
minV = sys.maxsize
# 0 ~ 256까지 확인
for i in range(257):
    cnt = 0
    block_cnt = b
    # dict 저장했던 값 돌면서
    for num in nums:
        x = nums.get(num)
        if num == i:
            continue
        # num이 크면
        elif num > i:
            # x2해서 계산
            cnt += 2 * x * (num-i)
            block_cnt += x * (num-i)
        else:
            cnt += x * (i - num)
            block_cnt -= x * (i - num)
    # cnt가 minV 보다 커지면 뒤에 확인할 필요 없음
    if cnt > minV:
        break
    # 블록 갯수 체크 + minV가 cnt보다 크면 최솟값 교체
    # 답이 여러개 있으면 가장 높은 값 출력해야 하므로 minV >= cnt
    if block_cnt >= 0 and minV >= cnt:
        minV = cnt
        ans = i

print(minV, ans)
