def max_area(arr):
    max_area = 0
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            area = min(arr[i], arr[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area

print(max_area([3,7,5,6,8,4]))