class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            nonlocal current_area
            if grid[i][j]:
                current_area += 1
                grid[i][j] = 0
                if i > 0:
                    dfs(i - 1, j)
                if j + 1 < len(grid[0]):
                    dfs(i, j + 1)
                if i + 1 < len(grid):
                    dfs(i + 1, j)
                if j > 0:
                    dfs(i, j - 1)
                    
        current_area = max_area = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    dfs(i, j)
                    max_area = max(current_area, max_area)
                    current_area = 0
        return max_area