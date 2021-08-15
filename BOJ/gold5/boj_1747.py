# 1747. 소수 & 팰린드롬

n = int(input())
MAX_SIZE = 1003001
nums = [0]*(MAX_SIZE)


def is_pallindrome(x):
    return str(x) == str(x)[::-1]


# 소수 구하기
nums = list(range(MAX_SIZE+1))
nums[1] = 0
for i in range(2, MAX_SIZE):
    if nums[i] != 0:
        for j in range(2*i, MAX_SIZE, i):
            nums[j] = 0

for i in range(n, MAX_SIZE+1):
    if nums[i] and is_pallindrome(i):
        print(i)
        break