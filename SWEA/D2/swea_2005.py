# 2005. 파스칼의 삼각형

import sys

sys.stdin = open('swea_2005_pascal.txt')

for tc in range(1, 1 + int(input())):
    N = int(input())
    result = [[1]]

    for i in range(1, N):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(temp)

    print('#%d' % tc)
    for k in range(N):
        print(' '.join(map(str, result[k])))
