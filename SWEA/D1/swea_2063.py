# statistics 모듈 사용
# import statistics
# T = int(input()) # input 갯수

# tc = input()
# num = list(map(int,tc.split()))
# print(f'{statistics.median(num)}')


T = int(input())  # input 갯수

tc = input()
num = list(map(int, tc.split()))
num.sort()

print(f'{num[len(num) // 2]}')
