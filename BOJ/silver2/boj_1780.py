# 1780. 종이의 개수

import sys
input = sys.stdin.readline


def divide(x, y, n):  # x,y에서부터 n*n
    for i in range(x, x + n):
        for j in range(y, y + n):
            if papers[x][y] != papers[i][j]:
                n //= 3
                # 9등분해서 반복
                for a in range(3):
                    for b in range(3):
                        divide(x+n*a, y+n*b, n)
                return
    # 모두 같으면 해당 종이 +1
    ans[papers[x][y]] += 1


n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
ans = [0] * 3
divide(0, 0, n)
for i in (-1, 0, 1):
    print(ans[i])
