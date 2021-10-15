# 1157. 단어공부

import sys
from collections import Counter

s = input().upper()
if len(s) == 1:
    print(s)
    sys.exit()

s = Counter(s)

arr = sorted(s.items(), key=lambda x:x[1], reverse=True)
if arr[0][1] == arr[1][1]:
    print('?')
else:
    print(arr[0][0])