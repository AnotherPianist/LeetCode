class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(i, j):
            if (border := 0 <= i < len(grid) and 0 <= j < len(grid[0])) and grid[i][j] == 0:
                grid[i][j] = 1
                return bfs(i - 1, j) + bfs(i, j + 1) + bfs(i + 1, j) + bfs(i, j - 1) == 4
            else:
                return True if border else False
            
        return sum(bfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0)