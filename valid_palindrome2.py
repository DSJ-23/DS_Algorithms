
class Solution:
    def validPalindrome(self, s: str) -> bool:
    
        if s == s[::-1]:
            return True
        else:
            for index, value in enumerate(s):
                ith = s[:index] + s[index+1:]
                if ith == ith[::-1]:
                    return True
        return False



def isPalindrome(self, s: str) -> bool:    
        
        a = 0
        b = len(s) -1
        
        while a <= b:
            if (s[a].isalnum() is False):
                a = a + 1
            elif s[b].isalnum() is False:
                b = b-1
            elif (s[a].isalnum() and s[b].isalnum()) and s[a].lower() == s[b].lower():
                a = a + 1
                b = b - 1
            else:
                print(s[a], s[b])
                return False
        return True