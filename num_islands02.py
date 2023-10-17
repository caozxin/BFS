from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[bool]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def bfs(row, col):
            queue = deque([(row, col)])

            while queue:
                
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if is_valid(new_x, new_y) and grid[new_x][new_y]:
                        grid[new_x][new_y] = 0  # Mark as visited
                        queue.append((new_x, new_y))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1
                    grid[row][col] = 0  # Mark as visited
                    bfs(row, col)

        return count
new_solution = Solution()
grid = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [0,0,0,1,1],
    [0,0,0,0,0],
    [0,0,0,0,1]
    ]
# grid = [
#     [0, 1, 0],
#     [1, 0, 1],
#     [0, 1, 0]
#     ]
result = new_solution.numIslands(grid)
print("result", result)