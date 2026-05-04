class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #bfs
        time = 0
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row,col,0])
                elif grid[row][col] ==1:
                    fresh += 1

        
        while queue:
            row, col, time = queue.popleft()
            for r,c in directions:
                if 0<=(row+r)<len(grid) and 0<=(col+c)<len(grid[0]) and grid[row+r][col+c] == 1:
                    grid[row+r][col+c] = 2
                    queue.append([row+r,col+c,time+1])
                    fresh -= 1
        
        if fresh == 0:
            return time
        return -1