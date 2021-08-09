# 실패율

def solution(N, stages):
    
    answer = []
    total = len(stages)
    for i in range(1, 1 + N):
        cnt = stages.count(i)
        if total == 0:
            failure = 0
        else:
            # 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
            failure = cnt/total # stages >= 1
        answer.append((i,failure))
        total -= cnt
    
    answer = [a[0] for a in sorted(answer, key=lambda x:-x[1])]
    
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))