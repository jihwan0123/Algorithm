# 1459: 숫자고르기
n = int(input())
res = []

def check(x):
    global num
    visited[x] = 1
    for y in adj[x]:
        if not visited[y]:
            check(y)
        elif y == num:
            res.append(y)


adj = [[] for _ in range(n+1)]
for i in range(n):
    adj[i+1].append(int(input()))

for num in range(1, n+1):
    visited = [0] * (n+1)
    check(num)

print(len(res))
for j in res:
    print(j)
