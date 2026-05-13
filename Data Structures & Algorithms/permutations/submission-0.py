class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(path, visited):
            if len(path) == len(nums):
                results.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i] != True:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False
        
        backtrack([], [False] * len(nums))
        return results