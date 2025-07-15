def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # step 1
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # recrusive left call
    right_half = merge_sort(arr[mid:]) # recursive right call

    # step 2: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    # compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [7,3,8,5,1,9,5]
sorted_arr = merge_sort(arr)
print(sorted_arr)