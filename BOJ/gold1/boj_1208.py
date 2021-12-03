# 1208. 부분수열의 합 2

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 절반 나눠서 모든 합 경우의 수 생성
m = n//2
n -= m

arr1 = [0] * (1 << n)
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            arr1[i] += arr[j]

arr2 = [0] * (1 << m)
for i in range(1 << m):
    for j in range(m):
        if i & (1 << j):
            arr2[i] += arr[j+n]

# 두 배열 모두 오름차순 정렬
arr1.sort()
arr2.sort()

n = (1 << n)
m = (1 << m)

left, right = 0, m-1
ans = 0
while left < n and right >= 0:
    temp = arr1[left] + arr2[right]
    if temp < s:  # s보다 작으면 left +1
        left += 1
    elif temp > s:  # s보다 크면 right -1
        right -= 1
    elif temp == s:  # 같으면
        # 3 0
        # 0 0 0 같은 경우가 있기 때문에 합이 연속으로 같은 경우 계산
        x = y = 1  # x : arr1 연속으로 같은 개수, y: arr2 연속으로 같은 개수
        l, r = left, right
        left += 1
        while left < n and arr1[l] == arr1[left]:
            x += 1
            left += 1

        right -= 1
        while right >= 0 and arr2[r] == arr2[right]:
            y += 1
            right -= 1

        ans += x * y

# 0,0인 경우 제외
if s == 0:
    ans -= 1

print(ans)
