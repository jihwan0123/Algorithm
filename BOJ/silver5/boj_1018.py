# 1018. 체스판 다시 칠하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chess = [input().strip() for _ in range(n)]
ans = 64


def chess_paint(x, y):  # 색칠할 칸 계산
    cnt = 0
    # 8 * 8 크기 검사
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) & 1:  # 홀수칸
                if chess[i][j] != 'B':
                    cnt += 1
            else:  # 짝수칸
                if chess[i][j] != 'W':
                    cnt += 1
    return cnt


# 8 * 8 체스판으로 자르기
for x in range(n-7):
    for y in range(m-7):
        res = chess_paint(x, y)
        ans = min(ans, res, 64-res)

print(ans)
