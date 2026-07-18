class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = {i:1 for i in range(len(nums))}
        lis[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        
        return max(lis.values())