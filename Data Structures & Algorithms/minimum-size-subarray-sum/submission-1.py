class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        minlen = float('inf')
        left, right = 0, 0
        while right < len(nums):
            if sum < target:
                sum += nums[right]
                right += 1
            else:
                minlen = min(minlen, right-left)
                sum -= nums[left]
                left += 1
        while sum >= target:
            minlen = min(minlen, right-left)
            sum -= nums[left]
            left += 1
        return 0 if minlen == float('inf') else minlen

        