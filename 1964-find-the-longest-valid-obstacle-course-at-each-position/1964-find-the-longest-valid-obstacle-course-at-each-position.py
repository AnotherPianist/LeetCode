from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = [1] * len(obstacles)
        
        prefix = []
        
        for i, height in enumerate(obstacles):
            idx = bisect_right(prefix, height)
            
            if idx == len(prefix):
                prefix.append(height)
            else:
                prefix[idx] = height
            
            res[i] = idx + 1
        
        return res