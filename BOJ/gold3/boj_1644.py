# 1644. 소수의 연속 합

n = int(input())

nums = [0]*(n+1)
prime_nums = []

# 소수 구하기
for i in range(2, n+1):
    nums[i] = i

for i in range(2, n+1):
    if nums[i] != 0:
        for j in range(2*i, n+1, i):
            nums[j] = 0

for num in nums:
    if num:
        prime_nums.append(num)

ans = 0 # 정답 갯수
x = 2 # 첫 소수인 2부터 시작
s = e = 0
length = len(prime_nums)
while e < length: # 맨 마지막 index면
    if x == n:
        ans += 1
        e += 1
        if e == length:
            break
        x = x - prime_nums[s] + prime_nums[e]
        s += 1
    elif x > n:
        x -= prime_nums[s]
        s += 1
    else:
        e += 1
        if e == length:
            break
        x += prime_nums[e]

print(ans)
