# 1215. 회문1

import sys

sys.stdin = open('swea_1215.txt')


def is_pallindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


def find_pallindrome(words, text):
    cnt = 0
    for word in words:
        for i in range(len(word) - text + 1):
            w = word[i: i + text]
            if is_pallindrome(w):
                cnt += 1
    return cnt


T = 10

for tc in range(1, 1 + T):
    m = int(input())
    data = [list(input()) for _ in range(8)]
    data2 = list(zip(*data))

    a = find_pallindrome(data, m)
    b = find_pallindrome(data2, m)

    print('#{} {}'.format(tc, a + b))
