# 피로도

ans = 0


def dfs(cur, dungeons, used, cnt):
    global ans
    if cur <= 0 or cnt == len(dungeons):
        return

    for i in range(len(dungeons)):
        if used[i] == 1:
            continue
        if cur >= dungeons[i][0]:
            used[i] = 1
            ans = max(ans, cnt+1)
            dfs(cur - dungeons[i][1], dungeons, used, cnt+1)
            used[i] = 0


def solution(k, dungeons):
    used = [0] * (len(dungeons)+1)
    dungeons = sorted(dungeons)
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            used[i] = 1
            dfs(k-dungeons[i][1], dungeons, used, 1)
            used[i] = 0

    return ans


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
