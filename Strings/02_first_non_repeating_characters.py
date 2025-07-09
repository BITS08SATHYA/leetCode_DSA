def first_non_repeating_character(str):

    char_tracker = {}

    for i in str:
        if i in char_tracker:
            char_tracker[i] += 1
        else:
            char_tracker[i] = 1

    for i in range(len(str)):
        if char_tracker[str[i]] == 1:
            return str[i]

    return None



print(first_non_repeating_character('abaRbl50'))