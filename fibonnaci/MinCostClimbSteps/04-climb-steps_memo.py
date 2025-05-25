def minCostClimbStairs(cost):
    n = len(cost)
    minCost = [-1] * n

    def helper(index):
        # return the cost for reaching the top starting from step - index
        # base case
        if index > n - 1:
            return 0
        # recursive case
        if minCost[index] != -1:
            return minCost[index]
        # one step
        oneStep = cost[index] + helper(index + 1)

        # twostep
        twoStep = cost[index] + helper(index + 2)

        minCost[index] = min(oneStep, twoStep)
        return minCost[index]

    return min(helper(0),helper(1))

# Memoization approach