# 2675. 문자열반복

t = int(input())
for _ in range(t):
    r, s = input().split()
    r = int(r)
    ans = ''
    for i in s:
        ans += i*r

    print(ans)