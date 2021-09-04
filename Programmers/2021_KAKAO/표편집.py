# 정확성 30/30, 효율성 5/10
'''
def solution(n, k, cmd):
    check = ['O'] * n
    cur = k
    stack = [0] * n
    stack_idx = -1
    for c in cmd:
        method = c.split()
        if method[0] == 'U':
            x = int(method[1])
            while x:
                cur -= 1
                if check[cur] == 'O':
                    x -= 1

        elif method[0] == 'D':
            x = int(method[1])
            while x:
                cur += 1
                if check[cur] == 'O':
                    x -= 1
            
        elif method[0] == 'C':
            check[cur] = 'X'
            stack_idx += 1
            stack[stack_idx] = cur
            x = y = cur
            chk = 1
            while x < n - 1:
                x += 1
                if check[x] == 'O':
                    cur = x
                    chk = 0
                    break
            if chk:
                while y > 0:
                    y -= 1
                    if check[y] == 'O':
                        cur = y
                        break

        elif method[0] == 'Z':
            x = stack[stack_idx]
            stack[stack_idx] = 0
            stack_idx -= 1
            check[x] = 'O'

    answer = ''.join(check)

    return answer
'''

# linked list
def solution(n, k, cmd):
    class Node:
        def __init__(self):
            self.removed = "O"
            self.prev = None
            self.next = None

    linked_list = [Node() for i in range(n)] # n개의 노드 생성

    # 각 노드 연결
    for i in range(1, n):
        linked_list[i].prev = linked_list[i-1]
        linked_list[i-1].next = linked_list[i]

    # 시작 노드 설정
    k = linked_list[k]
    stack = []
    for c in cmd:
        if c[0] == 'U':  # 위로 이동
            for _ in range(int((c[2:]))):
                k = k.prev

        elif c[0] == 'D':  # 아래로 이동
            for _ in range(int((c[2:]))):
                k = k.next

        elif c[0] == 'C':  # 삭제
            # 삭제한 값 저장
            stack.append(k)
            # removed 처리
            k.removed = "X"
            # 삭제한 노드의 이전값, 이후값
            prev_node = k.prev
            next_node = k.next
            # 이전값이 있으면 연결
            if prev_node:
                prev_node.next = next_node
            # 다음값이 있으면 연결 후 아래행으로 이동
            if next_node:
                next_node.prev = prev_node
                k = next_node
            else: # 없으면, 마지막 행이므로 바로 윗행 선택
                k = prev_node

        elif c[0] == 'Z':  # 복구
            # 제일 최근에 삭제한 노드 복구
            node = stack.pop()
            node.removed = "O"
            # 앞, 뒤 연결된 노드 다시 연결
            prev_node = node.prev
            next_node = node.next
            if prev_node:
                prev_node.next = node
            if next_node:
                next_node.prev = node

    return ''.join([node.removed for node in linked_list])


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
# OOOOXOOO
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
# OOXOXOOO
