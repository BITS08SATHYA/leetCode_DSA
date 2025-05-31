def permute_w_duplicates(nums):
    res = []
    def helper(i):
        if i == len(nums) - 1:
            res.append(nums[:])
            return
        # recursive case
        hash = {}
        for j in range(i, len(nums)):
            if nums[j] not in hash:
                hash[nums[j]] = True
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
    helper(0)
    return res

print(permute_w_duplicates([1,1,3]))