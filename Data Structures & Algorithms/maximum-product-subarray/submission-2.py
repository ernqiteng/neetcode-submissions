class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct, minproduct, globalmaxproduct = 1, 1, nums[0]

        for num in nums:
            maxproduct, minproduct = max(num*minproduct, num*maxproduct, num), min(num*minproduct, num*maxproduct, num)
            globalmaxproduct = max(maxproduct, globalmaxproduct)

        return globalmaxproduct
