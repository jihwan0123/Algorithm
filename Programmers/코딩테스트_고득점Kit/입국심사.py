# 입국심사

def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n + 1

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid//time

        if cnt >= n:
            right = mid - 1
            answer = mid

        else:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
