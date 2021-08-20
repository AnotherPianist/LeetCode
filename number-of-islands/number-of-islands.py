class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '.'
                if i > 0:
                    dfs(i - 1, j)
                if j < len(grid[0]) - 1:
                    dfs(i, j + 1)
                if i < len(grid) - 1:
                    dfs(i + 1, j)
                if j > 0:
                    dfs(i, j - 1)
                    
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
                    
        return count