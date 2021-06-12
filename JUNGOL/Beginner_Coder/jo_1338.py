# 1338. 문자삼각형1

'''
        A
      B F
    C G J
  D H K M
E I L N O
'''
# N = 5
N = int(input())
arr = [[' ' for _ in range(N)] for _ in range(N)]
start = ord('A')
for i in range(N):
    k = N
    for j in range(i,N):
        k -= 1
        arr[j][k] = chr(start)
        start += 1
        if start > 90:
            start = 65
for a in arr:
    print(' '.join(a))


