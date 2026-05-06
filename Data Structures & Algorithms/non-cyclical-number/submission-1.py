class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquare(n):
            sum = 0
            for x in range(len(str(n))):
                sum += int(str(n)[x])*int(str(n)[x])
            return sum
        seen = set()
        curr = sumofsquare(n)
        while (curr != 1) and (curr not in seen):
            seen.add(curr)
            curr = sumofsquare(curr)
        if curr == 1:
            return True
        return False