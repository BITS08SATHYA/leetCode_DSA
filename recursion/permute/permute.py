def permute(nums):
    n = len(nums)
    res = []
    def helper(index):
        # base case
        if index == n - 1:
            res.append(nums[:])
            return
        for j in range(index, n):
            nums[index], nums[j] = nums[j],nums[index]
            helper(index + 1)
            nums[index], nums[j] = nums[j],nums[index]
    helper(0)
    return res, len(res)

print(permute([1,2,3]))