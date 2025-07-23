class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# in order traversal
# left - root - right

def inorderTraversal(root):
    res = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


node = TreeNode(1)
node.right = TreeNode(2)
node.left = TreeNode(3)

print(inorderTraversal(node))