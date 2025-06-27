def max_area(arr):
    max_area = 0
    left = 0
    right = len(arr)-1
    while left < right:
        area = min(arr[left], arr[right]) * (right - left)
        max_area = max(area, max_area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_area([3,7,5,6,8,4]))