# 1304: 숫자사각형3

n = int(input())
nums = [[0] * n for _ in range(n)]
cnt = 1
for j in range(n):
    for i in range(n):
        nums[i][j] = str(cnt)
        cnt += 1

for num in nums:
    print(' '.join(num))
