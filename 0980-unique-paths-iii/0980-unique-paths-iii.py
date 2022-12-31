class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        path_length = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    start = (i, j)
                elif cell == 0:
                    path_length += 1

        self.distinct_paths = 0
                    
        def dfs(i, j, formed_path):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1 and grid[i][j] != -7):
                return
            if grid[i][j] == 2:
                if formed_path - 1 == path_length:
                    self.distinct_paths += 1
                return
            grid[i][j] = -7
            for _i, _j in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(i + _i, j + _j, formed_path + 1)
            grid[i][j] = 0
        
        dfs(start[0], start[1], 0)

        return self.distinct_paths