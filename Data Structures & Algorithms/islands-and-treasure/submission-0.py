class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    queue.append([row,col,0])
                    visited.add((row,col))

        while queue:
            row, col, dist = queue.popleft()
            if grid[row][col] != -1:
                grid[row][col] = min(grid[row][col], dist)
            for r,c in directions:
                if 0 <= (row+r) < len(grid):
                    if 0 <= (col+c) < len(grid[0]):
                        if (row+r, col+c) not in visited and grid[row+r][col+c] != -1:
                            queue.append([row+r,col+c, dist+1])
                            visited.add((row+r,col+c))