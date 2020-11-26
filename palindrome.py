import re


def isPalindrome(a):
    b = re.sub(r'[^a-zA-z]', "", s)
    if b[::-1].lower() == b.lower():
        return True
    else:
        return False



print(isPalindrome("A man, a plan, a canal: Panama"))

