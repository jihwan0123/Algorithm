# 1314. 문자사각형2

n = int(input())
cnt = ord('A')
characters = [[0] * n for _ in range(n)]
for i in range(n):
    if i % 2:
        for j in range(n-1,-1,-1):
            characters[j][i] = chr(cnt)
            cnt += 1
            if cnt > ord('Z'):
                cnt = ord('A')
    else:
        for j in range(n):
            characters[j][i] = chr(cnt)
            cnt += 1
            if cnt > ord('Z'):
                cnt = ord('A')

for character in characters:
    print(' '.join(character))