class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        setofnums = set()
        for i in range(len(nums)):
            lenbefore = len(setofnums)
            setofnums.add(nums[i])
            lenafter = len(setofnums)
            if lenbefore == lenafter:
                return nums[i]

