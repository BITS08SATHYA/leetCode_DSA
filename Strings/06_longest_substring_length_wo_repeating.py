def max_unique_length(str):
    max_len = 0
    start = 0
    seen = {}

    for i in range(len(str)):
        char = str[i]
        if char in seen:
            start = max(start, seen[char] + 1)
        max_len = max(max_len, i-start + 1)
        seen[char] = i
    return max_len

print(max_unique_length("pqbrstbuvwpvy"))

print(max_unique_length("abc"))