# 1671. 색종이(중)

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
n = int(input())
papers = [[0]*(105) for _ in range(105)]


# 종이 놓여진 위치 표시
def check_paper(a, b):
    for i in range(a, a+10):
        for j in range(b, b+10):
            papers[i][j] = 1


# 변인지 확인
def check_side(x, y):
    cnt = 0
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 105 and 0 <= ny < 105 and papers[nx][ny]:
            cnt += 1
    return cnt


for k in range(n):
    s, e = map(int, input().split())
    check_paper(s, e)


res = 0
for r in range(105):
    for c in range(105):
        if papers[r][c] == 0:
            res += check_side(r, c)

print(res)


# for i in papers:
#     print(*i)
