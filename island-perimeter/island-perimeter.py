class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    perimeter += 4
                    for ii, jj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        ii += i
                        jj += j
                        if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 1:
                            perimeter -= 1
        return perimeter