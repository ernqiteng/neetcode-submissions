class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "[":
                stack.append("]")
            elif s[i] == "(":
                stack.append(")")
            elif s[i] == "{":
                stack.append("}")
            else:
                if len(stack) != 0:
                    if s[i] != stack[-1]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True        
        else:
            return False
