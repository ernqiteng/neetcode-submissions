class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = {}
        for i in range(len(nums)):
            if nums[i] not in num:
                num[nums[i]] = 1
            else:
                num[nums[i]] += 1
        
        for key,value in num.items():
            if value == 1:
                return key