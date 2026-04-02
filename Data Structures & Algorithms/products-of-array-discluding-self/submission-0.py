class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        index = []
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                index.append(i)
            else:
                product *= nums[i]
        
        output = [0 for i in range(len(nums))]
        if zeros > 1:
            return output
        elif zeros == 1:
            output[index[0]] = product
            return output
        else:
            for i in range(len(nums)):
                product = 1
                for j in range(len(nums)):
                    if i == j:
                        continue
                    else:
                        product *= nums[j]
                output[i] = product
            return output
