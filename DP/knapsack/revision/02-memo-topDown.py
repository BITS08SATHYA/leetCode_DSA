# 2 Memoization (Top Down approach)

def knapsnack_memo(W, wt, val, n):
    # Write code here
    dp =[[-1]*(W+1) for _ in range(n)]

    def helper(index, rem_weight):
        # base case
        if index > n - 1 or rem_weight == 0:
            return 0
        if dp[index][rem_weight] != -1:
            return dp[index][rem_weight]

        # recursive case
        exclude = helper(index + 1, rem_weight)
        include = 0

        if wt[index] <= rem_weight:
            include = val[index] + helper(index + 1, rem_weight - wt[index])
        dp[index][rem_weight] = max(exclude, include)
        print(f'{index}-{wt[index]} - {dp[index][rem_weight]}')
        return dp[index][rem_weight]

    result = helper(0, W)

    print("\nMemoization Table (dp):\n")
    print("     ", end="")
    for w in range(W + 1):
        print(f"{w:>4}", end="")
    print()
    for i in range(n):
        print(f"I{i + 1:<3} ", end="")
        for w in range(W + 1):
            print(f"{dp[i][w]:>4}", end="")
        print()
    return result

knapsnack_memo(8,[8,2,5], [2,3,9], 3)
















