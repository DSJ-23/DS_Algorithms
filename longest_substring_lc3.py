class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        a_pointer = 0
        b_pointer = 0
        max_length = 0
        
        seen = {}
        
        while b_pointer < len(s):
            char = s[b_pointer]
            if char not in seen:
                seen[char] = True
                b_pointer += 1
                max_length = max(max_length, len(seen.keys()))
            else:
                seen.pop(s[a_pointer])
                a_pointer += 1
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        max_length = 0
    
        while len(s) > 0:
            temp_max = 0
            seen = {}
            for i in s:
                if i in seen:
                    break
                else:
                    temp_max += 1
                    seen[i] = True
                    max_length = max(max_length, temp_max)
            s = s[1:]
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        
        max_length = 0
        chars = list(s)
        
        while len(chars) > 0:
            temp_max = 0
            seen = {}
            for i in chars:
                if i in seen:
                    break
                else:
                    temp_max += 1
                    seen[i] = True
                    max_length = max(max_length, temp_max)
            chars.pop(0)
        return max_length