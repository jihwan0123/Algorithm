# 1438: 색종이(초)

n = int(input())  # 색종이의 수
papers = [[0]*(101) for _ in range(101)]


def check_paper(a, b):
    for i in range(a, a+10):
        for j in range(b, b+10):
            papers[i][j] = 1


for i in range(n):
    s, e = map(int, input().split())
    check_paper(s, e)

res = 0
for paper in papers:
    res += paper.count(1)

print(res)
