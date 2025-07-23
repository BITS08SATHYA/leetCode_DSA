class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    # write code here
    res = []
    def helper(node, curr, rem_sum):
        # base case
        if node is None:
            return
        # recursive case
        curr.append(node.val)
        if rem_sum == node.val and node.right is None and node.left is None:
            res.append(curr[:])
        else:
            helper(node.left, curr, rem_sum-node.val)
            helper(node.right, curr, rem_sum-node.val)
        curr.pop() # backtracking

    helper(root, [], targetSum)
    return res

node = TreeNode(7)

# first half
node.left = TreeNode(3)
node.left.left = TreeNode(6)
node.left.right = TreeNode(5)
node.left.right.right = TreeNode(5)

# second half
node.right = TreeNode(6)
node.right.left = TreeNode(1)
node.right.right = TreeNode(4)
node.right.right.left = TreeNode(2)
node.right.right.right = TreeNode(3)

print(pathSum(node, 20))