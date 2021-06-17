# 1169: 주사위 던지기1

'''
m = 1

1 1 1
1 1 2
1 1 3
1 1 4
1 1 5
1 1 6
1 2 1
…
6 6 6

m = 2

1 1 1
1 1 2
…
1 1 6
1 2 2
…
5 6 6
6 6 6

m = 3

1 2 3
1 2 4
1 2 5
1 2 6
1 3 2
1 3 4
…
6 5 3
6 5 4
'''

n, m = map(int, input().split())
numbers = list(range(1, 7))
result = [0] * n
visited = [0] * 7


def dice1(lev):  # N 번 던져서 나올 수 있는 모든 경우
    if lev == n:
        print(*result)
        return

    for i in range(6):
        result[lev] = numbers[i]
        dice1(lev+1)
        result[lev] = 0


def dice2(lev, s):  # N 번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
    # s보다 같거나 큰 수만 넣어야 한다.
    if lev == n:
        print(*result)
        return

    for i in range(s, 6):
        result[lev] = numbers[i]
        dice2(lev+1, i)
        result[lev] = 0


def dice3(lev):  # N 번 던져서 모두 다른 수가 나올 수 있는 모든 경우
    if lev == n:
        print(*result)
        return

    for i in range(6):
        if visited[numbers[i]]:
            continue

        result[lev] = numbers[i]
        visited[numbers[i]] = 1
        dice3(lev+1)
        result[lev] = 0
        visited[numbers[i]] = 0


if m == 1:
    dice1(0)

elif m == 2:
    dice2(0, 0)

elif m == 3:
    dice3(0)
