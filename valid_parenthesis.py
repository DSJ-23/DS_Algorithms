from stack import Stack

class Solution:

    def isValid(self, s):
        valid = Stack()
        for p in s:
            if p == "(" or p == "[" or p =="{":
                valid.add(p)
            # elif p == ")" or p == "]" or p == "}":
                
        print(valid.get_stack())
        return True

a= Solution() 
print(a.isValid("()[]{"))
# print(Solution.isValid("()[]"))

