def canJump(nums):
    n = len(nums)
    max_index = 0
    for i in range(n):
        if i > max_index: return False
        max_index = max(max_index, i+nums[i])
        if max_index >= n -1:
            return True
    return False


print(canJump([1, 2, 3]))