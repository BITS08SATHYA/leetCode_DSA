def wordbreak_rec(s, wordDict):
    n = len(s)
    dp = [False]*n

    def check_ending_at(index):
        # base case
        if index < 0:
            return True

        # recursive case
        for word in wordDict:
            if (s[index-len(word)+1:index+j] == word and
                    check_ending_at(index-len(word))):
                return True
        return False


    return check_ending_at(n-1)