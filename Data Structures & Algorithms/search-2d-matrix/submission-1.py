class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix[0])*len(matrix))-1
        while left <= right:
            mid = (left+right)//2
            row = mid//len(matrix[0])
            column = mid%len(matrix[0])
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                right = mid-1
            else:
                left = mid +1
        
        return False
