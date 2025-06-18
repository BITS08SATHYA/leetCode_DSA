def memo(N,arr):

    dp = [[-1]*N for _ in range(N)]

    def findCost(i,j):
        # base case
        if i == j:
            return 0

        # recursive case
        if dp[i][j] != -1:
            return dp[i][j]
        cost = float('inf')
        for k in range(i,j):
            curr_cost = findCost(i,k) + findCost(k+1,j) + arr[i-j]*arr[k]*arr[j]
            cost = min(cost,curr_cost)
        dp[i][j] = cost
        return dp[i][j]

    return findCost(1, N-1)


arr1 = [2,10,5,4]
print(memo(4, arr1))