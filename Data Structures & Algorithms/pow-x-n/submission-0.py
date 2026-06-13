class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        num = x
        count = 1
        if n > 0:
            while count != n:
                num = num*x
                count += 1
            return num

        # num <= -1
        while count != -n:
            num = num*x
            count += 1
        return 1/num
