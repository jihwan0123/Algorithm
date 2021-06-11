# 2629. 양팔저울

'''
2
1 4
2
3 2
'''
'''
Y N
'''

def dfs(lev, weightSum):
    # 같은 횟수에 같은 무게면 pass
    if memo[lev][weightSum] == 1:
        return
    # 아니면 메모
    memo[lev][weightSum] = 1
    # 무게 전부 사용했으면 종료
    if lev == n:
        return
    # +, 0, - 반복
    dfs(lev+1, weightSum+weights[lev])
    dfs(lev+1, weightSum)
    dfs(lev+1, abs(weightSum-weights[lev]))


n = int(input())
weights = list(map(int, input().split()))
x = int(input())
find_nums = list(map(int,input().split()))

memo = [[0 for _ in range(40001)] for _ in range(n+1)]
dfs(0, 0)

for find_num in find_nums:
    if memo[n][find_num]:
        print('Y', end=' ')
    else:
        print('N', end=' ')