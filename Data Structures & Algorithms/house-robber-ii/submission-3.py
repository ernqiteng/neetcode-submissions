class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxmoney(nums):
            money = [-1 for i in range(len(nums))]
            if len(nums) >= 1:
                money[0] = nums[0]
            if len(nums) >= 2:
                money[1] = max(nums[0], nums[1])
            if len(nums) > 2:
                for i in range(2, len(nums)):
                    money[i] = max(money[i-1], money[i-2]+nums[i])
            return max(money)
        if len(nums) == 1:
            return nums[0]
        return max(maxmoney(nums[:-1]), maxmoney(nums[1:]))
