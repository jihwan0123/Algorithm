# 1258. 행렬찾기

import sys

sys.stdin = open('input_1258.txt')


# 시작지점 찾기
def find_start_point(m):
    for x in range(n):
        for y in range(n):
            if m[x][y]:
                return x, y


# box 찾는 함수
def find_box(sr, sc):
    row, col = sr, sc
    while row < n and matrix[row][col]:
        row += 1
    r = row - sr

    row, col = sr, sc
    while col < n and matrix[row][col]:
        col += 1
    c = col - sc

    # 넓이, 좌표 저장
    area.append(r * c)
    point.append((r, c))
    changeZero((sr, sc), (sr + r, sc + c))
    return


# point1 ~ point2 사이의 사각형 모두 0으로 바꾸기
def changeZero(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 0


# 정렬
def area_sort():
    for j in range(lg - 1):
        for i in range(lg - j - 1):
            if area[i] > area[i + 1]:
                point[i], point[i + 1] = point[i + 1], point[i]
                area[i], area[i + 1] = area[i + 1], area[i]
            elif area[i] == area[i + 1]:
                # 같으면 row값이 더 작은 값이 앞으로 가도록 정렬
                if point[i][0] > point[i + 1][0]:
                    point[i], point[i + 1] = point[i + 1], point[i]
                    area[i], area[i + 1] = area[i + 1], area[i]


for tc in range(1, 1 + int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    area, point = [], []
    # 시작지점을 찾을수 없으면 반복 종료
    while find_start_point(matrix):
        # 시작점 찾고
        a, b = find_start_point(matrix)
        # box 찾아서 넓이랑 좌표 저장
        find_box(a, b)

    lg = len(area)
    area_sort()

    print('#{} {}'.format(tc, lg), end=' ')
    for i in point:
        print(i[0], i[1], end=' ')
    print()
