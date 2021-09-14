# 12782. 비트 우정지수

t = int(input())
for _ in range(t):
    n, m = input().split()
    x = y = 0
    for i in range(len(n)):
        if n[i] != m[i]: # 비트가 다르고,
            if int(n[i]): # 1인경우
                x += 1
            else: # 0인경우
                y += 1
    print(max(x, y)) # 둘중 최댓값 출력