class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(heights)-1
        while left != right:
            print(left, right)
            print((right-left)*(min(heights[left], heights[right])))
            if (right-left)*(min(heights[left], heights[right])) > maxarea:
                maxarea = (right-left)*(min(heights[left], heights[right]))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxarea