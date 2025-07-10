def group_anagrams(s):
    if len(s) == 0:
        return []

    sorted_string = [''.join(sorted(i)) for i in s]
    hash = {}
    for i in range(len(sorted_string)):
        if sorted_string[i] in hash:
            hash[sorted_string[i]].append(s[i])
        else:
            hash[sorted_string[i]] = [s[i]]
    return list(hash.values())


print(group_anagrams(['arc','abc','car','cat','act','acb','atc']))

