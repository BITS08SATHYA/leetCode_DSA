def findMaxAvg(nums, k):
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for i in range(k, len(nums)):
        curr_sum += curr_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum / k


print(findMaxAvg([1, 13, -6,-3,40,2], 4))