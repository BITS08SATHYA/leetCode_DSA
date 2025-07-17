def radix_sort(array):
    if len(array) == 0:
        return 'empty array'

    # finding max ana dnumber of digits takes O(n)
    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))

    for i in range(number_of_digits):
        counting_sort(array, i)

    return array


def counting_sort(array, place):
    output = [0] * len(array)
    temp = [0] * 10
    digit_place = 10 ** place

    # couting occurences of digits. This is O(n)
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1

    for i in range(1, 10):
        temp[i] += temp[i-1]

    for j in range(len(array) -1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]

    array[:] = output[:]


array = [384,73,374,183,65,247,185]
print(radix_sort(array))