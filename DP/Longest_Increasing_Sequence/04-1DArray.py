def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * (n)

    max = 1

    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
        if dp[i] > max: max = dp[i]
    return max

nums = [1,2,3]
print(lengthOfLIS(nums))