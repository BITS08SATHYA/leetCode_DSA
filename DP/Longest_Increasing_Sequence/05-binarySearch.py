def lengthOfLIS(nums):

    #

    def binarySearch(sub, num):
        left,right = 0, len(sub)-1
        while left < right:
            mid = (left+right)//2
            if sub[mid] < num:
                left = mid + 1
            else:
                right = mid

        return left

    sub = [nums[0]]
    n = len(nums)

    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            index = binarySearch(sub, num)
            sub[index] = num
    return len(sub)


nums = [1,2,3]
print(lengthOfLIS(nums))