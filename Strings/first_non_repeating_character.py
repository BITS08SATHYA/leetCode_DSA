def first_non_repeating_character(str):
    for i in range(len(str)):
        repeat = False
        for j in range(len(str)):
            if i != j and str[i] == str[j]:
                repeat = True
        if repeat == False:
            return i
    return None



print(first_non_repeating_character('abaRb150'))