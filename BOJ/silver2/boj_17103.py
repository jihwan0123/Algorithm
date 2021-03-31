# 17103. 골드바흐 파티션

# 에라토스테네스의 체
primes = []
check = [0] * 1000001
for i in range(2,1000001):
    if check[i] == False:
        primes.append(i)
        for j in range(2*i, 1000000, i):
            check[j] = True



T = int(input())
for tc in range(T):
    n = int(input())
    ans = 0
    for x in primes:
        y = n - x
        if x <= y and check[y] == False:
            ans += 1
        if y < x:
            break

    print(ans)