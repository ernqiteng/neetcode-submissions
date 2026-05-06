class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        start = 0
        x = str(x)
        if len(x) > 0 and x[0] == "-":
            reverse = "-"
            start = 1
        else:
            reverse = ""
        for n in range(start, len(x)):
            stack.append(x[n])
        while stack:
            reverse = reverse + stack.pop()
        reverse = int(reverse)
        if reverse < -2**31 or reverse > (2**31) -1:
            return 0
        return reverse