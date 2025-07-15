def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr

arr = [1,8,2,6,4,5]
print(selection_sort(arr))



