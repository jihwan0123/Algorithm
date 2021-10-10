# 20164. 홀수 홀릭 호석

def dfs(sub_num, total):
    global minV, maxV
    # 자른 길이 체크
    n = len(sub_num)
    # 홀수는 끝자리가 1이므로, int(x)&1 이 참이면 홀수
    odd_cnt = sum(map(lambda x: int(x) & 1, sub_num))
    if n == 1:  # 한자리만 남았으면
        # 현재값에 홀수갯수 추가 후 종료
        minV = min(minV, total + odd_cnt)
        maxV = max(maxV, total + odd_cnt)
        return
    if n == 2:  # 두자리면
        # dfs 계속
        dfs(str(int(sub_num[0])+int(sub_num[1])), total + odd_cnt)
    else:
        # 세자리면 세등분 후 dfs
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                n1 = int(sub_num[:i])
                n2 = int(sub_num[i:j])
                n3 = int(sub_num[j:])
                dfs(str(n1+n2+n3), total + odd_cnt)


n = input()
minV, maxV = float('inf'), 0
dfs(n, 0)
print(minV, maxV)
