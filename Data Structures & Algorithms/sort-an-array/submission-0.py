class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(left, right):
            if len(left) > 1:
                left = sort(left[:len(left)//2], left[(len(left)//2):])
            if len(right) > 1:
                right = sort(right[:len(right)//2], right[(len(right)//2):])
            result = []
            leftpointer = 0
            rightpointer = 0
            while leftpointer != len(left) and rightpointer != len(right):
                if left[leftpointer] > right[rightpointer]:
                    result.append(right[rightpointer])
                    rightpointer += 1
                else:
                    result.append(left[leftpointer])
                    leftpointer += 1

            while leftpointer != len(left):
                result.append(left[leftpointer])
                leftpointer += 1
            while rightpointer != len(right):
                result.append(right[rightpointer])
                rightpointer += 1
            return result

        if len(nums) == 0 or len(nums) == 1:
            return nums
        return sort(nums[:len(nums)//2], nums[(len(nums)//2):])