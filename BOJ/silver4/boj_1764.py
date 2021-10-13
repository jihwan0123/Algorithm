# 1764. 듣보잡

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
persons = dict()
for _ in range(n+m):
    p = input().rstrip()
    if persons.get(p):
        persons[p] += 1
    else:
        persons[p] = 1

ans = []
ans_cnt = 0
for person, cnt in sorted(persons.items()):
    if cnt > 1:
        ans_cnt += 1
        ans.append(person)

print(ans_cnt)
print('\n'.join(ans))
