def targetSum(array, target, list):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                list.append((i,j))
                # return (i,j)
    return list


array = [3,5,8,6]
tv = 11
list = []
print(targetSum(array, tv, list))