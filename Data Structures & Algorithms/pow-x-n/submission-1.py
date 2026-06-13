class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n>0:
            power = n
        else:
            power = -n

        num = x
        count = 1
        while count != power:
            num = num*x
            count += 1
        if n > 0:
            return num
        return 1/num

