class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        check if in bounds
        check if in visited
        check all 4 directions
        if 1 return 1
        else return 0
        get area
        update maxarea

        """
        def dfs(r,c):
            if not (0 <= r < len(grid)) or not (0 <= c < cols):
                return 0
            if (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r,c-1))

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxarea = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxarea = max(maxarea, dfs(row,col))
        return maxarea

