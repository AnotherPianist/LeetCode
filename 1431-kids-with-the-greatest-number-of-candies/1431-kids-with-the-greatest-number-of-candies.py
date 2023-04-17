class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        res = []
        
        for kid in candies:
            res.append(True if kid + extraCandies >= greatest else False)
        
        return res