# 16208 귀찮음

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
ans = 0
length = sum(a)
for i in range(n):
    ans += a[i]*(length-a[i])
    length -= a[i]

print(ans)