from collections import defaultdict
from math import atan2


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        
        res = 2
        m = defaultdict(int)
        
        for i in range(len(points)):
            for j in range(len(points)):
                if j != i:
                    _atan2 = atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                    m[_atan2] += 1
            res = max(res, max(m.values()) + 1)
            m.clear()
        return res