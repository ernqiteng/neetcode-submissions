class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        no way to systematically do eg from bottom right to top left because paths can be 
        either way horizontally and vertically

        can go through row by row 

        condition: if cells up/down/left/right > curr val, can be a valid path
                    check if in bounds of matrix

        could do dfs - time complexity is too high - exponential

        need to use memoisation to reduce unnecessary computation
        can save in a data structure the longest path starting from that cell

        do recursively 
        start from lowest value and go up?
        note the visited cells?            
        if in the data structure get from there
        else calculate the value
        take max of the ones around it
        """
        dp = {}
        
        def dfs(row,col):
            if (row,col) in dp:
                return dp[(row,col)]

            curr_max = 1
            #up
            if row-1 >= 0 and matrix[row-1][col] > matrix[row][col]:
                curr_max = max(curr_max, dfs(row-1,col)+1)
            #down
            if row+1 < len(matrix) and matrix[row+1][col] > matrix[row][col]:
                curr_max = max(curr_max, dfs(row+1,col)+1)
            #left
            if col-1 >= 0 and matrix[row][col-1] > matrix[row][col]:
                curr_max = max(curr_max, dfs(row,col-1)+1)
            #right
            if col+1 < len(matrix[0]) and matrix[row][col+1] > matrix[row][col]:
                curr_max = max(curr_max, dfs(row,col+1)+1)

            dp[(row,col)] = curr_max
            return curr_max
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                dfs(row,col)
        
        return max(dp.values())