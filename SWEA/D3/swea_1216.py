# 1216. 회문2

import sys

sys.stdin = open('swea_1216.txt')


def is_pallindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


def count_pallindrome(words, length):
    for word in words:
        for i in range(len(word) - length + 1):
            if is_pallindrome(word[i: i + length]):
                return True


T = 10

for tc in range(1, 1 + T):
    m = input()

    data = [input() for _ in range(100)]
    data2 = list(zip(*data))

    for n in range(100, 1, -1):

        if count_pallindrome(data, n) or count_pallindrome(data2, n):
            print('#{} {}'.format(m, n))
            break
