# 복서 정렬하기

def solution(weights, head2head):
    answer = []
    for i in range(len(head2head)):
        win = cnt = 0
        length = len(head2head) - head2head[i].count('N')
        if length == 0:
            answer.append((i+1, cnt, 0, weights[i]))
            continue
        for j in range(len(head2head)):
            if head2head[i][j] =='W':
                win += 1
                if weights[i] < weights[j]:
                    cnt += 1
                    
        answer.append((i+1, cnt, win/length, weights[i]))
        
    answer = sorted(answer, key=lambda x: (-x[2], -x[1], -x[3]))
    return [answer[i][0] for i in range(len(answer))]