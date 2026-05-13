class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        results = []
        def backtrack(index, path, currsum):
            if currsum == target:
                results.append(path[:])
                return
            
            if index == len(candidates) or currsum > target:
                return
            
            path.append(candidates[index])
            backtrack(index+1, path, currsum + candidates[index])
            path.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index+1, path, currsum)

        backtrack(0, [], 0)
        return results