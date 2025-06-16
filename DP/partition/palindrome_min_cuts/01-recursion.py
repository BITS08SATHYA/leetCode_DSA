def min_cuts_pal_recursion(s):

    n = len(s)

    def isPalindrome(i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            return True

    def partitions(start, end):
        # base case
        if start == end or isPalindrome(start, end):
            return 0
        # recursive case
        minimum = end - start
        for end_index in range(start,end):
            if isPalindrome(start, end_index):
                minimum = min(minimum, 1+partitions(end_index+1, end))
        return minimum

    return partitions(0, n-1)

str = 'abcabc'
print(min_cuts_pal_recursion(str))