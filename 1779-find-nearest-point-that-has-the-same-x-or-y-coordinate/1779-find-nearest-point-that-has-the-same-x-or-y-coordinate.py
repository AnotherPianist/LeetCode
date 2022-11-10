class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float("inf")
        min_idx = -1
        
        for idx, (i, j) in enumerate(points):
            distance = abs(x - i) + abs(y - j)
            if (i == x or j == y) and distance < min_distance:
                min_distance = distance
                min_idx = idx
                
        return min_idx