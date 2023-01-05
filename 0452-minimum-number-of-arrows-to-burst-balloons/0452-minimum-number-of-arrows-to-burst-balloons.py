class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points.sort()
        
        num_arrows, arrow_start = 1, points[-1][0]
        
        for start, end in reversed(points):
            if end < arrow_start:
                arrow_start = start
                num_arrows += 1
        
        return num_arrows
            