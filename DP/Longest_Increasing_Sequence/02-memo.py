def memo(nums):

    n = len(nums)
    dp = [[-1]*n for _ in range(n)]

    def helper(curr_index, prev_index):
        # base case
        if curr_index > n - 1:
            return 0
        if dp[curr_index][prev_index+1] != -1:
            return dp[curr_index][prev_index+1]
        # recursive case
        exclude = helper(curr_index + 1, prev_index)
        include = 0
        if prev_index == -1 or nums[curr_index] > nums[prev_index]:
            include = 1 + helper(curr_index+1, curr_index)
        dp[curr_index][prev_index+1] = max(exclude, include)
        return dp[curr_index][prev_index+1]
    return helper(0, -1)



nums = [1,2,3]
print(memo(nums))