from bisect import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.insert(bisect(intervals, newInterval), newInterval)
        
        merged = []
        
        for i in range(len(intervals)):
            if not merged or intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        
        return merged