import re

class Solution:
    def isPalindrome(self, s):
        valid_characters = []
        for i in s:
            if self.is_word(i):
                valid_characters.append(i.lower())
        print(valid_characters)
        if valid_characters == valid_characters[::-1]:
            return True
        else:
            return False

    def is_word(self, character):
        return bool(re.search(r'[a-z]', character, flags = re.I))


a = Solution()

print(a.isPalindrome("A man, a plan, a canal: Panama"))
# print(a.is_word('a'))