# 11729. 하노이 탑 이동 순서

def hanoi(n, before, mid, after):
    if n == 0:
        return

    hanoi(n-1, before, after, mid)
    ans.append((before, after))
    hanoi(n-1, mid, before, after)


ans = []
hanoi(int(input()), 1, 2, 3)
print(len(ans))
for a in ans:
    print(*a)
