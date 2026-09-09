class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        letters = {}  #value:index
        for index in range(len(nums)):
            if target-nums[index] in letters:
                return [letters[target-nums[index]],index]
            letters[nums[index]] = index