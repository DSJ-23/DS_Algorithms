from utilities import *

s = "anagram"
# print(remove_char(s, 3))


for index, value in enumerate(s):
    print(index, value)




# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#         fi = {}
#         se = {}
#         for i in s:
#             if i not in fi:
#                 fi[i] = 1
#             else:
#                 fi[i] += 1
#         for b in t:
#             if b not in se:
#                 se[b] = 1
#             else:
#                 se[b] += 1
#         if fi == se:
#             return True
#         return False

# class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
        
    #     a = {}
    #     b = {}
        
    #     for i in s:
    #         if i in a:
    #             a[i] = a[i] + 1
    #         else:
    #             a[i] = 1
        
    #     for j in t:
    #         if j in b:
    #             b[j] = b[j] + 1
    #         else:
    #             b[j] = 1
        
    #     if a == b:
    #         return True
        
    #     return False
