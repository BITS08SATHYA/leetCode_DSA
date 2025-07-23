class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# pre - order traversal
# root - left - right

def preOrderTraversal(root):
    res = []
    stack = [root]

    if root is None: return res

    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res

node = TreeNode(1)
node.right = TreeNode(2)
node.left = TreeNode(3)

print(preOrderTraversal(node))