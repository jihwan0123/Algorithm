# 2661. 좋은 수열

def dfs(n, s):
    global chk
    # 좋은수열인지 체크
    for i in range(len(s)):
        for j in range(i+2, len(s)):
            if s[i:j] == s[j:2*j-i]:
                return
    # 하나 결과 나왔으면 종료
    if chk:
        return
    # 결과 출력
    if n == 1:
        print(s)
        chk = True
        return

    # dfs 1,2,3 순서대로 돌면서 최솟값 먼저 구한다.
    for i in range(1, 4):
        if s[-1] != str(i):
            dfs(n-1, s+str(i))


chk = False
dfs(int(input()), "1")
