# 22251. 빌런 호석

# abcdef, bc, abdeg, abcdg, bcfg, acdfg, acdefg, abc, abcdefg, abcdfg
display = [[1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 0],
           [1, 1, 0, 1, 1, 0, 1],
           [1, 1, 1, 1, 0, 0, 1],
           [0, 1, 1, 0, 0, 1, 1],
           [1, 0, 1, 1, 0, 1, 1],
           [1, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 1]]

nums = [[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        for a in range(7):
            if display[i][a] != display[j][a]:
                nums[i][j] += 1


def check(X, I):
    res = 0
    for _ in range(k):  # k번째 자리까지 검사
        res += nums[X % 10][I % 10]  # 1의자리부터 k번째 자리까지 검사, 자리가 비어있으면 0
        X //= 10
        I //= 10

    if res <= p:
        return 1
    return 0


# n: 총 층수, k: 총 자리 수, p: 총 반전시킬 갯수, x: 현재 층수
n, k, p, x = map(int, input().split())
ans = 0
for i in range(1, n+1):  # n층까지 돌면서 검사
    if x == i:
        continue
    ans += check(x, i)  # x층에서 i층으로 바꿀 수 있으면1, 아니면 0

print(ans)
