def knapsack(W, wt, val, n):

    dp = [[0]*(W+1) for _ in range(n+1)]

