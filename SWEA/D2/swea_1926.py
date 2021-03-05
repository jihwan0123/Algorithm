# 1926. 간단한 369 게임
N = int(input())

num = [3, 6, 9]
arr = [str(i) for i in range(1, N + 1)]  # 1 2 3 4 ... N

for i in range(N):  # 1 부터 N까지 반복한다.
    result = ''  # 3,6,9 나올때 - 출력할 문자열
    for j in arr[i]:  # arr 숫자들 반복
        if int(j) in num:  # 각 자리수가 3,6,9이면
            result += '-'  # 3,6,9 나온만큼 -를 더하고
            arr[i] = result  # 더한 문자열로 교체한다.

print(' '.join(arr))
