class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1 for num in nums]
        output = []

        for index in range(1,len(nums)):
            prefix.append(prefix[index-1]*nums[index-1])

        suffix[-1] = 1
        for index in range(len(nums)-2,-1,-1):
            suffix[index] = suffix[index+1]*nums[index+1]

        for index in range(len(nums)):
            output.append(prefix[index]*suffix[index])
        return output
