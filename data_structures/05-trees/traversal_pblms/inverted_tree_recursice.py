def invertRecursive(node):
    if node is None:
        return

    temp = node.left
    node.left = node.right
    node.right = temp

    invertRecursive(node.left)
    invertRecursive(node.right)

    return node