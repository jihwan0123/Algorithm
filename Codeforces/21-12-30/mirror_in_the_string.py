# B. Mirror in the String

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    s = input().strip()
    if len(s) == 1:
        ans.append(s * 2)
        continue
    temp = s[0]
    for i in range(1, n):
        if ord(s[i]) > ord(temp[-1]):
            break
        # zaaz
        # zaaaaz 같은 경우 처리용
        if s[i] == temp[-1] and ord(s[0]) <= ord(temp[-1]):
            break
        temp += s[i]
    ans.append(temp + temp[::-1])
print("\n".join(ans))


"""input
4
10
codeforces
9
cbacbacba
3
aaa
4
bbaa
"""
"""output
cc
cbaabc
aa
bb
"""
