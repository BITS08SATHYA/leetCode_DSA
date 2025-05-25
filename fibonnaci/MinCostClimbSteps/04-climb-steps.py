def minCostClimbStairs(cost):
    n = len(cost)

    def helper(index):
        # return the cost for reaching the top starting from step - index
        # base case
        if index > n - 1:
            return 0
        # recursive case
        # one step
        oneStep = cost[index] + helper(index + 1)

        # twostep
        twoStep = cost[index] + helper(index + 2)
        return min(oneStep, twoStep)

    return min(helper(0),helper(1))

# Memoization approach