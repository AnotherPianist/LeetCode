class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        delta_y, delta_x = y1 - y0, x1 - x0
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            
            if delta_y * (x - x0) != delta_x * (y - y0):
                return False
        
        return True