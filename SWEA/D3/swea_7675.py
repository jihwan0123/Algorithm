# 7675. 통역사 성경이

import sys

sys.stdin = open('swea_7675.txt')

'''
result = []
for tc in range(1, 1 + int(input())):
    n = int(input())
    words = input()
    words = words.replace('.', ',.').replace('!', '!.').replace('?', '?.').split('.')
    names = [n.strip() for n in words if n]
    res = []
    for name in names:
        cnt = 0
        i = name.split()
        for j in i:
            if j[0].isupper() and j[1:len(j) - 1].islower():
                cnt += 1

        if i[-1][-1] == ',' and i[-1][1:len(i) - 1].isalpha():
            cnt -= 1

        res.append(cnt)
    result.append('#{} {}'.format(tc, ' '.join(map(str, res))))
print('\n'.join(result))
'''
op = {
    '!': True,
    '?': True,
    '.': True
}

for tc in range(1, 1 + int(input())):
    n = int(input())
    sentence = input()
    ans = []
    start = 0
    for i in range(len(sentence)):
        # 구분기호 만나면 True
        if op.get(sentence[i], False):
            cnt = 0
            for word in sentence[start:i].split():
                # 맨 앞이 대문자이고, 뒤에는 알파벳이면서 소문자면 이름
                if (len(word) == 1 and word.isupper()) or\
                        (word[0].isupper() and word.isalpha() and word[1:].islower()):
                    cnt += 1

            # index : 구분문자 다음으로
            start = i + 1
            ans.append(cnt)

    print('#{} {}'.format(tc, ' '.join(map(str, ans))))
