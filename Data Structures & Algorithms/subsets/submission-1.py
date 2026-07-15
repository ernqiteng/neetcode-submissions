class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset(index, numbers):
            if index == len(nums):
                output.append(numbers[:])
                return

            numbers.append(nums[index])
            subset(index+1, numbers)
            numbers.pop()
            subset(index+1, numbers)
        
        nums.sort()
        nums = list(set(nums))
        output = []
        subset(0, [])
        return output






