class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) != len(word2):
            return "word length doesn't match"

        for i in range(len(word1)):
            print(word1[i],word2[i] , end="")
            # print(word2[i])
        return None


str1 = 'abc'
str2 = 'pqr'

sol = Solution()
sol.mergeAlternately(str1, str2)