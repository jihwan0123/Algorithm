from collections import Counter

ans = 987654321
def dfs(cur, used, temp, cnt, target):
    global ans
    if temp[cur] == target:
        ans = min(cnt, ans)
    for i in range(len(temp)):
        if used[i]:
            continue
        if sum((temp[cur] - temp[i]).values()) == 1:
            used[i] = 1
            dfs(i, used, temp, cnt+1, target)
            used[i] = 0


def solution(begin, target, words):
    global ans
    if target not in words:
        return 0

    temp = []
    used = [0] * (len(words)+1)

    begin = Counter(begin)
    target = Counter(target)

    for w in words:
        temp.append(Counter(w))

    for i in range(len(temp)):
        if used[i]:
            continue
        if sum((begin - temp[i]).values()) == 1:
            dfs(i, used, temp, 1, target)

    return ans


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
