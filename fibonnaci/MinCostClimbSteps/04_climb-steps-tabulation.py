def minCostClimbSteps(cost):
    n = len(cost)
    minCost = [0] * (n + 1)

    minCost[0] = 0
    minCost[1] = 0

    for i in range(2, n+1):
        oneStep = cost[i-1] + minCost[i-1]
        twoStep = cost[i-2] + minCost[i-2]
        minCost[i] = min(oneStep, twoStep)
    return minCost[n]

