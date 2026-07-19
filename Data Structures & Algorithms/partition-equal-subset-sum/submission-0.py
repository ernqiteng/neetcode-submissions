class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        targetsum = sum(nums)/2

        def backtrack(cursum, index):
            if cursum == targetsum:
                return True
            if index >= len(nums):
                return False
            
            if cursum+nums[index] <= targetsum:
                return backtrack(cursum+nums[index], index+1) or backtrack(cursum, index+1)
            return backtrack(cursum, index+1)

        return backtrack(0, 0)