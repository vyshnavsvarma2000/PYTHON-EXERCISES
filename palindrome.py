# WAP to check whether a string is palindrome or not

def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("racecar"))
