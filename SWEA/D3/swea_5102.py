import sys

sys.stdin = open('swea_5102.txt', 'r')

T = int(input())


def bfs_graph(g, start, end):
    queue = [start]
    visited[start] = 0
    while queue:
        a = queue.pop(0)
        level = visited[a]
        for i in g[a]:
            if i == end:
                return level + 1
            if not visited[i]:
                visited[i] = level + 1
                queue.append(i)
    return 0


for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    AL = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for s, e in edges:
        AL[s].append(e)
        AL[e].append(s)

    print('#{} {}'.format(tc, bfs_graph(AL, S, G)))

'''
def BFS(sV):
    # 큐를 생성과 동시에 선언
    Q = [(sV, 0)]
    # 방문체크를 위한
    visited = [False] * (V + 1)
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)
        # 현재 내가 서있는 위치가 도착지라면 거리르 반환하고 끝냄
        if v == eV:
            return dist

        for i in range(1, V + 1):
            if adj_arr[v][i] == 1 and visited[i] == False:
                Q.append([i, dist + 1])
                visited[i] = True
    return 0


def BFS2(sV):
    # 큐를 생성과 동시에 선언
    Q = [sV]
    # 방문체크를 위한
    visited = [False] * (V + 1)
    visited[sV] = True
    dist = 0
    while Q:
        size = len(Q)
        for i in range(size):
            v = Q.pop(0)
            if v == eV: return dist

            for i in range(1, V + 1):
                if not visited[i] and adj_arr[v][i]:
                    Q.append(i)
                    visited[i] = True
        dist += 1
    return 0


for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 정점의 수 1번부터 시작, E: 간선의 수

    # 인접행렬을 이용하여 작성해보자
    adj_arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        # 무방향이므로 양쪽 연결
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    # 시작점, 끝점
    sV, eV = map(int, input().split())

    print('#{} {}'.format(tc, BFS2(sV)))
'''
