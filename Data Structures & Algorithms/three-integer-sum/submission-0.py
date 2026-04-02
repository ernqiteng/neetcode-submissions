class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        curr_nums = sorted([nums[i],nums[j],nums[k]])
                        if curr_nums in triples:
                            continue
                        else:
                            triples.append(curr_nums)
        return triples