# 15686. 치킨 배달

import sys
input = sys.stdin.readline


def find_chicken_and_house():  # 모든 치킨집, 가정집 좌표 저장
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                chickens.append((i, j))
            elif data[i][j] == 1:
                houses.append((i, j))


def find_combi(lev, s, u, use):  # m개 조합 저장
    if lev == m:
        combis.append(u.copy())
        return

    for i in range(s, length):
        use[i] = 1
        u.append(chickens[i])
        find_combi(lev+1, i+1, u, use)
        use[i] = 0
        u.remove(chickens[i])


def find_min(c, h):
    result = 2000
    # 전체 조합들 검사
    for combi in c:
        min_distance = 0
        for a, b in h:
            temp = 2000
            for k in range(m):
                # 가정집부터 조합 내의 모든 치킨집중 최소거리 temp에 저장
                temp = min(temp, abs(a - combi[k][0]) + abs(b - combi[k][1]))
            # 최소거리들의 합 min_chicken에 저장
            min_distance += temp
            # 현재 최솟값보다 크면 가지치기
            if min_distance >= result:
                break
        # 최솟값 갱신
        result = min(min_distance, result)

    return result


n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
chickens = []
houses = []
find_chicken_and_house()  # 전체 치킨집과 가정집의 좌표 저장
length = len(chickens)
used = [0] * length
combis = []
find_combi(0, 0, [], used)
print(find_min(combis, houses))


''' 
# 처음 코드 => pypy에서 4700ms
# bfs, list 너무 많이 사용해서 복잡해짐

import sys
input = sys.stdin.readline

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def find_distance(x, y):
    visited = [[0] * n for _ in range(n)]
    q = [(x, y)]
    visited[x][y] = 1
    while q:
        a, b = q.pop(0)
        for dx, dy in dxy:
            nx = a + dx
            ny = b + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                if data[nx][ny] == 1:
                    v[nx][ny] = min(v[nx][ny], abs(x-nx) + abs(y-ny))


def find_chickens():
    x = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == 2:
                x.append((i, j))
    return x


def find_combi(lev, s, u, use):
    if lev == m:
        chicken_combis.append(u.copy())
        return

    for i in range(s, length):
        use[i] = 1
        u.append(chickens[i])
        find_combi(lev+1, i+1, u, use)
        use[i] = 0
        u.remove(chickens[i])


n, m = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(n)]
chickens = find_chickens()
length = len(chickens)
v = [[2500]*n for _ in range(n)]
# m개가 전체 치킨집보다 크면 그냥 계산
if len(chickens) <= m:
    res = 0
    for chicken in chickens:
        find_distance(chicken[0], chicken[1])

    for i in v:
        for j in i:
            if j != 2500:
                res += j
    print(res)

# chickens에서 최대 m개만큼 뽑아야한다.
else:
    result = []
    used = [0] * length
    chicken_combis = []
    find_combi(0, 0, [], used)
    for chicken_combi in chicken_combis:
        res = 0
        v = [[2500]*n for _ in range(n)]
        for c in chicken_combi:
            find_distance(c[0], c[1])

        for i in v:
            for j in i:
                if j != 2500:
                    res += j
        result.append(res)

    print(min(result))

'''