# 11742. 트리의 전위순회

def preorder(node):
    if not node:
        return
    res.append(node)
    nums = AL.get(node)
    if nums:
        if len(nums) == 2:
            preorder(nums[0])
            preorder(nums[1])
        else:
            preorder(nums[0])


n = int(input())
tree = list(map(int, input().split()))
AL = {}
for i in range(len(tree) // 2):
    if AL.get(tree[2 * i]):
        AL[tree[2 * i]].append(tree[2 * i + 1])
    else:
        AL[tree[2 * i]] = [tree[2 * i + 1]]

res = []
preorder(1)
print('-'.join(map(str, res)))
