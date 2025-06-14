from numpy.ma.core import maximum


def maxEnvelopes(envelopes):

     # w - ascending, h - descending ; tabulation
     envelopes.sort(key=lambda x:(x[0], -x[1]))

     # LIS on heights
     n = len(envelopes)
     dp = [1]* n
     maximum = 1
     for i in range(1,n):
         for j in range(i):
             if envelopes[i][1] > envelopes[j][1] and dp[j]+1 > dp[i]:
                 dp[i] = dp[j+1]
         if dp[i] > maximum: maximum = dp[i]
     return maximum


envelopes = [[1,2],[2,9],[4,5]]
print(maxEnvelopes(envelopes))
