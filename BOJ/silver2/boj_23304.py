# 23304. 아카라카

import sys
input = sys.stdin.readline

s = input().rstrip()


def is_pallindrome(x):
    l = len(x)
    if l == 1:
        return True
    elif l > 1 and x != x[::-1]:
        return False
    else:
        return is_pallindrome(x[:l//2])


if is_pallindrome(s):
    print('AKARAKA')
else:
    print('IPSELENTI')
