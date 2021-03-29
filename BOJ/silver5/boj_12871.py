# 12871. 무한 문자열

s = input()
t = input()

if len(s) > len(t):
    s, t = t, s

S = s * len(t)
T = t * len(s)

if S == T:
    print(1)
else:
    print(0)