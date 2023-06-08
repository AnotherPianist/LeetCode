class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        count = 0
        
        for row in grid:
            left, right = 0, n - 1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
                
            count += n - left
    
        return count