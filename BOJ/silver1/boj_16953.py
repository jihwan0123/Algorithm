# 16953. A -> B

import sys

# sys.stdin = open('boj_16953.txt')
'''
for tc in range(1,1+int(input())):
    a, b = map(int,input().split())
    queue = [(a,1)]
    print(queue)
    ans = -1
    while queue:
        n, cnt = queue.pop()
        if n == b:
            ans = cnt
            break
        n1 = n * 2
        n2 = n * 10 + 1

        if n1 <= b:
            queue.append((n1,cnt+1))
        if n2 <= b:
            queue.append((n2,cnt+1))
    print('#{} {}' .format(tc, ans))
'''


a, b = map(int,input().split())
queue = [(a,1)]
ans = -1
while queue:
    n, cnt = queue.pop()
    if n == b:
        ans = cnt
        break
    n1 = n * 2
    n2 = n * 10 + 1

    if n1 <= b:
        queue.append((n1,cnt+1))
    if n2 <= b:
        queue.append((n2,cnt+1))
print(ans)