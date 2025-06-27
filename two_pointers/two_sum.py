def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


list = [1,2,5,7,9,11,14]
target = 11
print(two_sum(list, target))