class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)-1):
            for j in range(i, len(heights)):
                if (j-i)*min(heights[i], heights[j]) > maxarea:
                    maxarea = (j-i)*min(heights[i], heights[j])
        return maxarea