# 23783. Ресторан

import sys
input = sys.stdin.readline

word = input().rstrip()

sounds = {
    'B': 'v',
    'E': 'ye',
    'H': 'n',
    'P': 'r',
    'C': 's',
    'Y': 'u',
    'X': 'h'
}
for s in sounds:
    word = word.replace(s, sounds[s])
print(word.lower())
