def palindrome(str):

    new_str = ''
    for i in reversed(range(len(str))):
        new_str += str[i]
    if new_str == str:
        return True
    return False


print(palindrome("abcba"))
# print(palindrome("malayalam"))