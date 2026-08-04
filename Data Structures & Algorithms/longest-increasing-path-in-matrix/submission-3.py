class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
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