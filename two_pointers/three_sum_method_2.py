def three_sum(nums):
    res = set()
    for i in range(len(nums)):
        need = set()
        for j in range(i+1, len(nums)):
            valueNeeded = - (nums[i] + nums[j])
            if valueNeeded in need:
                triplet = tuple(sorted((nums[i], nums[j], valueNeeded)))
                res.add(triplet)
            need.add(nums[j])
    return [list[triplet] for triplet in res]

list = [4,0,6,2,-2,5]
print(three_sum(list))