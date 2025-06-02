def combination_3(candidates, target):
    candidates.sort()
    res = []
    n = len(candidates)
    def helper(start_index, curr, sum_included):
        if sum_included > target:
            return
        if sum_included == target:
            res.append(curr[:])
            return
        if start_index > n-1:
            return
        # recursive case
        hash = {}
        for j in range(start_index, n):
            if candidates[j] not in hash:
                hash[candidates[j]] = True
                curr.append(candidates[j])
                helper(j+1, curr, sum_included + candidates[j])
                curr.pop()
    helper(0, [], 0)
    return res

print(combination_3([2,3,6,7], 7))