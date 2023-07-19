class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res, k = 0, float("-inf")
        
        for start, end in intervals:
            if start >= k:
                k = end
            else:
                res += 1
        
        return res
        