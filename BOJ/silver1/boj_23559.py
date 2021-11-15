# 23559. 밥
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
menus = []
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    # 전부 1000원짜리를 구매했다고 가정
    ans += b
    x -= 1000
    if a - b > 0:
        menus.append(a-b)

# a-b의 차이를 내림차순으로 정렬
menus.sort(reverse=True)

# 5000원 메뉴와 1000원 메뉴 차이가 큰 것 부터 바꿔본다.
for i in range(len(menus)):
    # 4000원보다 작으면 종료
    if x < 4000:
        break
    x -= 4000
    ans += menus[i]

print(ans)
