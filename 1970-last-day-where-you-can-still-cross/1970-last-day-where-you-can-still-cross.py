class Solution:
    def canCross(self, row, col, cells, day):
        grid = [[0] * col for _ in range(row)]
        
        for r, c in cells[:day]:
            grid[r - 1][c - 1] = 1
            
        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] != 0:
                return False
            if i == row - 1:
                return True
            grid[i][j] = -1
            for next_i, next_j in [(i + 1, j), (i, j + 1), (i, j - 1), (i - 1, j)]:
                if dfs(next_i, next_j):
                    return True
            return False
        
        for j in range(col):
            if grid[0][j] == 0 and dfs(0, j):
                return True

        return False
    
    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, row * col
        
        while left < right:
            mid = right - (right - left) // 2
            if self.canCross(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1
                
        return left