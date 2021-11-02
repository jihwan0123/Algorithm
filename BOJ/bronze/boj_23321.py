# 23321. 홍익 댄스 파티

import sys
input = sys.stdin.readline

ready = {('.', 'o', 'm', 'l', 'n'): ('o', 'w', 'l', 'n', '.'),
         ('o', 'w', 'l', 'n', '.'): ('.', 'o', 'm', 'l', 'n')}
images = [input().strip() for _ in range(5)]

temp = list(zip(*images))
for i in range(len(temp)):
    if ready.get(temp[i]):
        temp[i] = ready[temp[i]]

ans = list(zip(*temp))
print('\n'.join([''.join(i) for i in ans]))
