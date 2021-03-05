# 1213. String

import sys

sys.stdin = open('swea_1213.txt', 'rt', encoding='utf-8')


def find_word(word, words):
    n1 = len(word)
    n2 = len(words)
    idx, cnt = 0, 0

    while idx < n2:
        if word == words[idx:idx + n1]:
            idx += n1
            cnt += 1
            if idx >= n2:
                return cnt
        else:
            idx += 1
    return cnt


for tc in range(1, 11):
    a = int(input())
    f_str = input()
    input_str = input()

    result = find_word(f_str, input_str)

    print('#{} {}'.format(a, result))
