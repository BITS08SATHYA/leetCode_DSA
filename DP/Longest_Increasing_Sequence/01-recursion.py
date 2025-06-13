def recursion(nums):

    n = len(nums)

    def helper(curr_index, prev_index):
        if curr_index > n - 1:
            return 0
        # recursive case
        exclude = helper(curr_index + 1, prev_index)
        include = 0
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
            include = 1 + helper(curr_index+1, curr_index)
        return max(exclude, include)
    return helper(0, -1)



nums = [1,2,3,4,1,5]
print(recursion(nums))