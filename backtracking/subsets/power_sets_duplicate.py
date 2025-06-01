def subsetsWithDup(nums):
    res = []
    def helper(i, curr):
        if i == len(nums):
            res.append(curr[:])
            return
        # include
        curr.append(nums[i])
        helper(i+1, curr)
        curr.pop()  # backtracking
        # exclude
        while i < len(nums)-1 and nums[i] == nums[i+1]:
            i += 1
        helper(i+1, curr)
    helper(0, [])
    return res

print(subsetsWithDup([1,3, 3,7]))
