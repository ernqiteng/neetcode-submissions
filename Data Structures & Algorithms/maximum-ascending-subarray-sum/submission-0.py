class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        left = 0
        sum = nums[left]
        highestsum = nums[left]
        while left < len(nums)-1:
            if nums[left] < nums[left+1]:
                sum += nums[left+1]
            else:
                sum = nums[left+1]
            left += 1
            highestsum = max(highestsum, sum)
        return highestsum