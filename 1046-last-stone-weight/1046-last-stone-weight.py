import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            
            res = val1 - val2
            
            if res != 0:
                heapq.heappush(stones, res)
        
        return -stones[0] if stones else 0