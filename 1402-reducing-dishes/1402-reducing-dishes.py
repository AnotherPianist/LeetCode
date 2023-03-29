class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = total = 0
        satisfaction.sort()
        
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        
        return res