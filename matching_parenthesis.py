class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                result.append(i)
            else:
                if i == ")" and result[-1] == "(":
                    result.pop()
                if i == "]" and result[-1] == "[":
                    result.pop()
                if i == "}" and result[-1] == "{":
                    result.pop()
                else:
                    return False
        return True

a = []
print(a[-1])