class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 0
        min = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] <= min:
                min = self.stack[i]
        return min
