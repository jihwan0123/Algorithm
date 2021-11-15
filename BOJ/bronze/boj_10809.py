# 10809. 알파벳 찾기

alphabet = input()

for i in range(ord('a'), ord('z')+1):
    print(alphabet.find(chr(i), 0), end=' ')
