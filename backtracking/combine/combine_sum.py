def combinationSum(candidates, target):
    res = []
    n = len(candidates)
    def helper(start_index, curr, sum_included):
        if sum_included > target:
            return
        if sum_included == target:
            res.append(curr[:])
            return
        # recursive case
        for j in range(start_index, n):
            curr.append(candidates[j])
            helper(j, curr, sum_included + candidates[j])
            curr.pop()
    helper(0, [], 0)
    return res

print(combinationSum([2,3,6,7], 7))