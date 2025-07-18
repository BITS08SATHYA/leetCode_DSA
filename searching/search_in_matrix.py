def search_in_matri(matrix, target):
    columns = len(matrix[0])
    rows = len(matrix)
    print(f'Rows: {rows}, Columns: {columns}')
    # binary search to identify relevant row
    top = 0
    bottom = rows - 1
    while top <= bottom:
        middle = (top + bottom) // 2
        if target < matrix[middle][0]:
            bottom = middle - 1
        elif target > matrix[middle][columns - 1]:
            top = middle + 1
        else:
            break
    if top > bottom:
        return False
    left = 0
    right = columns - 1
    while left <= right:
        middle_val = (left + right) // 2
        if target == matrix[middle][middle_val]:
            return True
        elif target < matrix[middle][middle_val]:
            right = middle_val - 1
        else:
            left = middle_val + 1
    return False



matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [20,0,40,50]
]
print(search_in_matri(matrix, 40))