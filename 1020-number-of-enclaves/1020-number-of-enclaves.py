class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            
            for _i, _j in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1):
                if 0 <= _i < len(grid) and 0 <= _j < len(grid[0]) and grid[_i][_j]:
                    dfs(_i, _j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
                    dfs(i, j)
        
        return sum(sum(row) for row in grid)