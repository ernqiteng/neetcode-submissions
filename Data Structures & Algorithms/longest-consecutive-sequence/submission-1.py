class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        current_run = 0
        max_run = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            print(i, nums[i])
            if nums[i] == nums[i+1]:
                continue
            elif nums[i] + 1 == nums[i+1]:
                current_run += 1
            else:
                print(current_run)
                if current_run > max_run:
                    max_run = current_run
                current_run = 0
        if current_run > max_run:
            max_run = current_run
        return max_run + 1
