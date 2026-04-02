class Solution:
    def countBits(self, n: int) -> List[int]:
        def converttobinary(num):
            if num == 0:
                return "0"
            result = ""
            while num > 0:
                res = num % 2
                if res == 1:
                    result = "1" + result
                else:
                    result = "0" + result
                num = num // 2
            return result

        def countno1s(binary):
            total = 0
            for i in range(len(binary)):
                if binary[i] == "1":
                    total += 1
            return total

        output = []
        for i in range(0,n+1):
            print(i)
            binary = converttobinary(i)
            print(binary)
            ones = countno1s(binary)
            print(ones)
            output.append(ones)
        return output
        
        
        
        

