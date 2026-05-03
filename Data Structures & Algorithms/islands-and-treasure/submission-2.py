class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            row, col, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] != -1):
                    grid[nr][nc] = dist + 1
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))