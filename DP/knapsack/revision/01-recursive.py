def knapsnack(W, wt, val, n):

    def helper(index, rem_weight):

        # base case
        if index > n-1 or rem_weight == 0:
            return 0

        # recursive  case
        exclude = helper(index+1, rem_weight)
        include = 0

        if wt[index] <= rem_weight:
            include = val[index] + helper(index+1, rem_weight - wt[index])
        return max(exclude, include)
    return helper(0,W)

print(knapsnack(8,[8,2,5], [2,3,9], 3))