# 2857: 세로읽기

words = [[''] *15 for _ in range(15)]
for i in range(5):
    w = input()
    for j in range(len(w)):
        words[j][i] = w[j]

res = ''
for word in words:
    res += ''.join(word)

print(res)