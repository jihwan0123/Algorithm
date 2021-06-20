# 2514: 문자열 찾기

words = input()
koi = ioi = 0
for i in range(len(words)-2):
    if words[i:i+3] == 'KOI':
        koi += 1
    if words[i:i+3] == 'IOI':
        ioi += 1

print(koi)
print(ioi)