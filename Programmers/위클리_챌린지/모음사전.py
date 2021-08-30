from itertools import product, chain


def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    x = chain.from_iterable(product(words, repeat=i) for i in range(1, 6))
    y = sorted(x)
    answer = y.index(tuple(word))+1
    return answer


print(solution('AAAAE'))
print(solution('AAAE'))
print(solution('I'))
print(solution('EIO'))
