s = "A man, a plan, a canal: Panama"

s = s.lower()
s="".join(list(filter(str.isalnum, s)))


print(s)



# You ran it twice and average runtime is faster than 97!!!

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:    
        if s == "":
            return True
        if len(s) == 1:
            return True
        
        s = s.lower()
        s="".join(list(filter(str.isalnum, s)))
        
    
        a = 0
        b = len(s) -1

        while a <= b:
            if s[a] != s[b]:
                return False
            else:
                a += 1
                b -= 1
        
        
        return True