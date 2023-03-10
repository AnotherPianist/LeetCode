from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = ceil(sum(piles) / h), max(piles)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if sum(ceil(bananas / mid) for bananas in piles) > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left