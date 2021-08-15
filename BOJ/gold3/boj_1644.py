# 1644. 소수의 연속 합

n = int(input())

# 소수 구하기
nums = list(range(n+1))
nums[1] = 0

for i in range(2, n+1):
    if nums[i] != 0:
        for j in range(2*i, n+1, i):
            nums[j] = 0

prime_nums = []
for num in nums:
    if num:
        prime_nums.append(num)

ans = 0  # 정답 갯수
x = 2  # 첫 소수인 2부터 시작
s = e = 0
length = len(prime_nums)
while e < length:  # 맨 마지막 index면 종료
    if x == n: # 같으면 ans,s,e: + 1
        ans += 1
        e += 1
        if e == length: # e == length면 다음 while 문에서 index error 발생하므로 종료
            break
        x = x - prime_nums[s] + prime_nums[e]
        s += 1
    elif x > n: # 더 크면 s + 1
        x -= prime_nums[s]
        s += 1
    else: # 작으면 e + 1
        e += 1
        if e == length: # e == length면 다음 while 문에서 index error 발생하므로 종료
            break
        x += prime_nums[e]

print(ans)
