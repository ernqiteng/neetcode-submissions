import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        hello
        """
        stack = []
        for i in range(len(tokens)):
            try:
                num = int(tokens[i])
                stack.append(num)
                print(num)
            except:
                op2 = stack.pop()
                op1 = stack.pop()
                symbol = tokens[i]
                if symbol == "+":
                    stack.append(op1 + op2)
                elif symbol == "-":
                    stack.append(op1 - op2)
                elif symbol == "*":
                    stack.append(op1 * op2)
                elif symbol == "/":
                    if op1//op2 >= 0:
                        stack.append(op1//op2)
                    else:
                        stack.append(math.ceil(op1/op2))
                else: continue
                print(stack[-1])
        if len(stack) == 1:
            return stack[0]
        else:
            return "Error"
