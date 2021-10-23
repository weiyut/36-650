def palindrome(str):
    if len(str) <2:
        return True
    elif str[0] == str[-1]:
        return palindrome(str[1:-1])
    else:
        return False

print(palindrome('kayak'))
print(palindrome('hello'))