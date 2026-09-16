class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            elif char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            else:
                return False
        return True if not stack else False