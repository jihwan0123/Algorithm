# 1013. Contact

import sys
import re

input = sys.stdin.readline

t = int(input())
p = re.compile("(100+1+|01)+")
res = []

for _ in range(t):
    m = p.fullmatch(input().strip())
    if m:
        res.append("YES")
    else:
        res.append("NO")

print("\n".join(res))
