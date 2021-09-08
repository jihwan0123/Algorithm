def solution(board, moves):
    answer = 0
    length = len(board)
    stack = []
    for move in moves:
        for i in range(length):
            if board[i][move-1]:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if len(stack) >= 2 and (stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))