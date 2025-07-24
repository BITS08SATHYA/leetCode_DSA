from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if root is None:
        return []

    output = []
    queue = deque([root])
    while queue:
        length = len(queue)
        count = 0
        curr_level_values = []

        while count < length:
            curr = queue.popleft()
            curr_level_values.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
        output.append(curr_level_values)

    return output


node = TreeNode(1)
node.right = TreeNode(2)
node.left = TreeNode(3)

print(levelOrder(node))