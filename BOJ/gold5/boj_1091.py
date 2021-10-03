# 1091. 카드 섞기

import sys
input = sys.stdin.readline


def check():  # 카드가 맞게 갔는지 체크
    for i in range(n):
        if p[cards[i]] != i % 3:
            return False
    return True


n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
cards = list(range(n))
chk_list = list(range(n)) # 초기값과 비교할 리스트

cnt = 0
while True:
    if check():
        print(cnt)
        break

    temp = cards.copy()
    for i in range(n):
        cards[s[i]] = temp[i]

    # 처음 시작한 list와 같으면 종료
    if cards == chk_list:
        print(-1)
        break

    cnt += 1