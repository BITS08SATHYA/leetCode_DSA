def minDistance_memo(word1, word2):

    n = len(word1)
    m = len(word2)
    dp = [[-1]*m for _ in range(n)]
    def helper(index1, index2):
        # base case
        if index1 > n-1 and index2 > m-1:
            return 0
        if index1 > n-1:
            return m - index2
        if index2 > m - 1:
            return n - index1

        if dp[index1][index2] != -1:
            return dp[index1][index2]

        # recursive case
        if word1[index1] == word2[index2]:
            dp[index1][index2] = helper(index1+1, index2+1)
        else:
            replace = 1 + helper(index1+1, index2+1)
            delete = 1 + helper(index1+1, index2)
            insert = 1 + helper(index1, index2+1)
            dp[index1][index2] = min(replace, delete, insert)
        return dp[index1][index2]
    return helper(0,0)