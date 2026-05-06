class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        start = 0
        if len(str(x)) > 0 and str(x)[0] == "-":
            reverse = "-"
            start = 1
        else:
            reverse = ""
        for n in range(start, len(str(x))):
            stack.append(str(x)[n])
        while stack:
            reverse = reverse + stack.pop()
        reverse = int(reverse)
        if reverse < -2**31 or reverse > (2**31) -1:
            return 0
        return reverse