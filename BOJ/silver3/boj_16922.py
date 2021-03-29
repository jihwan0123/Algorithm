# 16922. 로마 숫자 만들기

nums = (1, 5, 10, 50)

def dfs(i, cnt):
    global res
    if cnt == N:
        result.add(res)
        return

        
    for j in range(i, 4):
        if not visit[cnt]:
            res += nums[j]
            dfs(j, cnt + 1)
            res -= nums[j]


N = int(input())
visit = [0] * N
res = 0
result = set()
dfs(0, 0)
print(len(result))
    