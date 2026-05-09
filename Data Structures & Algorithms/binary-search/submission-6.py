class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, left, right, target):
            if left > right:
                return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(nums, left, mid-1, target)
            else:
                return binarySearch(nums, mid+1, right, target)

        left = 0
        right = len(nums)-1
        return binarySearch(nums, left, right, target)

        
            
        