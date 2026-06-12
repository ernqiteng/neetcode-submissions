class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [-1 for i in range(len(nums))]

        if len(nums) >= 1:
            money[0] = nums[0]
        if len(nums) >= 2:
            money[1] = max(nums[0], nums[1])
        if len(nums) > 2:
            for i in range(2, len(nums)):
                money[i] = max(money[i-1], money[i-2]+nums[i])
        return max(money)

