def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def partition(array, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    # Finding middle takes O(1)
    middle = (start + end) // 2
    swap(array, start, middle)

    pivot = array[start]
    i = start + 1
    j = end

    while i <= j:
        # in worst cas scenario, this can take O(n)
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i < j:
            swap(array, i, j)

    # This swap is O(1)
    swap(array, start, j)
    return j

def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    while start < end:
        pivot_idx = partition(array, start, end)

        # Recursively call Quick sort on lower sized subArray
        # Each recursion takes O(log(n)) in best case scenario and O(n) in worst case
        if pivot_idx - start < end - pivot_idx:
            quick_sort(array, start, pivot_idx - 1)
            start = pivot_idx + 1
        else:
            quick_sort(array, pivot_idx + 1, end)
            end = pivot_idx - 1

    return array


arr = [6,3,1,9,5]
print(quick_sort(arr, 0, len(arr)-1))