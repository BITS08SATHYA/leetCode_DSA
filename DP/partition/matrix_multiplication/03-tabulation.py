def tabulation(N,arr):

    dp = [[0]*N for _ in range(N)]

    for l in range(1,N+1):
        for i in range(1, N-l+1):
            j = i + l - 1
            if i == j: dp[i][j] = 0
            else:
                cost = float('inf')
                for k in range(1,j):
                    new_cost = dp[i][j] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    cost = min(cost, new_cost)
                dp[i][j] = cost
    return dp[1][N-1]



arr1 = [2,10,5,4]
print(tabulation(4, arr1))