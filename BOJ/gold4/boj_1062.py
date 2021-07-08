# 1062. 가르침
import sys
input = sys.stdin.readline

# lev: 고른 갯수, s: 시작지점, x: 고른 숫자 비트연산 결과


def check(lev, s, x, all_word):
    global ans
    if lev == k:
        cnt = 0
        for i in range(n):
            # & 연산 결과 checking과 같으면 읽을 수 있는 단어
            if checking[i] & x == checking[i]:
                cnt += 1
        ans = max(ans, cnt)
        return
    if s > len(all_word):
        return

    # k개 배우기
    for j in range(s, len(all_word)):
        if all_word[j] not in (0, 2, 8, 13, 19):
            x |= (1 << all_word[j])
            check(lev+1, j+1, x, all_word)
            x &= ~(1 << all_word[j])


n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]

# 처음 배우는 수 a기준으로 비트마스킹
# a,c,i,n,t = 0,2,8,13,19
learn = 0
learn |= (1 << 0) | (1 << 2) | (1 << 8) | (1 << 13) | (1 << 19)
checking = [learn] * n

# 전체 나오는 알파벳 중복제거해서 저장
all_words = set()
all_words.update((0, 2, 8, 13, 19))

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    for i in range(n):
        chk = learn
        for w in words[i]:
            if ord(w) not in (0, 2, 8, 13, 19):
                chk |= (1 << (ord(w) - ord('a')))
                all_words.add(ord(w) - ord('a'))
        # 입력받은 단어 or 연산해서 저장
        checking[i] = chk

    # 전체 단어의 수보다 선택하는 k의 수가 더 크면 n개 전부 가능
    if k >= len(all_words):
        print(n)
    else:
        ans = 0
        check(5, 0, learn, sorted(list(all_words)))  # 5개는 고정이므로 5부터 시작
        print(ans)
