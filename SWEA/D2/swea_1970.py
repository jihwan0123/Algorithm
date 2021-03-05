# 1970. 쉬운 거스름돈

import sys

sys.stdin = open('easy_change_iunput.txt')

T = int(input())

for tc in range(1, 1+T):
    n = int(input().strip())
    result = []

    count = n//50000
    result.append(str(count))
    n = n - count * 50000

    count = n // 10000
    result.append(str(count))
    n = n - count * 10000

    count = n//5000
    result.append(str(count))
    n = n - count * 5000

    count = n//1000
    result.append(str(count))
    n = n - count * 1000

    count = n//500
    result.append(str(count))
    n = n - count * 500

    count = n//100
    result.append(str(count))
    n = n - count * 100

    count = n//50
    result.append(str(count))
    n = n - count * 50

    count = n // 10
    result.append(str(count))

    change = ' '.join(result)

    print('#%d\n%s' %(tc, change))
