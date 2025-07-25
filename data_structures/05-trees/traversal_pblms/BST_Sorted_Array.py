class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def buildBSTfromSortedArray(nums, left = 0, right = None):
    if right is None:
        right = len(nums) - 1

    # base case
    if left > right:
        return None

    middle = (left + right) // 2

    node = Node(nums[middle])

    node.left = buildBSTfromSortedArray(nums, left, middle - 1)
    node.right = buildBSTfromSortedArray(nums, middle + 1, right)


    return node