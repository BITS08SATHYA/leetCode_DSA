def findRepeatedDnaSequence(s):
    L = 10
    n = len(s)

    seen, output = set(), set()

    for start in range(n-L+1):
        # n = 20, L = 10 first sequence index 0 to index 9 ; last sequence index 10(20-10) to index 19
        temp = s[start:start+L]
        if temp in seen:
            # repeating pattern
            output.add(temp[:])
        seen.add(temp)

    return list(output)