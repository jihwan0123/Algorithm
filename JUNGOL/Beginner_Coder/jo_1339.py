# 1339:문자삼각형2

N = int(input())
arr = [[' ' for _ in range(N)] for _ in range(N)]
start = ord('A')

if N < 1 or N > 100 or (N % 2 == 0):
    print('INPUT ERROR')
else:
    for i in range(N//2, -1, -1):
        k = (N//2)*2-i
        for j in range(i, k+1):
            arr[j][i] = chr(start)
            start += 1
            if start > 90:
                start = 65

    for i in range(N):
        print(' '.join(arr[i]))
