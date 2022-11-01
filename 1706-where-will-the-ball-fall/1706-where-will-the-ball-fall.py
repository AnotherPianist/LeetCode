class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = [None] * len(grid[0])
        
        for j, col in enumerate(grid[0]):
            curr_col = j
            for i, row in enumerate(grid):
                next_col = curr_col + grid[i][curr_col]
                if next_col < 0 or next_col >= len(grid[0]) or grid[i][curr_col] != grid[i][next_col]:
                    result[j] = -1
                    break
                result[j] = next_col
                curr_col = next_col
                
        return result