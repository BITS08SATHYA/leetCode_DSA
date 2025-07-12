def search_rotated_sorted_array(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target: return middle
        if nums[left] <= nums[middle]:
            # left part is sorted
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            # right part is sorted
            if nums[right] >= target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
    return -1

print(search_rotated_sorted_array([7,8,1,2,3,4,5,6], 3))
