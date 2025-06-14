from anytree import Node, RenderTree

def recursion(nums):
    n = len(nums)

    def helper(curr_index, prev_index, parent=None):
        node_label = f"({curr_index},{prev_index})"
        node = Node(node_label, parent=parent)

        if curr_index > n - 1:
            return node  # Just return the leaf node

        # Option 1: Exclude current element
        helper(curr_index + 1, prev_index, node)

        # Option 2: Include current element if valid
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
            helper(curr_index + 1, curr_index, node)

        return node

    root = helper(0, -1)

    # Print the recursion tree
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")

    return root


# Example usage
nums = [1, 2, 3]
recursion(nums)
