def longestCommonSubsequence_tab(text1, text2):
    n = len(text1)
    m = len(text2)
    prev = [0] * (m+1)
    curr = [0] * (m+1)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if text1[i-1] == text2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr[:]
    return curr[m]



str1 = 'abcdef'
str2 = 'acef'
print(longestCommonSubsequence_tab(str1, str2))