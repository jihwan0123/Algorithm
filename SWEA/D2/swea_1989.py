# 1989. 초심자의 회문 검사
def is_pallindrome(word):
    for i in range(len(word)):
        if word[i] == word[len(word) - i - 1]:
            pass
        else:
            return 0
    return 1


T = int(input())

for tc in range(1, T + 1):
    words = input()
    print('#{} {}'.format(tc, is_pallindrome(words)))
