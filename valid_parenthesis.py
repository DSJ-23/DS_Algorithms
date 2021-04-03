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

class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        print(s)
        for i in s:
            if i == "(" or i == "[" or i == "{":
                result.append(i)
            else:
                if result != []:
                    if i == ")" and result[-1] == "(":
                        result.pop()
                    if i == "]" and result[-1] == "[":
                        result.pop()
                    if i == "}" and result[-1] == "{":
                        result.pop()
                else:
                    return False
        if len(result) > 0:
            return False
        return True

