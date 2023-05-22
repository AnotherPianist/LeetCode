from collections import Counter
from heapq import nlargest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        counter = Counter(nums)
        
        return nlargest(k, counter.keys(), key=counter.get)