# B. Make AP

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    # x, x+t, x+2t
    if ((a + c) / 2) % b == 0:
        print("YES")
        continue
    if (2 * b - c) >= a and (2 * b - c) % a == 0:
        print("YES")
        continue
    if (2 * b - a) >= c and (2 * b - a) % c == 0:
        print("YES")
        continue
    print("NO")
