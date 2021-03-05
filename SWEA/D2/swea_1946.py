# swea_1946 간단한 압축 풀기

import sys

sys.stdin = open('swea_1946.txt')

T = int(input())

for tc in range(1, 1 + T):
    n = int(input())
    print('#%d' % tc)
    result = []
    for i in range(n):
        c, k = input().split()
        # c : 알파벳 , k = 연속으로 나오는 횟수
        for j in range(int(k)):
            result.append(c)
            # 10개 모이면 출력
            if len(result) == 10:
                print(''.join(result))
                result.clear()
            # 전체 횟수를 다 돌아도 출력
            elif j == int(k) - 1 and i == n - 1:
                print(''.join(result))
