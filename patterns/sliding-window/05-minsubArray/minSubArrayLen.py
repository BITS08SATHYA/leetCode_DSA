def minSubArrayLen(target, nums):
    left = 0
    currentSum = 0
    length = float("infinity")
    for right in range(1, len(nums)):
        currentSum += nums[right]
        while currentSum >= target:
            newLength = right - left + 1
            if newLength < length:
                length = newLength
            # left pointer checking another valid window of lower size
            currentSum -= nums[left]
            left += 1
    return length if length != float("infinity") else 0


# nums = [1,3,4,3,5,4]
nums = [5,1,3,5,10,7,4,9,2,8]
print(minSubArrayLen(15, nums))