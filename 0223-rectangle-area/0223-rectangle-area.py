class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x_overlap = min(ax2, bx2) - max(ax1, bx1)
        y_overlap = min(ay2, by2) - max(ay1, by1)
        
        area_overlap = x_overlap * y_overlap if x_overlap > 0 and y_overlap > 0 else 0
        
        return (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1) - area_overlap