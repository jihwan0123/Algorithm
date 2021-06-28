# 2637. 장난감조립
# 위상정렬

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
degree = [0] * (n+1)
check = [True] * (n+1)  # 기본부품인지 체크
adj = [[] for _ in range(n+1)]  # 그래프
parts = [[0] * (n + 1) for _ in range(n + 1)]  # 2차원 필요한 부품들


def topoligical_sort():
    q = []
    for i in range(1, n):
        # 위상 0인것부터 시작
        if not degree[i]:
            q.append(i)

    while q:
        # 하나씩 꺼내서 정렬 시작
        now = q.pop(0)
        for part, weight in adj[now]:
            # 기본부품이면
            if check[now]:
                # 가중치 추가
                parts[part][now] += weight
            # 중간 부품이면
            else:
                # 중간부품 갯수 * 가중치만큼 추가
                for i in range(1, n + 1):
                    parts[part][i] += parts[now][i] * weight

            # 다 했으면 node의 위상 -1
            degree[part] -= 1

            # 위상이 0이면 다음 정렬 대상이므로 큐에 추가
            if not degree[part]:
                q.append(part)


for _ in range(m):
    x, y, k = map(int, input().split())
    adj[y].append((x, k))  # y -> x = k 가중치
    degree[x] += 1  # 위상 체크
    check[x] = False  # 기본부품 아닌 것 체크

# 위상 정렬 실행
topoligical_sort()

# 기본부품만 출력
for i in range(1, n+1):
    if check[i]:
        print(i, parts[-1][i])
