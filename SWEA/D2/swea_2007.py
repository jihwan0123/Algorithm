# 2007. 패턴 마디의 길이

T = int(input())

for tc in range(1, 1 + T):  # test case 반복
    words = input()  # tc 입력: KOREAKOREAKOREAKOREAKOREAKOREA
    cnt = 0
    for i in range(1, len(words) + 1):
        if words[0:i] == words[i:2 * i]:
            cnt = i
            # print(cnt)
            break
        else:
            pass
    print('#{} {}'.format(tc, cnt))
