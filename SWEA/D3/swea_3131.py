# 3131. 100만 이하의 모든 소수

# 1 이상 100만 이하의 모든 소수
n = 1000001
prime = list(range(n))

for i in range(2, n):
    if prime[i] == 0: continue
    # 자기 자신은 지우지 않는다
    for j in range(2 * i, n, i):
        prime[j] = 0

res = []
for k in range(2, n):
    if prime[k]:
        res.append(k)

print(*res)
