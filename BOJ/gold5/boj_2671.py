# 2671. 잠수함식별

import sys
import re

input = sys.stdin.readline

p = re.compile("(100+1+|01)+")
m = p.fullmatch(input().strip())
if m:
    print("SUBMARINE")
else:
    print("NOISE")
