def maxFrequency(nums, k):
    nums.sort()
    left = 0
    total = 0
    res = 0
    for right in range(len(nums)):
        total += nums[right]
        # 2 possiblities
        # nums[right] * (right-left+1) = A
        # total of window + k = B
        # 1. A > B --> Invalid window --> reduce the size of window --> left pointer
        # 2. A = B --> Valid window --> right pointer (increasing the window)
        # ...3,3
        # 3. A < B --> valid window --> increase size of the window --> right pointer
        while nums[right] * (right-left+1) > total + k:
            total -= nums[left]
            left += 1
        # valid window
        res = max(res, right - left + 1)
    return res

nums = [2,2,2,3,3,7]
print(maxFrequency(nums, 2))




















