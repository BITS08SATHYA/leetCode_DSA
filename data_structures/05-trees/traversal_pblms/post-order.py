class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Post order traversal
# left - right - root
def postOrderTraversal(root):
    stack = [root]
    visited = [False]
    res = []
    while stack:
        curr = stack.pop()
        visit = visited.pop()
        if curr:
            if visit:
                res.append(curr.val)
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right)
                visited.append(False)
                stack.append(curr.left)
                visited.append(False)
    return res

node = TreeNode(1)
node.right = TreeNode(2)
node.left = TreeNode(3)

print(postOrderTraversal(node))