import heapq
from math import floor


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-rocks for rocks in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            remaining = floor(heapq.heappop(piles) / 2)
            heapq.heappush(piles, remaining)
        
        return -sum(piles)