# 로또의_최고_순위와_최저_순위

def solution(lottos, win_nums):
    answer = []
    x = lottos.count(0)
    cnt = 0
    for i in win_nums:
        if i in lottos:
            cnt += 1
    ans = 6
    if cnt == 6:
        ans = 1
    elif cnt == 5:
        ans = 2
    elif cnt == 4:
        ans = 3
    elif cnt == 3:
        ans = 4
    elif cnt == 2:
        ans = 5

    if ans - x > 0:
        answer.append(ans-x)
    else:
        answer.append(1)
    answer.append(ans)
        
    return answer