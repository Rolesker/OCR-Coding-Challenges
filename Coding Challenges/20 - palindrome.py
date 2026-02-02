def check_palindrome(s):
    if s==s[::-1]:
        return True
    return False

print(check_palindrome("hello"))
print(check_palindrome("radar"))