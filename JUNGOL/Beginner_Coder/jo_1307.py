# 1307: 문자사각형1

n = int(input())
cnt = ord('A')
x = cnt + (n**2 % 26) - 1
characters = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        characters[j][i] = chr(x)
        x -= 1
        if x < cnt:
            x = ord('Z')

for character in characters:
    print(' '.join(character))