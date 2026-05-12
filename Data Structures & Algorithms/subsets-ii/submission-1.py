class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []
        def backtrack(index, path):
            if index >= len(nums):
                if path[:] not in results:
                    results.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1, path)
        
        backtrack(0, [])
        return results