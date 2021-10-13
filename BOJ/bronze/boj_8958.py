# 8958. OX퀴즈

n = int(input())
for _ in range(n):
    ans = 0
    results = input()
    cnt = 0
    for r in results:
        if r == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    
    print(ans)