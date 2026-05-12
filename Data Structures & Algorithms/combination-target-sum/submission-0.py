class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        results = []
        def backtrack(index, path, currsum):
            if currsum == target:
                results.append(path[:])
                return
            
            if index == len(nums) or currsum + nums[index] > target:
                return
            
            path.append(nums[index])
            backtrack(index, path, currsum + nums[index])
            path.pop()
            backtrack(index+1, path, currsum)

        backtrack(0, [], 0)
        return results