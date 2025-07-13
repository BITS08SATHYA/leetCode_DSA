def bubble_sort(array):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted = False
        counter += 1
    return array



array = [2,3,7,1,8]
print(bubble_sort(array))