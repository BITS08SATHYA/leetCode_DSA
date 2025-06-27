def wordbreak_rec(s, wordDict):
    n = len(s)
    dp = [-1]*n

    def check_ending_at(index):
        # base case
        if index < 0:
            return True
        if dp[index] != -1:
            return index

        # recursive case
        for word in wordDict:
            if (s[index-len(word)+1:index+j] == word and
                    check_ending_at(index-len(word))):
                dp[index] = True
                return dp[index]
        dp[index] =False
        return dp[index]


    return check_ending_at(n-1)