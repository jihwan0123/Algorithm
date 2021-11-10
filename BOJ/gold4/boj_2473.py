# 2473. 세 용액

import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
maxV = sys.maxsize
a = b = c = 0
for i in range(n-2):  # (n-3,n-2,n-1) 인 경우까지 확인해야 하므로 n-2까지
    minV = nums[i]  # 초기값 고정시켜두고 시작
    # 용액 문제 풀이 과정 반복
    s, e = i+1, n-1
    while s < e:
        total = nums[s] + nums[e] + minV
        if (abs(total) < maxV):
            c = minV
            a = nums[s]
            b = nums[e]
            maxV = abs(total)
            # 0이면 바로 종료
            if total == 0:
                print(c, a, b)
                sys.exit()
        if total < 0:
            s += 1
        else:
            e -= 1

print(c, a, b)
